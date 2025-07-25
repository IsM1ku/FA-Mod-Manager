# Full Auto Mod Manager

This project provides a proof of concept for managing and merging mods for **Full Auto** (Xbox 360) and **Full Auto 2: Battlelines** (PS3). It relies on command line tools to unpack and repack `smallf.dat` so that modified files can be exported back to the game.

## Requirements

- Windows operating system. The repo includes Windows executables used to unpack and repack game data:
  - `bundled/tools/unpack_smallf_win.exe`
  - `bundled/tools/repack_smallf_win.exe`
- Python 3 with Tkinter for the GUI (`mod_manager.py`).
When packaged with PyInstaller the `bundled` directory is included inside the executable while
`mod_profiles`, `smallf`, `exiso`, and `xbox_extract` remain next to the program so they can be modified by the user. If
`bundled/tools` is missing the program falls back to `smallf/tools` for compatibility with older setups.

## Configuring Game Paths

Game directories and settings are stored in `fa_mod_manager_config.json`. The JSON looks like the following:

```json
{
    "game_paths": {
        "Full Auto (Xbox 360)": "C:/Path/To/Full Auto",
        "Full Auto 2: Battlelines (PS3)": "C:/Path/To/Full Auto 2"
    },
    "logging_enabled": false,
    "comments_enabled": true
}
```

Use the **Settings** button in the GUI to select or update these paths, toggle logging, and enable/disable the experimental comment feature. The backend saves them using `save_config()` and they are loaded on startup via `load_config()`.

## Basic Workflow

1. **Unpack** – `backend.unpack_smallf(game)` copies the original `smallf.dat` and unpacks it using `unpack_smallf_win.exe`.
2. **Apply Mods** – modify files in the temporary folder (handled by `apply_mods_to_temp`).
3. **Repack** – `backend.repack_smallf(game, mod_name)` copies the unpacked files
   into `bundled/tools` and runs `repack_smallf_win.exe` without arguments. The
   resulting file is stored under `mod_profiles/<game>/<mod_name>/smallf.dat`.
4. **Export** – `backend.export_smallf_to_game(game, mod_name, game_root)` copies the new file back to the game. On PS3 it is placed in `PS3_GAME/USRDIR/smallf.dat`, while the Xbox 360 version expects `smallF.dat` directly in the game root. Use the **Revert to Original** button to restore the vanilla file.

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

### Xbox 360 ISO Extraction

The `exiso` folder contains the `extract-xiso` tool used to unpack Xbox 360 ISOs.
Select an ISO and extraction folder from the **Settings** menu and click
**Extract ISO** to unpack the game. The contents are placed inside a folder named
after the ISO within the chosen directory. By default this directory is
`xbox_extract` next to the program.
