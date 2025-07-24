import os
import shutil
import subprocess
import json

# ----------- Setup paths relative to this script -----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SMALLF_DIR = os.path.join(BASE_DIR, "smallf")
TOOLS_DIR = os.path.join(SMALLF_DIR, "tools")
FINISHED_DIR = os.path.join(SMALLF_DIR, "finished")
BASE_FA_DIR = os.path.join(SMALLF_DIR, "base", "fa")
BASE_FA2_DIR = os.path.join(SMALLF_DIR, "base", "fa2")

UNPACKED_FA_DIR = os.path.join(SMALLF_DIR, "base", "fa_unpacked")
UNPACKED_FA2_DIR = os.path.join(SMALLF_DIR, "base", "fa2_unpacked")
TEMP_FA_DIR = os.path.join(SMALLF_DIR, "base", "fa_temp")
TEMP_FA2_DIR = os.path.join(SMALLF_DIR, "base", "fa2_temp")

CONFIG_FILE = os.path.join(BASE_DIR, "fa_mod_manager_config.json")

# ----------- Config: Save/load game paths (optional) -----------
def save_game_paths(game_paths):
    with open(CONFIG_FILE, "w") as f:
        json.dump(game_paths, f)

def load_game_paths():
    """Return saved game paths, creating an empty config if needed."""
    if not os.path.isfile(CONFIG_FILE):
        example = os.path.join(BASE_DIR, "fa_mod_manager_config.example.json")
        if os.path.isfile(example):
            shutil.copy2(example, CONFIG_FILE)
        else:
            with open(CONFIG_FILE, "w") as f:
                json.dump({}, f)
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

# ----------- Unpack and repack functions -----------
def _ensure_base_unpacked(game):
    """Unpack the original smallf.dat once and cache the result."""
    exe = os.path.join(TOOLS_DIR, "unpack_smallf_win.exe")
    if game == "fa2":
        input_smallf = os.path.join(BASE_FA2_DIR, "smallf.dat")
        unpack_dir = UNPACKED_FA2_DIR
    else:
        input_smallf = os.path.join(BASE_FA_DIR, "smallF.dat")
        unpack_dir = UNPACKED_FA_DIR

    if not os.path.isdir(unpack_dir):
        os.makedirs(unpack_dir, exist_ok=True)
        dat_copy = os.path.join(unpack_dir, os.path.basename(input_smallf))
        shutil.copy2(input_smallf, dat_copy)
        subprocess.check_call([exe, os.path.basename(dat_copy)], cwd=unpack_dir)
        os.remove(dat_copy)
        print(f"[OK] Cached base unpack to: {unpack_dir}")
    return unpack_dir


def unpack_smallf(game):
    """Prepare a temp folder with the unpacked smallf for the given game."""
    if game == "fa2":
        temp_dir = TEMP_FA2_DIR
    else:
        temp_dir = TEMP_FA_DIR

    unpack_dir = _ensure_base_unpacked(game)

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    shutil.copytree(unpack_dir, temp_dir)
    print(f"[OK] Prepared temp folder at {temp_dir}")
    return temp_dir

def repack_smallf(game, mod_name):
    """Repack the temp folder into ``finished/<mod_name>/smallf.dat``.

    The repacker expects a ``smallf`` folder in the same directory, so the
    unpacked data is copied into ``smallf/tools`` before running it without any
    command line arguments.
    """
    exe = os.path.join(TOOLS_DIR, "repack_smallf_win.exe")
    if game == "fa2":
        temp_dir = TEMP_FA2_DIR
    else:
        temp_dir = TEMP_FA_DIR

    # Prepare folder structure for the repacker
    working_smallf = os.path.join(TOOLS_DIR, "smallf")
    if os.path.exists(working_smallf):
        shutil.rmtree(working_smallf)
    shutil.copytree(temp_dir, working_smallf)

    # Run the repacker in the tools directory with no arguments
    subprocess.check_call([exe], cwd=TOOLS_DIR)

    # Determine repacker output file name
    candidate1 = os.path.join(TOOLS_DIR, "smallf_repack.dat")
    candidate2 = os.path.join(TOOLS_DIR, "smallf.dat")
    if os.path.isfile(candidate1):
        src = candidate1
    else:
        src = candidate2

    finished_subdir = os.path.join(FINISHED_DIR, mod_name)
    os.makedirs(finished_subdir, exist_ok=True)
    dest = os.path.join(finished_subdir, "smallf.dat")
    shutil.move(src, dest)

    # Clean up the working folder
    shutil.rmtree(working_smallf)

    print(f"[OK] Repacked smallf written to: {dest}")
    return dest

