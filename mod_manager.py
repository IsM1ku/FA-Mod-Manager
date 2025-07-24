import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES

import mod_manager_backend as backend

# --- Dummy data for demo purposes ---
GAMES = ['Full Auto (Xbox 360)', 'Full Auto 2: Battlelines (PS3)']
DEMO_PROFILES = ['Default', 'Debug', 'Modded Physics']
DEMO_MODS = []  # start with an empty mod list


class FAModManager(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title('Full Auto Mod Manager Prototype')
        self.geometry('720x400')
        self.resizable(False, False)

        # Store paths to repacked smallf per profile
        self.profile_smallfs = {}
        # List of mod file paths corresponding to entries in the listbox
        self.mod_files = []

        # Load or create game paths config
        self.game_paths = {game: "" for game in GAMES}
        self.game_paths.update(backend.load_game_paths())

        # Top: Game dropdown & settings
        top_frame = tk.Frame(self)
        top_frame.pack(pady=10, fill='x')
        self.game_var = tk.StringVar(value=GAMES[0])
        ttk.Label(top_frame, text='Game:').pack(side='left', padx=5)
        self.game_dropdown = ttk.Combobox(top_frame, values=GAMES, textvariable=self.game_var, state='readonly')
        self.game_dropdown.pack(side='left', padx=5)
        tk.Button(top_frame, text='Settings', command=self.open_settings).pack(side='right', padx=5)

        # Middle: Profiles & Mods
        main_frame = tk.Frame(self)
        main_frame.pack(padx=25, pady=5, fill='both', expand=True)

        # Left: Mod profiles
        profiles_frame = tk.LabelFrame(main_frame, text='Mod Profiles')
        profiles_frame.pack(side='left', fill='y', padx=10, ipadx=8)
        self.profile_list = tk.Listbox(profiles_frame, height=10)
        for profile in DEMO_PROFILES:
            self.profile_list.insert('end', profile)
        self.profile_list.pack(padx=5, pady=5)
        tk.Button(profiles_frame, text='Set Active', command=self.set_active_profile).pack(fill='x', pady=2)
        b_frame = tk.Frame(profiles_frame)
        b_frame.pack()
        tk.Button(b_frame, text='Rename', command=self.rename_profile).pack(side='left', padx=2)
        tk.Button(b_frame, text='Delete', command=self.delete_profile).pack(side='left', padx=2)

        # Right: Mod list for selected profile
        mods_frame = tk.LabelFrame(main_frame, text='Mod List')
        mods_frame.pack(side='left', fill='both', padx=10, expand=True)
        self.mods_list = tk.Listbox(mods_frame, height=10, selectmode='extended')
        self.mods_list.pack(padx=5, pady=5, fill='both', expand=True)
        # placeholder label shown when no mods are listed
        self.mods_placeholder = tk.Label(
            self.mods_list, text='Drag mods here or use "Add Files"',
            foreground='gray'
        )
        self.mods_placeholder.place(relx=0.5, rely=0.5, anchor='center')
        # Enable drag-and-drop of txt files into the listbox
        self.mods_list.drop_target_register(DND_FILES)
        self.mods_list.dnd_bind('<<Drop>>', self.on_file_drop)

        def update_placeholder(event=None):
            if self.mods_list.size() == 0:
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
        selected_game = self.game_var.get()
        directory = filedialog.askdirectory(
            title=f"Select game folder for {selected_game}",
            mustexist=True
        )
        if directory:
            self.game_paths[selected_game] = directory
            backend.save_game_paths(self.game_paths)
            smallf_path = None

            if "Full Auto 2" in selected_game:
                candidate = os.path.join(directory, "PS3_GAME", "USRDIR", "smallf.dat")
                if os.path.isfile(candidate):
                    smallf_path = candidate

            # Add logic for other games as needed

            if smallf_path:
                messagebox.showinfo("File Found", f"Found smallf.dat at:\n{smallf_path}")
            else:
                messagebox.showerror("Not Found", "Could not find smallf.dat at PS3_GAME/USRDIR/ in the selected folder.")
        else:
            messagebox.showwarning("No folder selected", "Please select a folder.")

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
            if new_name:
                self.profile_list.delete(selected[0])
                self.profile_list.insert(selected[0], new_name)
        else:
            messagebox.showwarning("Select a Profile", "No profile selected!")

    def delete_profile(self):
        selected = self.profile_list.curselection()
        if selected:
            self.profile_list.delete(selected[0])
        else:
            messagebox.showwarning("Select a Profile", "No profile selected!")

    # --- Mod list helpers ---
    def on_file_drop(self, event):
        files = self.tk.splitlist(event.data)
        for path in files:
            if os.path.isfile(path) and path.lower().endswith('.txt'):
                self.mods_list.insert('end', os.path.basename(path))
                self.mod_files.append(path)
        self.update_mod_placeholder()

    def add_files(self):
        paths = filedialog.askopenfilenames(
            title='Select Mod Files',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        for path in paths:
            if os.path.isfile(path) and path.lower().endswith('.txt'):
                self.mods_list.insert('end', os.path.basename(path))
                self.mod_files.append(path)
        if paths:
            self.update_mod_placeholder()

    def remove_selected_mods(self):
        selection = list(self.mods_list.curselection())
        if not selection:
            return
        for index in reversed(selection):
            self.mods_list.delete(index)
            del self.mod_files[index]
        self.update_mod_placeholder()

    def clear_mods(self):
        self.mods_list.delete(0, 'end')
        self.mod_files.clear()
        self.update_mod_placeholder()

    def move_up(self):
        selection = self.mods_list.curselection()
        if not selection:
            return
        index = selection[0]
        if index == 0:
            return
        item = self.mods_list.get(index)
        self.mods_list.delete(index)
        self.mods_list.insert(index - 1, item)
        self.mod_files.insert(index - 1, self.mod_files.pop(index))
        self.mods_list.selection_set(index - 1)

    def move_down(self):
        selection = self.mods_list.curselection()
        if not selection:
            return
        index = selection[0]
        if index == self.mods_list.size() - 1:
            return
        item = self.mods_list.get(index)
        self.mods_list.delete(index)
        self.mods_list.insert(index + 1, item)
        self.mod_files.insert(index + 1, self.mod_files.pop(index))
        self.mods_list.selection_set(index + 1)

    def merge_mods(self):
        mod_indices = list(self.mods_list.curselection())
        if not mod_indices:
            messagebox.showwarning("Select Mods", "No mods selected to merge!")
            return

        merge_name = simpledialog.askstring("Merge Name", "Enter name for merged mod:")
        if not merge_name:
            return

        selected_game = self.game_var.get()
        game_key = "fa2" if "Full Auto 2" in selected_game else "fa"
        mod_paths = [self.mod_files[i] for i in mod_indices]

        try:
            backend.unpack_smallf(game_key)
            backend.apply_mods_to_temp(game_key, mods=mod_paths)
            out_path = backend.repack_smallf(game_key, merge_name)
            self.profile_smallfs[merge_name] = (game_key, out_path)
            if merge_name not in self.profile_list.get(0, 'end'):
                self.profile_list.insert('end', merge_name)
            messagebox.showinfo(
                "Merge Complete",
                f"Repacked smallf '{merge_name}' saved to:\n{out_path}"
            )
        except Exception as exc:
            messagebox.showerror("Error", f"Merge failed:\n{exc}")

if __name__ == "__main__":
    app = FAModManager()
    app.mainloop()
