import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES

from config_manager import BUNDLED_DIR

# Directory containing the original FA2 music files shipped with the manager
MUSIC_ORIG_DIR = os.path.join(BUNDLED_DIR, "music", "fa2")


def _music_dir(game_root):
    """Return the fa2_rxx music directory within ``game_root``."""
    return os.path.join(game_root, "PS3_GAME", "USRDIR", "media", "fa2_rxx")


def list_music_files(game_root):
    """Return a list of dictionaries with ``name`` and ``status`` for each .yuk file."""
    music_dir = _music_dir(game_root)
    os.makedirs(music_dir, exist_ok=True)
    files = []
    for name in sorted(os.listdir(music_dir)):
        if not name.lower().endswith(".yuk"):
            continue
        path = os.path.join(music_dir, name)
        status = "custom"
        orig_path = os.path.join(MUSIC_ORIG_DIR, name)
        if os.path.isfile(orig_path):
            if os.path.getsize(orig_path) == os.path.getsize(path):
                status = "original"
            else:
                status = "modified"
        files.append({"name": name, "status": status})
    return files


def add_music_files(game_root, paths):
    """Copy the given .yuk files into the game's music folder."""
    music_dir = _music_dir(game_root)
    os.makedirs(music_dir, exist_ok=True)
    for src in paths:
        if not os.path.isfile(src):
            continue
        dest = os.path.join(music_dir, os.path.basename(src))
        shutil.copy2(src, dest)


def remove_music_files(game_root, names):
    """Remove the specified files from the music folder."""
    music_dir = _music_dir(game_root)
    for name in names:
        path = os.path.join(music_dir, name)
        if os.path.isfile(path):
            os.remove(path)


def revert_music_file(game_root, name):
    """Restore a single track from the bundled originals."""
    src = os.path.join(MUSIC_ORIG_DIR, name)
    if not os.path.isfile(src):
        return
    dest = os.path.join(_music_dir(game_root), name)
    shutil.copy2(src, dest)


def revert_all_music(game_root):
    """Restore all original tracks from the bundled folder."""
    music_dir = _music_dir(game_root)
    os.makedirs(music_dir, exist_ok=True)
    for name in os.listdir(MUSIC_ORIG_DIR):
        src = os.path.join(MUSIC_ORIG_DIR, name)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(music_dir, name))


class MusicManagerWindow(tk.Toplevel):
    def __init__(self, master, game_root):
        super().__init__(master)
        self.title("Full Auto 2 Music Manager")
        self.transient(master)
        self.grab_set()
        self.game_root = game_root

        self.file_list = []

        main = tk.Frame(self)
        main.pack(padx=10, pady=10, fill="both", expand=True)
        list_frame = tk.Frame(main)
        list_frame.pack(side="left", fill="both", expand=True)

        self.listbox = tk.Listbox(list_frame)
        self.listbox.pack(side="left", fill="both", expand=True)
        sb = tk.Scrollbar(list_frame, command=self.listbox.yview)
        sb.pack(side="right", fill="y")
        self.listbox.configure(yscrollcommand=sb.set)
        self.listbox.bind("<<ListboxSelect>>", self.update_details)
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind("<<Drop>>", self.on_drop)

        right = tk.Frame(main)
        right.pack(side="left", padx=10, fill="y")

        self.info = tk.Label(right, text="")
        self.info.pack(anchor="w")

        tk.Button(right, text="Add .yuk File", command=self.add_file).pack(fill="x", pady=2)
        tk.Button(right, text="Remove Selected", command=self.remove_selected).pack(fill="x", pady=2)
        tk.Button(right, text="Revert Selected to Original", command=self.revert_selected).pack(fill="x", pady=2)
        tk.Button(right, text="Revert All Originals", command=self.revert_all).pack(fill="x", pady=2)

        self.refresh_list()

    def on_drop(self, event):
        files = self.tk.splitlist(event.data)
        add_music_files(self.game_root, [f for f in files if f.lower().endswith(".yuk")])
        self.refresh_list()

    def add_file(self):
        paths = filedialog.askopenfilenames(parent=self, title="Select .yuk files", filetypes=[("YUK files", "*.yuk"), ("All Files", "*.*")])
        add_music_files(self.game_root, paths)
        self.refresh_list()

    def remove_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        name = self.file_list[sel[0]]["name"]
        remove_music_files(self.game_root, [name])
        self.refresh_list()

    def revert_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        name = self.file_list[sel[0]]["name"]
        revert_music_file(self.game_root, name)
        self.refresh_list()

    def revert_all(self):
        revert_all_music(self.game_root)
        self.refresh_list()

    def refresh_list(self):
        self.file_list = list_music_files(self.game_root)
        self.listbox.delete(0, tk.END)
        for info in self.file_list:
            prefix = {
                "original": "\u2705",
                "modified": "\u26A0\ufe0f",
                "custom": "\u2753",
            }.get(info["status"], "")
            self.listbox.insert(tk.END, f"{prefix} {info['name']}")
        self.info.configure(text="")

    def update_details(self, event=None):
        sel = self.listbox.curselection()
        if not sel:
            self.info.configure(text="")
            return
        info = self.file_list[sel[0]]
        self.info.configure(text=f"File: {info['name']}\nStatus: {info['status'].capitalize()}")