# ----------- Export to game folder -----------
def export_smallf_to_game(game, mod_name, game_root):
    """Copy the repacked smallf.dat into the given game's PS3 folder.

    The file is renamed to ``smallf_modified.dat`` so existing game files are
    left untouched. ``game`` should be either ``'fa'`` or ``'fa2'``.
    """
    finished_subdir = os.path.join(FINISHED_DIR, mod_name)

    src = os.path.join(finished_subdir, "smallf.dat")
    if not os.path.isfile(src):
        raise FileNotFoundError(f"Repacked file not found: {src}")

    dest_dir = os.path.join(game_root, "PS3_GAME", "USRDIR")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "smallf_modified.dat")
    shutil.copy2(src, dest)
    print(f"[OK] Exported modified smallf to: {dest}")

# ----------- Profile management -----------
def import_profile(game, profile_name, source_smallf):
    """Import an existing smallf.dat as a mod profile."""
    finished_subdir = os.path.join(FINISHED_DIR, profile_name)
    os.makedirs(finished_subdir, exist_ok=True)
    dest = os.path.join(finished_subdir, "smallf.dat")
    shutil.copy2(source_smallf, dest)
    print(f"[OK] Imported profile '{profile_name}' -> {dest}")
    return dest


def list_existing_profiles():
    """Return names of profiles already present in ``finished``."""
    if not os.path.isdir(FINISHED_DIR):
        return []
    names = []
    for name in os.listdir(FINISHED_DIR):
        if os.path.isfile(os.path.join(FINISHED_DIR, name, "smallf.dat")):
            names.append(name)
    return names

# ----------- Patch/merge logic placeholder -----------
def apply_mods_to_temp(game, mods):
    """
    Given a game ('fa' or 'fa2') and a list of mod objects,
    patch the relevant files in the temp folder.
    For now, this is just a placeholder!
    """
    if game == "fa2":
        temp_dir = TEMP_FA2_DIR
    else:
        temp_dir = TEMP_FA_DIR
    # For each mod, read patch instructions and modify files in temp_dir
    print(f"[INFO] Would now patch files in: {temp_dir} using {len(mods)} mod(s)")
    # ----> Insert section-replacement, merge, conflict detection, etc here

# ----------- Main example usage -----------
if __name__ == "__main__":
    # Example settings:
    selected_game = "fa2"   # or "fa"
    mod_name = "ExampleMod"

    # 1. Unpack
    temp_dir = unpack_smallf(selected_game)

    # 2. Apply mods (add your mod objects/list here!)
    apply_mods_to_temp(selected_game, mods=[])  # Insert real mods list!

    # 3. Repack
    output_smallf = repack_smallf(selected_game, mod_name)

    # 4. Export to the game folder if configured
    game_paths = load_game_paths()
    if selected_game == "fa2":
        key = "Full Auto 2: Battlelines (PS3)"
    else:
        key = "Full Auto (Xbox 360)"
    game_root = game_paths.get(key)
    if game_root:
        export_smallf_to_game(selected_game, mod_name, game_root)
    else:
        print("[WARN] Game path not configured; skipping export.")

    print("\n[Done] Workflow complete.")
    print(f"You can find your new smallf.dat here:\n  {output_smallf}")
