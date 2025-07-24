# agents.md

# Project Overview

**Name:** Full Auto Mod Manager  
**Purpose:**  
A desktop GUI tool for managing, merging, and applying mods to Full Auto (Xbox 360) and Full Auto 2: Battlelines (PS3).  
**Core Goals:**  
- Help users easily patch/restore game data (`smallf.dat`) with modded content
- Enable mod profiles and mod merging
- User-friendly setup, backup, and restoration
- Modular design for future game/format support

---

## Main Features

- **Game Directory Selection:** User-friendly way to point to their Full Auto game folder.
- **`smallf.dat` Detection:** Locates and manages the main game data file for mods.
- **Mod Profiles:** Save/load different sets of mods.
- **Mod Merging:** (WIP) Combine multiple mods into a single `smallf.dat`.
- **Backup/Restore:** Automatically back up original files before changes.

---

## Main Files & Structure

- **`mod_manager.py`**  
  Main GUI application. Handles all user interactions and controls backend logic.

- **`mod_manager_backend.py`**  
  Handles file operations, merging logic, and low-level mod management.

- **`fa_mod_manager_config.json`**  
  Stores user/game configuration, such as selected folders or mod profile info.

- **`smallf/`**  
  Directory for base data files and/or example mod data.

---

## Typical Usage

1. **Run** `mod_manager.py` with Python 3.x and Tkinter installed.
2. Use the **Settings** button to select the root game folder (e.g., `Full Auto 2 - Battlelines (Europe)`).
3. The tool finds `smallf.dat` at `PS3_GAME/USRDIR/smallf.dat`.
4. Create or choose a mod profile, select mods, and click **Merge** to apply.
5. Restore original file easily if needed.

---

## Data Structures / API

- **Configuration:**  
  Stores paths and mod profile info in JSON format:
  ```json
  {
    "Full Auto 2: Battlelines (PS3)": "C:/Games/Full Auto 2 - Battlelines (Europe)"
  }
