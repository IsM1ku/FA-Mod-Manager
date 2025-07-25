import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES

import mod_manager_backend as backend

# --- Dummy data for demo purposes ---
GAMES = ['Full Auto (Xbox 360)', 'Full Auto 2: Battlelines (PS3)']
DEMO_PROFILES = []
DEMO_MODS = []  # start with an empty mod list


class FAModManager(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title('Full Auto Mod Manager Prototype')
        self.geometry('800x500')
        self.minsize(720, 400)
        self.resizable(True, True)

        # Store paths to repacked smallf per profile
        self.profile_smallfs = {}

        # Load configuration
        config = backend.load_config()
        self.game_paths = {game: "" for game in GAMES}
        self.game_paths.update(config.get("game_paths", {}))
        self.logging_enabled = config.get("logging_enabled", False)
        self.comments_enabled = config.get("comments_enabled", True)
        backend.init_logger(self.logging_enabled)
        backend.init_comments(self.comments_enabled)

        # Top: Game dropdown & settings
        top_frame = tk.Frame(self)
        top_frame.pack(pady=10, fill='x')
        self.game_var = tk.StringVar(value=GAMES[0])
        ttk.Label(top_frame, text='Game:').pack(side='left', padx=5)
        # Make combobox wide enough for long game titles
        max_chars = max(len(g) for g in GAMES) + 2
        self.game_dropdown = ttk.Combobox(
            top_frame,
            values=GAMES,
            textvariable=self.game_var,
            state='readonly',
            width=max_chars,
        )
        self.game_dropdown.pack(side='left', padx=5)
        tk.Button(top_frame, text='Settings', command=self.open_settings).pack(side='right', padx=5)

        # Middle: Profiles & Mods
        main_frame = tk.Frame(self)
        main_frame.pack(padx=25, pady=5, fill='both', expand=True)

        # Left: Mod profiles
        profiles_frame = tk.LabelFrame(main_frame, text='Mod Profiles')
        profiles_frame.pack(side='left', fill='y', padx=10, ipadx=8)
        # wider listbox so placeholder text fits comfortably
        self.profile_list = tk.Listbox(profiles_frame, height=10, width=25)
        self.profile_list.pack(padx=5, pady=5)
        self.profile_placeholder = tk.Label(
            self.profile_list,
            text='No mod profiles found, create one or import one',
            foreground='gray', wraplength=180, justify='center'
        )
        self.profile_placeholder.place(relx=0.5, rely=0.5, anchor='center')

        def update_profile_placeholder(event=None):
            if self.profile_list.size() == 0:
                self.profile_placeholder.place(relx=0.5, rely=0.5, anchor='center')
            else:
                self.profile_placeholder.place_forget()

        self.update_profile_placeholder = update_profile_placeholder
        for profile in backend.list_existing_profiles():
            self.profile_list.insert('end', profile)
            self.profile_smallfs[profile] = (None, os.path.join(backend.FINISHED_DIR, profile, 'smallf.dat'))
        self.update_profile_placeholder()
        tk.Button(profiles_frame, text='Set Active', command=self.set_active_profile).pack(fill='x', pady=2)
        tk.Button(profiles_frame, text='Revert to Original', command=self.restore_original).pack(fill='x', pady=2)
        tk.Button(profiles_frame, text='Import Profile', command=self.import_profile).pack(fill='x', pady=2)
        b_frame = tk.Frame(profiles_frame)
        b_frame.pack()
        tk.Button(b_frame, text='Rename', command=self.rename_profile).pack(side='left', padx=2)
        tk.Button(b_frame, text='Delete', command=self.delete_profile).pack(side='left', padx=2)

        # Right: Mod list for selected profile
        mods_frame = tk.LabelFrame(main_frame, text='Mod List')
        mods_frame.pack(side='left', fill='both', padx=10, expand=True)
        header = tk.Frame(mods_frame)
        header.pack(fill='x', padx=5)
        header.columnconfigure(3, weight=1)
        tk.Label(header, text="", width=3).grid(row=0, column=0)
        tk.Label(header, text="Name", width=20, anchor='w').grid(row=0, column=1, sticky='w')
        tk.Label(header, text="Author", width=15, anchor='w').grid(row=0, column=2, sticky='w')
        tk.Label(header, text="Description", anchor='w').grid(row=0, column=3, sticky='w')

        # Canvas + scrollbar to allow scrolling when many mods are listed
        canvas_frame = tk.Frame(mods_frame)
        canvas_frame.pack(padx=5, pady=5, fill='both', expand=True)
        self.mods_canvas = tk.Canvas(canvas_frame, highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=self.mods_canvas.yview)
        self.mods_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.mods_canvas.pack(side="left", fill="both", expand=True)
        self.mods_container = tk.Frame(self.mods_canvas)
        self.mods_container.bind(
            "<Configure>",
            lambda e: self.mods_canvas.configure(scrollregion=self.mods_canvas.bbox("all"))
        )
        self.mods_canvas.create_window((0, 0), window=self.mods_container, anchor="nw")
        self.mods_canvas.bind_all(
            "<MouseWheel>",
            lambda e: self.mods_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        )
        self.mod_entries = []
        self.selected_mod_index = None
        self.mods_canvas.drop_target_register(DND_FILES)
        self.mods_canvas.dnd_bind('<<Drop>>', self.on_file_drop)
        self.mods_container.drop_target_register(DND_FILES)
        self.mods_container.dnd_bind('<<Drop>>', self.on_file_drop)
        self.mods_placeholder = tk.Label(
            self.mods_container,
            text='Drag mods here or use "Add Files"',
            foreground='gray'
        )
        self.mods_placeholder.place(relx=0.5, rely=0.5, anchor='center')

        def update_placeholder(event=None):
            if len(self.mod_entries) == 0:
                self.mods_placeholder.place(relx=0.5, rely=0.5, anchor='center')
            else:
                self.mods_placeholder.place_forget()

        self.update_mod_placeholder = update_placeholder
        self.update_mod_placeholder()

        btn_frame = tk.Frame(mods_frame)
        btn_frame.pack(pady=4)
        tk.Button(btn_frame, text='Up', width=6, command=self.move_up).pack(side='left', padx=2)
        tk.Button(btn_frame, text='Down', width=6, command=self.move_down).pack(side='left', padx=2)
        tk.Button(btn_frame, text='Remove', width=8, command=self.remove_selected_mods).pack(side='left', padx=2)
        tk.Button(btn_frame, text='Clear', width=6, command=self.clear_mods).pack(side='left', padx=2)
        tk.Button(btn_frame, text='Add Files', command=self.add_files).pack(side='left', padx=2)
        tk.Button(mods_frame, text='Merge', command=self.merge_mods).pack(pady=4, fill='x')

    def open_settings(self):
        win = tk.Toplevel(self)
        win.title("Settings")
        entries = {}
        row = 0
        for game in GAMES:
            tk.Label(win, text=game).grid(row=row, column=0, sticky="w", padx=5, pady=2)
            var = tk.StringVar(value=self.game_paths.get(game, ""))
            tk.Entry(win, textvariable=var, width=40).grid(row=row, column=1, padx=5)

            def browse(g=game, v=var):
                path = filedialog.askdirectory(title=f"Select folder for {g}", mustexist=True)
                if path:
                    v.set(path)

            tk.Button(win, text="Browse", command=browse).grid(row=row, column=2, padx=5)
            entries[game] = var
            row += 1

        log_var = tk.BooleanVar(value=self.logging_enabled)
        tk.Checkbutton(win, text="Enable logging", variable=log_var).grid(row=row, column=0, columnspan=3, sticky="w", pady=4, padx=5)
        row += 1
        comment_var = tk.BooleanVar(value=self.comments_enabled)
        tk.Checkbutton(win, text="Add mod comments (experimental)", variable=comment_var).grid(row=row, column=0, columnspan=3, sticky="w", pady=2, padx=5)
        row += 1

        def save():
            for g, var in entries.items():
                self.game_paths[g] = var.get()
            self.logging_enabled = log_var.get()
            self.comments_enabled = comment_var.get()
            backend.save_config({"game_paths": self.game_paths, "logging_enabled": self.logging_enabled, "comments_enabled": self.comments_enabled})
            backend.init_logger(self.logging_enabled)
            backend.init_comments(self.comments_enabled)
            win.destroy()

        tk.Button(win, text="Save", command=save).grid(row=row, column=0, columnspan=3, pady=5)

    def set_active_profile(self):
        selected = self.profile_list.curselection()
        if not selected:
            messagebox.showwarning("Select a Profile", "No profile selected!")
            return

        profile = self.profile_list.get(selected[0])
        info = self.profile_smallfs.get(profile)
        if not info:
            messagebox.showwarning("Build Missing", "Run Merge for this profile first.")
            return

        game_key, _ = info
        if game_key is None:
            game_key = "fa2" if "Full Auto 2" in self.game_var.get() else "fa"
        selected_game = self.game_var.get()
        game_root = self.game_paths.get(selected_game, "")
        if not game_root:
            messagebox.showerror("Error", "Game folder not set. Please use Settings first.")
            return

        try:
            backend.export_smallf_to_game(game_key, profile, game_root)
            messagebox.showinfo("Active Profile", f"Copied modified smallf for '{profile}' to game folder.")
        except Exception as exc:
            messagebox.showerror("Error", f"Failed to export:\n{exc}")

    def rename_profile(self):
        selected = self.profile_list.curselection()
        if selected:
            old_name = self.profile_list.get(selected[0])
            new_name = simpledialog.askstring("Rename Profile", f"Enter new name for '{old_name}':")
            if new_name and new_name != old_name:
                try:
                    new_path = backend.rename_profile(old_name, new_name)
                except Exception as exc:
                    messagebox.showerror("Error", f"Failed to rename profile:\n{exc}")
                    return
                self.profile_list.delete(selected[0])
                self.profile_list.insert(selected[0], new_name)
                game_key, _ = self.profile_smallfs.pop(old_name, (None, None))
                self.profile_smallfs[new_name] = (game_key, new_path)
        else:
            messagebox.showwarning("Select a Profile", "No profile selected!")

    def delete_profile(self):
        selected = self.profile_list.curselection()
        if selected:
            name = self.profile_list.get(selected[0])
            self.profile_list.delete(selected[0])
            self.profile_smallfs.pop(name, None)
        else:
            messagebox.showwarning("Select a Profile", "No profile selected!")

    def restore_original(self):
        selected_game = self.game_var.get()
        game_key = 'fa2' if 'Full Auto 2' in selected_game else 'fa'
        game_root = self.game_paths.get(selected_game, '')
        if not game_root:
            messagebox.showerror("Error", "Game folder not set. Please use Settings first.")
            return
        try:
            backend.restore_original_smallf(game_key, game_root)
            messagebox.showinfo("Restored", "Original smallf.dat restored.")
        except Exception as exc:
            messagebox.showerror("Error", f"Failed to restore original:\n{exc}")

    def import_profile(self):
        folder = filedialog.askdirectory(title='Select folder with smallf.dat', mustexist=True)
        if not folder:
            return
        smallf_path = os.path.join(folder, 'smallf.dat')
        if not os.path.isfile(smallf_path):
            messagebox.showerror('Error', 'smallf.dat not found in selected folder.')
            return
        profile_name = os.path.basename(folder)
        selected_game = self.game_var.get()
        game_key = 'fa2' if 'Full Auto 2' in selected_game else 'fa'
        dest = backend.import_profile(game_key, profile_name, smallf_path)
        self.profile_smallfs[profile_name] = (game_key, dest)
        if profile_name not in self.profile_list.get(0, 'end'):
            self.profile_list.insert('end', profile_name)
        self.update_profile_placeholder()

    # --- Mod list helpers ---
    def _add_mod(self, path):
        idx = len(self.mod_entries)
        var = tk.BooleanVar(value=True)
        try:
            meta, _ = backend._parse_mod_file(path)
        except Exception:
            meta = {}

        name = meta.get('name')
        author = meta.get('author')
        desc = meta.get('description')

        row = tk.Frame(self.mods_container)
        row.columnconfigure(3, weight=1)
        cb = tk.Checkbutton(row, variable=var)
        cb.grid(row=0, column=0, padx=2)

        name_lbl = tk.Label(row, text=name or os.path.basename(path), anchor='w', width=20)
        name_lbl.grid(row=0, column=1, sticky='w')
        tk.Label(row, text=author or '', anchor='w', width=15).grid(row=0, column=2, sticky='w')
        tk.Label(row, text=desc or '', anchor='w', wraplength=400, justify='left').grid(row=0, column=3, sticky='ew')

        row.bind('<Button-1>', lambda e, i=idx: self.select_mod(i))
        for child in row.winfo_children():
            child.bind('<Button-1>', lambda e, i=idx: self.select_mod(i))

        row.pack(anchor='w', fill='x', pady=1)
        self.mod_entries.append({'path': path, 'var': var, 'widget': row})
        self.update_mod_placeholder()

    def on_file_drop(self, event):
        files = self.tk.splitlist(event.data)
        for path in files:
            if os.path.isfile(path) and path.lower().endswith('.txt'):
                self._add_mod(path)
        if files:
            self.update_mod_placeholder()

    def add_files(self):
        paths = filedialog.askopenfilenames(
            title='Select Mod Files',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        for path in paths:
            if os.path.isfile(path) and path.lower().endswith('.txt'):
                self._add_mod(path)
        if paths:
            self.update_mod_placeholder()

    def select_mod(self, index):
        if self.selected_mod_index is not None and 0 <= self.selected_mod_index < len(self.mod_entries):
            old_row = self.mod_entries[self.selected_mod_index]['widget']
            for child in old_row.winfo_children():
                child.configure(background=old_row.cget('background'))
            old_row.configure(background=self.mods_container.cget('background'))
        self.selected_mod_index = index
        new_row = self.mod_entries[index]['widget']
        new_row.configure(background='lightblue')
        for child in new_row.winfo_children():
            child.configure(background='lightblue')

    def remove_selected_mods(self):
        idx = self.selected_mod_index
        if idx is None:
            return
        entry = self.mod_entries.pop(idx)
        entry['widget'].destroy()
        self.selected_mod_index = None
        self.update_mod_placeholder()

    def clear_mods(self):
        for entry in self.mod_entries:
            entry['widget'].destroy()
        self.mod_entries.clear()
        self.selected_mod_index = None
        self.update_mod_placeholder()

    def refresh_mod_widgets(self):
        for entry in self.mod_entries:
            entry['widget'].pack_forget()
        for entry in self.mod_entries:
            entry['widget'].pack(anchor='w', fill='x')
        if self.selected_mod_index is not None and 0 <= self.selected_mod_index < len(self.mod_entries):
            self.select_mod(self.selected_mod_index)
        # update scroll region whenever the mod list changes
        self.mods_canvas.configure(scrollregion=self.mods_canvas.bbox("all"))

    def move_up(self):
        idx = self.selected_mod_index
        if idx is None or idx == 0:
            return
        self.mod_entries[idx-1], self.mod_entries[idx] = self.mod_entries[idx], self.mod_entries[idx-1]
        self.selected_mod_index -= 1
        self.refresh_mod_widgets()
        self.select_mod(self.selected_mod_index)

    def move_down(self):
        idx = self.selected_mod_index
        if idx is None or idx >= len(self.mod_entries) - 1:
            return
        self.mod_entries[idx+1], self.mod_entries[idx] = self.mod_entries[idx], self.mod_entries[idx+1]
        self.selected_mod_index += 1
        self.refresh_mod_widgets()
        self.select_mod(self.selected_mod_index)

    def merge_mods(self):
        mod_paths = [e['path'] for e in self.mod_entries if e['var'].get()]
        if not mod_paths:
            messagebox.showwarning("Select Mods", "No mods selected to merge!")
            return

        merge_name = simpledialog.askstring("Merge Name", "Enter name for merged mod:")
        if not merge_name:
            return

        selected_game = self.game_var.get()
        game_key = "fa2" if "Full Auto 2" in selected_game else "fa"

        try:
            backend.unpack_smallf(game_key)
            backend.apply_mods_to_temp(game_key, mods=mod_paths, merge_name=merge_name)
            out_path = backend.repack_smallf(game_key, merge_name)
            self.profile_smallfs[merge_name] = (game_key, out_path)
            if merge_name not in self.profile_list.get(0, 'end'):
                self.profile_list.insert('end', merge_name)
                self.update_profile_placeholder()
            messagebox.showinfo(
                "Merge Complete",
                f"Repacked smallf '{merge_name}' saved to:\n{out_path}"
            )
        except Exception as exc:
            messagebox.showerror("Error", f"Merge failed:\n{exc}")

if __name__ == "__main__":
    app = FAModManager()
    app.mainloop()
