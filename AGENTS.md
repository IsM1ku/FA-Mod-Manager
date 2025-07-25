# AGENTS.md

# Project Overview

**Name:** Full Auto Mod Manager  
**Author:** IsM1ku  
**Purpose:**  
A desktop GUI tool for managing, merging, and applying mods to Full Auto (Xbox 360) and Full Auto 2: Battlelines (PS3).  
**Core Goals:**  
- Help users easily patch/restore game data (`smallf.dat` / `smallF.dat`) with modded content  
- Support mod profiles and intelligent mod merging  
- User-friendly setup, backup, and restoration  
- Modular design for future game/format support  
- **Goal:** Add **native Linux compatibility** and support for cross-platform unpacking/repacking.

---

## Main Features

- **Cross-Platform Game Support:**  
  - **Full Auto 2 (PS3):** Modifies `smallf.dat` in the game directory or backup.
  - **Full Auto (Xbox 360):** Supports direct folder editing (for Xenia, Aurora, XeXMenu) and ISO extraction (for ISOs, via bundled extract-xiso).
- **Game Directory/ISO Selection:** Easily select your Full Auto folder or Xbox 360 ISO.
- **Mod Profiles:** Organize, save, and switch between different modded builds.
- **Mod Merging:** Combine multiple mods with configurable order and conflict resolution.
- **Backup/Restore:** Automatic backup of original files, easy restoration.
- **Settings UI:** Configure game paths, ISO location, extraction folder, logging, and experimental features.
- **Drag-and-Drop Mod Loading:** Add mods by dragging `.txt` files into the GUI.
- **Import Existing Profiles:** Import `smallf.dat`/`smallF.dat` as reusable mod profiles.

---

## Main Files & Structure

- **`mod_manager.py`**  
  Main GUI application. Manages user interaction and frontend logic.

- **`mod_manager_backend.py`**  
  Backend for file operations, mod logic, and low-level patching.

- **`fa_mod_manager_config.json`**  
  User-generated config (created at first launch, or when missing) storing game paths, ISO locations, and settings.

- **`fa_mod_manager_config.example.json`**  
  Template config shipped with the app.

- **`bundled/`**  
  Bundled inside the .exe by PyInstaller; contains essential tools and scripts:
  - **`bundled/tools/`**:  
    - Unpacker/repacker binaries for smallf.dat, with **source code included in the repo** for both Windows and Linux.
    - **Both Windows and Linux versions of extract-xiso (exiso)** are included to support ISO extraction across platforms.

- **Other directories** (such as `smallf/`, `mod_profiles/`, `exiso/`, `xbox_extract/`)  
  Are always external—these stay next to the exe for user patching, mod development, or ISO extraction.

---

## Typical Usage

1. **Launch** `mod_manager.py` (or the packaged `.exe`).
2. Use **Settings** to choose your game folder, ISO, and extraction root.
3. For Xbox 360 ISOs, click **Extract ISO** (works on both Windows and Linux thanks to bundled binaries).
4. Add mods by drag-and-drop or using the Add button.
5. Select/arrange mod profiles and click **Merge** to build your custom `smallf.dat`/`smallF.dat`.
6. Use **Export** to deploy your modded file into the game directory or extracted folder.
7. Restore original files at any time.

---

## Xbox 360 ISO/FOLDER Workflow

- **ISO extraction** uses [extract-xiso](https://github.com/XboxDev/extract-xiso) to unpack the game.  
- **For emulators (Xenia) or modded consoles (Aurora/XeXMenu)**, the game can be played directly from the extracted folder.
- **Modding process** is identical for both PS3 and Xbox 360:  
  1. Extract ISO to folder (if needed)  
  2. Patch/merge with desired mods  
  3. Export patched `smallF.dat` to the appropriate location

---

## Mod File Format and Patching Specification

### Mod File Overview

Mods are defined as simple `.txt` files:

- **Metadata:** `name`, `author`, `description`
- **Patch instructions:** Each `[FILE ...]` block targets a specific file (e.g., `.psc` or `.txt`), a section (anchor), and supplies edit lines.
- **Insertion Syntax:**  
  - `;` prefix: replace existing line or append if not found  
  - `.;` prefix: insert immediately after section header

**Example Mod:**
```
# name:OP MGs and Debug Cam
# author:IsM1ku
# description:Makes the Machine Guns and Shotgun hilariously OP and removes the air stabilizer for more "realistic" in air gameplay, it also enables the debug freecam for FA2, this mod was made to test Full Auto Mod Manager during development.
# game:fa,fa2
[FILE MorphingWeaponSetup.psc]

sectionfa2:MorphingWeaponSetId "MachineGuns"
;MorphingWeaponSetData "firingRate = 100.0"
;MorphingWeaponSetData "projectileSpeed = 20000.0"

sectionfa2:MorphingWeaponSetId "ScatterGun"
;MorphingWeaponSetData "continuousFire = True"
;MorphingWeaponSetData "projectileSpeed = 20000.0"
;MorphingWeaponSetData "spreadAngleY = 0"
;MorphingWeaponSetData "projectileCount = 45"

sectionfa:MorphingWeaponSetId "MachineGuns0"
;MorphingWeaponSetData "projectileSpeed = 20000.0"
MorphingWeaponSetData "projectileMass = 20"

sectionfa:MorphingWeaponSetId "MachineGuns1"
;MorphingWeaponSetData "firingRate = 100.0"

sectionfa:MorphingWeaponSetId "MachineGuns2"
;MorphingWeaponSetData "firingRate = 200.0"

sectionfa:MorphingWeaponSetId "Shotgun0"
;MorphingWeaponSetData "projectileSpeed = 20000.0"
;MorphingWeaponSetData "spreadAngleY = 0"
;MorphingWeaponSetData "projectileCount = 45"

[FILE gameFA.psc]

sectionfa2://-----------POWERSLIDE, DRIVING AND STEERING--------------- 
;flipcorrectgain 0	//big air stabilizer.

sectionfa2:// Other debug stuff disabled by default
;isDeveloperBuild 1
;ShowComments 0
;ShowCamComments_Scale 0.0
;ShowCamComments_Opacity 0
;bind joy0_r3+joy0_l1 ShowComments 0
```

### Supported File Types

Both `.psc` and `.txt` are supported as plaintext.

---

## Transparency: In-File Comment Injection

- **Every edit includes a comment above it** noting the mod and author.
  - `.psc`: `// MODIFIED BY: ...`
  - `.txt`: `/* MODIFIED BY: ... */`
- If a line is replaced, the original can be commented out for full transparency:
  - `.psc`: `// ORIGINAL: ...`
  - `.txt`: `/* ORIGINAL: ... */`

---

## API / Data Structure Example

**fa_mod_manager_config.json:**
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