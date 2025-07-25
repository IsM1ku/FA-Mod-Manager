
# Full Auto Mod Manager v2

**Full Auto Mod Manager v2** is a fully functional modding and merging tool for **Full Auto** (Xbox 360) and **Full Auto 2: Battlelines** (PS3).  
It enables easy management, merging, and deployment of mods, supporting both games with robust features and an evolving set of planned improvements.  
The manager relies on command line tools to unpack and repack `smallf.dat` so that modified files can be exported back to the game.

## Credits and Third-Party Tools

This project relies on several external tools, which are included or used by the mod manager:

- **smallf unpacker & repacker**  
  - Original code by **Protorizer**  
  - Used for extracting and rebuilding `smallf.dat` archives for Full Auto and Full Auto 2: Battlelines.  
  - Binaries are included in this repository with permission.

- **extract-xiso**  
  - Original project by [in@fishtank.com](mailto:in@fishtank.com), maintained by the [XboxDev team](https://github.com/XboxDev/extract-xiso).  
  - Used for extracting Xbox 360 ISO images.  
  - Licensed under a modified BSD-style license (see `LICENSE.TXT` for details).  
  - Download the latest version or find source code at: https://github.com/XboxDev/extract-xiso

**If you use these tools, please consider crediting the original authors in your projects as well.**

---

## Requirements

- Windows operating system. The repo includes Windows executables used to unpack and repack game data:
  - `bundled/tools/unpack_smallf_win.exe`
  - `bundled/tools/repack_smallf_win.exe`
- Python 3 with Tkinter for the GUI (`mod_manager.py`).
- Pillow for image loading and scaling.

When packaged with PyInstaller, the `bundled` directory is included inside the executable while
`mod_profiles`, `smallf`, `exiso`, and `xbox_extract` remain next to the program so they can be modified by the user. If
`bundled/tools` is missing the program falls back to `smallf/tools` for compatibility with older setups.

---

## Configuring Game Paths

Game directories and settings are stored in `fa_mod_manager_config.json`. The JSON looks like the following:

```json
{
    "game_paths": {
        "Full Auto (Xbox 360)": "C:/Path/To/Full Auto",
        "Full Auto 2: Battlelines (PS3)": "C:/Path/To/Full Auto 2"
    },
    "logging_enabled": false,
    "comments_enabled": true,
    "xbox_iso": "C:/ISOs/FullAuto.iso",
    "extract_root": "C:/Path/To/XboxExtract"
}
```

Use the **Settings** button in the GUI to select or update these paths, toggle logging, and enable/disable the experimental comment feature. The backend saves them using `save_config()` and they are loaded on startup via `load_config()`. The same file also stores the last Xbox 360 ISO you opened (`xbox_iso`) and the folder used for extraction (`extract_root`).

---

## Basic Workflow

1. **Unpack** – `backend.unpack_smallf(game)` copies the original `smallf.dat` and unpacks it using `unpack_smallf_win.exe`.
2. **Apply Mods** – modify files in the temporary folder (handled by `apply_mods_to_temp`).
3. **Repack** – `backend.repack_smallf(game, mod_name)` copies the unpacked files
   into `bundled/tools` and runs `repack_smallf_win.exe` without arguments. The
   resulting file is stored under `mod_profiles/<game>/<mod_name>/smallf.dat`.
4. **Export** – `backend.export_smallf_to_game(game, mod_name, game_root)` copies the new file back to the game. On PS3 it is placed in `PS3_GAME/USRDIR/smallf.dat`, while the Xbox 360 version expects `smallF.dat` directly in the game root. Use the **Revert to Original** button to restore the vanilla file.

This sequence is also demonstrated in the `__main__` section of `mod_manager_backend.py` and forms the foundation of the GUI.

---

## Adding Mods

Mods can be added to the list either by dragging `.txt` files onto the mod list
or by clicking the **Add Files** button which opens your system's file picker.
Each mod entry now has a checkbox allowing you to enable or disable it for the
next merge. When no mods are loaded, the list shows a helpful "Drag mods here" hint.

### Importing Mod Profiles

Existing `smallf.dat` files can be imported as mod profiles using the **Import
Profile** button. Choose a folder containing a `smallf.dat` and it will appear
in the profile list using the folder name.
Each profile folder contains a small `profile.json` file with metadata such as
which game it belongs to. The manager uses this information when listing and
loading profiles.

---

## Xbox 360 ISO Extraction

extract-xiso now comes with FA Mod Manager. Select an ISO and extraction
folder from the **Settings** menu and click **Extract ISO** to unpack the game.
The contents are placed inside a folder named after the ISO within the chosen
directory. By default this directory is `xbox_extract` next to the program.
The paths you choose are saved back to `fa_mod_manager_config.json` under
`xbox_iso` and `extract_root` so the manager remembers them next time.

---

## Planned Features

- Native Linux compatibility (in progress)
- Expanded mod metadata and compatibility checks
- Additional unpacking and repacking tools for other platforms
- Custom music
- Editable variables for each mod

---

## License

- See [LICENSE.TXT](exiso/LICENSE.TXT) for details about extract-xiso and other included third-party code.
- All original code in this repository is released under the MIT License unless otherwise noted.

---

**For questions, issues, or contributions, please open an issue or PR on GitHub.**
