# Full Auto Mod Manager

This project provides a proof of concept for managing and merging mods for **Full Auto** (Xbox 360) and **Full Auto 2: Battlelines** (PS3). It relies on command line tools to unpack and repack `smallf.dat` so that modified files can be exported back to the game.

## Requirements

- Windows operating system. The repo includes Windows executables used to unpack and repack game data:
  - `smallf/tools/unpack_smallf_win.exe`
  - `smallf/tools/repack_smallf_win.exe`
- Python 3 with Tkinter for the GUI (`mod_manager.py`).

## Configuring Game Paths

Game directories are stored in `fa_mod_manager_config.json`. Each key is the game name and the value is the path to the game's root folder. The JSON looks like the following:

```json
{
    "Full Auto (Xbox 360)": "C:/Path/To/Full Auto",
    "Full Auto 2: Battlelines (PS3)": "C:/Path/To/Full Auto 2"
}
```

Use the **Settings** button in the GUI to select or update these paths. The backend saves them using `save_game_paths()` and they are loaded on startup via `load_game_paths()`.

## Basic Workflow

1. **Unpack** – `backend.unpack_smallf(game)` copies the original `smallf.dat` and unpacks it using `unpack_smallf_win.exe`.
2. **Apply Mods** – modify files in the temporary folder (handled by `apply_mods_to_temp`).
3. **Repack** – `backend.repack_smallf(game, mod_name)` copies the unpacked files
   into `smallf/tools` and runs `repack_smallf_win.exe` without arguments. The
   resulting file is stored under `smallf/finished/<mod_name>/smallf.dat`.
4. **Export** – `backend.export_smallf_to_game(game, mod_name, game_root)` copies the new file to `PS3_GAME/USRDIR/smallf_modified.dat` in your configured game directory.

This sequence is also demonstrated in the `__main__` section of `mod_manager_backend.py` and forms the foundation of the GUI.

## Adding Mods

Mods can be added to the list either by dragging `.txt` files onto the mod list
or by clicking the **Add Files** button which opens your system's file picker.
Each mod entry now has a checkbox allowing you to enable or disable it for the
next merge. When no mods are loaded, the list shows a helpful "Drag mods here" hint.

### Importing Mod Profiles

Existing `smallf.dat` files can be imported as mod profiles using the **Import
Profile** button. Choose a folder containing a `smallf.dat` and it will appear
in the profile list using the folder name.
