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
TEMP_FA_DIR = os.path.join(SMALLF_DIR, "base", "fa_temp")
TEMP_FA2_DIR = os.path.join(SMALLF_DIR, "base", "fa2_temp")

CONFIG_FILE = os.path.join(BASE_DIR, "fa_mod_manager_config.json")

# ----------- Config: Save/load game paths (optional) -----------
def save_game_paths(game_paths):
    with open(CONFIG_FILE, "w") as f:
        json.dump(game_paths, f)

def load_game_paths():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

# ----------- Unpack and repack functions -----------
def unpack_smallf(game):
    """Unpack smallf.dat for the given game ('fa' or 'fa2') into its temp folder."""
    exe = os.path.join(TOOLS_DIR, "unpack_smallf_win.exe")
    if game == "fa2":
        input_smallf = os.path.join(BASE_FA2_DIR, "smallf.dat")
        temp_dir = TEMP_FA2_DIR
    else:
        input_smallf = os.path.join(BASE_FA_DIR, "smallF.dat")
        temp_dir = TEMP_FA_DIR
    # Clean temp folder
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    # Most tools output to their own folder; set cwd to temp_dir just in case
    subprocess.check_call([exe, input_smallf], cwd=temp_dir)
    print(f"[OK] Unpacked {input_smallf} to {temp_dir}")
    return temp_dir

def repack_smallf(game, mod_name):
    """Repack the temp folder for the given game into finished/{game}/{mod_name}/smallf.dat."""
    exe = os.path.join(TOOLS_DIR, "repack_smallf_win.exe")
    if game == "fa2":
        temp_dir = TEMP_FA2_DIR
        finished_subdir = os.path.join(FINISHED_DIR, "fa2", mod_name)
    else:
        temp_dir = TEMP_FA_DIR
        finished_subdir = os.path.join(FINISHED_DIR, "fa", mod_name)
    subprocess.check_call([exe, temp_dir])
    # The repacker creates smallf_repack.dat in temp_dir
    src = os.path.join(temp_dir, "smallf_repack.dat")
    os.makedirs(finished_subdir, exist_ok=True)
    dest = os.path.join(finished_subdir, "smallf.dat")
    shutil.move(src, dest)
    print(f"[OK] Repacked smallf written to: {dest}")
    return dest

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

    print("\n[Done] Workflow complete.")
    print(f"You can find your new smallf.dat here:\n  {output_smallf}")
