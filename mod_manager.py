import os
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

# --- Dummy data for demo purposes ---
GAMES = ['Full Auto (Xbox 360)', 'Full Auto 2: Battlelines (PS3)']
DEMO_PROFILES = ['Default', 'Debug', 'Modded Physics']
DEMO_MODS = ['Weapon Overhaul', 'Classic Music Pack', 'Wreck Tweaks']

CONFIG_FILE = "fa_mod_manager_config.json"

def save_game_paths(game_paths):
    with open(CONFIG_FILE, "w") as f:
        json.dump(game_paths, f)

def load_game_paths():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

class FAModManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Full Auto Mod Manager Prototype')
        self.geometry('720x400')
        self.resizable(False, False)

        # Load or create game paths config
        self.game_paths = {game: "" for game in GAMES}
        self.game_paths.update(load_game_paths())

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
        self.mods_list = tk.Listbox(mods_frame, height=10, selectmode='multiple')
        for mod in DEMO_MODS:
            self.mods_list.insert('end', mod)
        self.mods_list.pack(padx=5, pady=5, fill='both', expand=True)
        tk.Button(mods_frame, text='Merge', command=self.merge_mods).pack(pady=4, fill='x')

    def open_settings(self):
        selected_game = self.game_var.get()
        directory = filedialog.askdirectory(
            title=f"Select game folder for {selected_game}",
            mustexist=True
        )
        if directory:
            self.game_paths[selected_game] = directory
            save_game_paths(self.game_paths)
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
        if selected:
            messagebox.showinfo("Active Profile", f"Set '{self.profile_list.get(selected[0])}' as active.")
        else:
            messagebox.showwarning("Select a Profile", "No profile selected!")

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

    def merge_mods(self):
        # Example use of the saved path (replace with real logic as needed)
        selected_game = self.game_var.get()
        game_root = self.game_paths.get(selected_game, "")
        if not game_root:
            messagebox.showerror("Error", "Game folder not set. Please use Settings first.")
            return

        smallf_path = os.path.join(game_root, "PS3_GAME", "USRDIR", "smallf.dat")
        if not os.path.isfile(smallf_path):
            messagebox.showerror("Error", "Could not find smallf.dat in your game folder.")
            return

        dest_path = os.path.join(game_root, "PS3_GAME", "USRDIR", "smallf_modified.dat")

        # Replace with real merge/copy logic
        messagebox.showinfo(
            "Merge",
            f"Would now patch/replace:\n{smallf_path}\n"
            f"Export would be written to:\n{dest_path}"
        )

if __name__ == "__main__":
    app = FAModManager()
    app.mainloop()
