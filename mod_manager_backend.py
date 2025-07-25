import os
import sys
import shutil
import subprocess
import json
import logging

# ----------- Setup paths relative to this script -----------
if getattr(sys, "frozen", False):
    # Running from a PyInstaller bundle
    APP_DIR = os.path.dirname(sys.executable)
    BUNDLED_DIR = os.path.join(sys._MEIPASS, "bundled")
else:
    APP_DIR = os.path.dirname(os.path.abspath(__file__))
    BUNDLED_DIR = os.path.join(APP_DIR, "bundled")

SMALLF_DIR = os.path.join(APP_DIR, "smallf")
MOD_PROFILES_DIR = os.path.join(APP_DIR, "mod_profiles")
EXISO_DIR = os.path.join(APP_DIR, "exiso")
XBOX_EXTRACT_DIR = os.path.join(APP_DIR, "xbox_extract")

BUNDLED_TOOLS_DIR = os.path.join(BUNDLED_DIR, "tools")
LEGACY_TOOLS_DIR = os.path.join(SMALLF_DIR, "tools")
TOOLS_DIR = BUNDLED_TOOLS_DIR if os.path.isdir(BUNDLED_TOOLS_DIR) else LEGACY_TOOLS_DIR
BASE_FA_DIR = os.path.join(SMALLF_DIR, "fa")
BASE_FA2_DIR = os.path.join(SMALLF_DIR, "fa2")

UNPACKED_FA_DIR = os.path.join(SMALLF_DIR, "fa_unpacked")
UNPACKED_FA2_DIR = os.path.join(SMALLF_DIR, "fa2_unpacked")
TEMP_FA_DIR = os.path.join(SMALLF_DIR, "fa_temp")
TEMP_FA2_DIR = os.path.join(SMALLF_DIR, "fa2_temp")

CONFIG_FILE = os.path.join(APP_DIR, "fa_mod_manager_config.json")
CONFIG_EXAMPLE = os.path.join(BUNDLED_DIR, "fa_mod_manager_config.example.json")
LOG_FILE = os.path.join(APP_DIR, "fa_mod_manager.log")
EXISO_EXE = os.path.join(EXISO_DIR, "extract-xiso.exe")


def _profile_dir(game, name):
    """Return directory for a profile of the given game."""
    return os.path.join(MOD_PROFILES_DIR, game, name)


def get_profile_smallf(game, name):
    """Return path to the profile's ``smallf.dat`` using the correct case."""
    filename = "smallF.dat" if game == "fa" else "smallf.dat"
    return os.path.join(_profile_dir(game, name), filename)

logger = logging.getLogger("fa_mod_manager")
logger.setLevel(logging.INFO)
LOGGING_ENABLED = False
COMMENTS_ENABLED = True


# ----------- Config management -----------
def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def load_config():
    """Return config dictionary, creating a default one if needed."""
    if not os.path.isfile(CONFIG_FILE):
        if os.path.isfile(CONFIG_EXAMPLE):
            shutil.copy2(CONFIG_EXAMPLE, CONFIG_FILE)
        else:
            default = {
                "game_paths": {},
                "logging_enabled": False,
                "comments_enabled": True,
                "xbox_iso": "",
                "extract_root": "",
            }
            with open(CONFIG_FILE, "w") as f:
                json.dump(default, f)
    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
    except Exception:
        data = {}

    if "game_paths" not in data:
        # upgrade old format
        data = {"game_paths": data, "logging_enabled": False, "comments_enabled": True}
    if "logging_enabled" not in data:
        data["logging_enabled"] = False
    if "comments_enabled" not in data:
        data["comments_enabled"] = True
    if "xbox_iso" not in data:
        data["xbox_iso"] = ""
    if "extract_root" not in data:
        data["extract_root"] = ""
    return data


def init_logger(enabled):
    """Enable or disable file logging."""
    global LOGGING_ENABLED
    LOGGING_ENABLED = enabled
    logger.handlers.clear()
    if enabled:
        handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        logger.addHandler(handler)


def get_logging_enabled():
    return LOGGING_ENABLED


def init_comments(enabled):
    """Enable or disable summary comments."""
    global COMMENTS_ENABLED
    COMMENTS_ENABLED = enabled


def get_comments_enabled():
    return COMMENTS_ENABLED


def log(msg):
    print(msg)
    if LOGGING_ENABLED:
        logger.info(msg)


# Backwards compatibility wrappers
def save_game_paths(game_paths):
    data = load_config()
    data["game_paths"] = game_paths
    save_config(data)


def load_game_paths():
    return load_config().get("game_paths", {})


# ----------- Mod parsing and patching -----------
def _parse_mod_file(path):
    """Return metadata dict and ordered patch instructions from a mod file.

    Each patch entry contains ``file``, ``section``, ``data`` and ``game`` keys.
    ``game`` is ``"fa"`` for Xbox 360, ``"fa2"`` for PS3 or ``"both``" for
    universal sections.
    """
    patches = []
    metadata = {}
    current_file = None
    current_section = None
    current_game = "both"
    current_data = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                if ":" in stripped:
                    key, val = stripped[1:].split(":", 1)
                    metadata[key.strip().lower()] = val.strip()
                continue
            if line.startswith("[FILE") and line.endswith("]"):
                if current_file and current_section and current_data:
                    patches.append({
                        "file": current_file,
                        "section": current_section,
                        "data": current_data,
                        "game": current_game,
                    })
                    current_section = None
                    current_data = []
                    current_game = "both"
                current_file = line[5:-1].strip()
            elif stripped.startswith("sectionfa2:") or stripped.startswith("sectionfa:") or stripped.startswith("section:"):
                if current_file is None:
                    continue
                if current_section and current_data:
                    patches.append({
                        "file": current_file,
                        "section": current_section,
                        "data": current_data,
                        "game": current_game,
                    })
                    current_data = []
                if stripped.startswith("sectionfa2:"):
                    current_game = "fa2"
                    current_section = stripped[len("sectionfa2:"):].strip()
                elif stripped.startswith("sectionfa:"):
                    current_game = "fa"
                    current_section = stripped[len("sectionfa:"):].strip()
                else:
                    current_game = "both"
                    current_section = stripped[len("section:"):].strip()
            elif stripped.startswith(";") or stripped.startswith(".;"):
                if current_file and current_section:
                    after_header = stripped.startswith(".;")
                    content = stripped[2:].strip() if after_header else stripped[1:].strip()
                    current_data.append({"line": content, "after_header": after_header})
    if current_file and current_section and current_data:
        patches.append({
            "file": current_file,
            "section": current_section,
            "data": current_data,
            "game": current_game,
        })

    # Determine the next section marker for each patch within the same file
    for i, patch in enumerate(patches):
        patch["next_section"] = None
        for j in range(i + 1, len(patches)):
            if patches[j]["file"] == patch["file"]:
                patch["next_section"] = patches[j]["section"]
                break
    return metadata, patches


# Helper to compare lines ignoring values
def _extract_key(line):
    """Return a comparison key for a config line, ignoring values."""
    line = line.strip()
    if "=" in line:
        return line.split("=", 1)[0].strip()
    parts = line.split()
    if not parts:
        return line
    if parts[0] == "bind" and len(parts) >= 2:
        return f"{parts[0]} {parts[1]}"
    return parts[0]

def _apply_patch_to_file(target_path, section, data_lines, next_section=None):
    """Patch a single file in place and return list of modified line numbers."""
    with open(target_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()
    anchor = None
    for i, line in enumerate(lines):
        if section in line:
            anchor = i
            break
    if anchor is None:
        raise ValueError(f"Section '{section}' not found in {target_path}")

    # find end of section for appends
    section_end = len(lines)
    if next_section:
        for i in range(anchor + 1, len(lines)):
            if next_section in lines[i]:
                section_end = i
                break

    changed = []

    for item in data_lines:
        new_line = item["line"]
        if item.get("after_header"):
            insert_pos = anchor + 1
            lines.insert(insert_pos, new_line)
            changed.append(insert_pos + 1)
            anchor += 1
            section_end += 1
            continue

        key = _extract_key(new_line)
        replaced = False
        for j in range(anchor + 1, section_end):
            if _extract_key(lines[j].lstrip()) == key:
                lines[j] = new_line
                changed.append(j + 1)
                replaced = True
                break
        if not replaced:
            insert_pos = section_end
            lines.insert(insert_pos, new_line)
            changed.append(insert_pos + 1)
            section_end += 1


    with open(target_path, "w", encoding="utf-8", errors="ignore") as f:
        f.write("\n".join(lines) + "\n")
    log(f"[OK] Patched {os.path.basename(target_path)} section '{section}'")
    return changed

def _append_summary_comment(target_path, changed_lines, mod_name=None, author=None):
    """Append a summary comment listing changed lines for a mod."""
    if not COMMENTS_ENABLED or not changed_lines:
        return
    with open(target_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()
    if target_path.lower().endswith(".psc"):
        c_start, c_end = "// ", ""
    else:
        c_start, c_end = "/* ", " */"
    mod_desc = mod_name or ""
    if author:
        mod_desc = f"{mod_desc} by {author}" if mod_desc else f"by {author}"
    summary = f"{c_start}line(s): {','.join(str(n) for n in changed_lines)} modified by {mod_desc}{c_end}"
    lines.append(summary)
    with open(target_path, "w", encoding="utf-8", errors="ignore") as f:
        f.write('\n'.join(lines) + '\n')


# ----------- Unpack and repack functions -----------

def _find_smallf_dir(path):
    """Return the path to the ``smallf`` folder inside ``path`` regardless of case."""

    lower = os.path.join(path, "smallf")
    if os.path.isdir(lower):
        return lower
    for name in os.listdir(path):
        if name.lower() == "smallf":
            return os.path.join(path, name)
    return lower


def _normalize_smallf_dir(path):
    """Return the normalized path to the ``smallf`` folder inside ``path``.

    The unpacker may create a folder matching the source filename (e.g. ``smallF``).
    This helper attempts to rename it to a consistent lowercase form. If the
    rename fails for any reason the original directory is returned so callers can
    still access the files.
    """

    found = _find_smallf_dir(path)
    lower = os.path.join(path, "smallf")

    if found == lower:
        return lower
    if not os.path.isdir(found):
        return lower

    try:
        # Renaming only the case can fail on Windows, so use a temporary name
        # when needed to force the change.
        if os.path.abspath(found).lower() == os.path.abspath(lower).lower():
            temp = os.path.join(path, "__tmp_smallf__")
            os.rename(found, temp)
            os.rename(temp, lower)
        else:
            os.rename(found, lower)
        return lower
    except OSError:
        # If renaming fails, fall back to using the existing directory.
        return found

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
        log(f"[OK] Cached base unpack to: {unpack_dir}")
    _normalize_smallf_dir(unpack_dir)
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
    _normalize_smallf_dir(temp_dir)
    log(f"[OK] Prepared temp folder at {temp_dir}")
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
    # The temporary folder contains a subdirectory with the unpacked files.
    # Ensure the folder name is consistently lowercase for the repacker.
    source_dir = _normalize_smallf_dir(temp_dir)

    # Prepare folder structure for the repacker
    working_smallf = os.path.join(TOOLS_DIR, "smallf")
    if os.path.exists(working_smallf):
        shutil.rmtree(working_smallf)
    shutil.copytree(source_dir, working_smallf)

    # Run the repacker in the tools directory with no arguments
    subprocess.check_call([exe], cwd=TOOLS_DIR)

    # Determine repacker output file name
    candidate1 = os.path.join(TOOLS_DIR, "smallf_repack.dat")
    candidate2 = os.path.join(TOOLS_DIR, "smallf.dat")
    if os.path.isfile(candidate1):
        src = candidate1
    else:
        src = candidate2

    finished_subdir = _profile_dir(game, mod_name)
    os.makedirs(finished_subdir, exist_ok=True)
    dest = get_profile_smallf(game, mod_name)
    shutil.move(src, dest)

    # Clean up the working folder
    shutil.rmtree(working_smallf)

    log(f"[OK] Repacked smallf written to: {dest}")
    return dest

# ----------- Export to game folder -----------
def export_smallf_to_game(game, mod_name, game_root):
    """Copy the repacked smallf.dat into the given game's PS3 folder as
    ``smallf.dat``."""
    finished_subdir = _profile_dir(game, mod_name)

    src = get_profile_smallf(game, mod_name)
    if not os.path.isfile(src):
        raise FileNotFoundError(f"Repacked file not found: {src}")

    if game == "fa2":
        dest_dir = os.path.join(game_root, "PS3_GAME", "USRDIR")
        os.makedirs(dest_dir, exist_ok=True)
        filename = "smallf.dat"
    else:
        dest_dir = game_root
        filename = "smallF.dat"
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, filename)
    shutil.copy2(src, dest)
    log(f"[OK] Exported modified smallf to: {dest}")


def restore_original_smallf(game, game_root):
    """Restore the original smallf.dat for the given game."""
    if game == "fa2":
        src = os.path.join(BASE_FA2_DIR, "smallf.dat")
        dest_dir = os.path.join(game_root, "PS3_GAME", "USRDIR")
        filename = "smallf.dat"
    else:
        src = os.path.join(BASE_FA_DIR, "smallF.dat")
        dest_dir = game_root
        filename = "smallF.dat"
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, filename)
    shutil.copy2(src, dest)
    log(f"[OK] Restored original smallf to: {dest}")


def extract_xbox_iso(iso_path, dest=None):
    """Extract an Xbox 360 ISO using ``extract-xiso``.

    The ISO's contents are placed inside a folder named after the ISO file
    within ``dest``.  The previous implementation simply called the
    ``extract-xiso`` binary and surfaced a generic ``CalledProcessError`` when
    the command failed.  This made it hard for users to diagnose issues such as
    missing files or permission errors.  We now verify the ISO path and capture
    the tool's output so the raised exception contains useful information.
    """
    if dest is None:
        dest = XBOX_EXTRACT_DIR
    if not os.path.isfile(iso_path):
        raise FileNotFoundError(f"ISO not found: {iso_path}")

    iso_name = os.path.splitext(os.path.basename(iso_path))[0]
    # Always create a subfolder named after the ISO to avoid cluttering the
    # chosen directory. If the provided path already ends with the ISO name,
    # keep it as-is.
    if os.path.basename(os.path.normpath(dest)).lower() != iso_name.lower():
        dest = os.path.join(dest, iso_name)

    os.makedirs(dest, exist_ok=True)
    # extract-xiso expects the -d option before the ISO path, otherwise it
    # interprets "-d" as a filename. Pass arguments in the correct order.
    cmd = [EXISO_EXE, "-d", dest, iso_path]
    try:
        result = subprocess.run(
            cmd,
            cwd=EXISO_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        err_output = e.stderr.strip() or e.stdout.strip()
        raise RuntimeError(
            f"extract-xiso failed with code {e.returncode}: {err_output}"
        ) from e

    log(f"[OK] Extracted {os.path.basename(iso_path)} to: {dest}")
    return dest

# ----------- Profile management -----------
def import_profile(game, profile_name, source_smallf):
    """Import an existing smallf.dat as a mod profile."""
    finished_subdir = _profile_dir(game, profile_name)
    os.makedirs(finished_subdir, exist_ok=True)
    dest = get_profile_smallf(game, profile_name)
    shutil.copy2(source_smallf, dest)
    log(f"[OK] Imported profile '{profile_name}' -> {dest}")
    return dest


def rename_profile(game, old_name, new_name):
    """Rename a profile folder and return new path."""
    old_dir = _profile_dir(game, old_name)
    new_dir = _profile_dir(game, new_name)
    if not os.path.isdir(old_dir):
        raise FileNotFoundError(f"Profile not found: {old_name}")
    if os.path.isdir(new_dir):
        raise FileExistsError(f"Profile already exists: {new_name}")
    os.rename(old_dir, new_dir)
    return get_profile_smallf(game, new_name)


def list_existing_profiles():
    """Return list of (game, profile_name) tuples for existing profiles."""
    result = []
    for game in ("fa", "fa2"):
        gdir = os.path.join(MOD_PROFILES_DIR, game)
        if not os.path.isdir(gdir):
            continue
        for name in os.listdir(gdir):
            prof_dir = os.path.join(gdir, name)
            if any(
                os.path.isfile(os.path.join(prof_dir, fname))
                for fname in ("smallf.dat", "smallF.dat")
            ):
                result.append((game, name))
    return result


def delete_profile(game, name):
    """Remove a profile folder."""
    path = _profile_dir(game, name)
    if not os.path.isdir(path):
        raise FileNotFoundError(f"Profile not found: {name}")
    shutil.rmtree(path)
    log(f"[OK] Deleted profile '{name}'")

# ----------- Patch/merge logic placeholder -----------
def apply_mods_to_temp(game, mods, merge_name=None):
    """Apply a sequence of mod files to the temporary unpacked directory.

    Parameters
    ----------
    game : str
        Either ``"fa"`` or ``"fa2"``.
    mods : list[str]
        Paths to mod definition files.
    merge_name : str, optional
        Desired name for the merged profile. If given it will be referenced in
        informational log messages. Defaults to the name of the last mod in
        ``mods``.
    """
    if game == "fa2":
        temp_dir = TEMP_FA2_DIR
    else:
        temp_dir = TEMP_FA_DIR

    # Mods are applied inside the unpacked "smallf" directory. Ensure the name
    # is lowercase so patched file paths match consistently.
    target_root = _normalize_smallf_dir(temp_dir)

    for mod in mods:
        meta, patches = _parse_mod_file(mod)
        mod_name = meta.get("name", os.path.basename(mod))
        author = meta.get("author")
        pending = {}
        for p in patches:
            p_game = p.get("game", "both")
            if p_game != "both" and p_game != game:
                continue
            target = os.path.join(target_root, p["file"])
            if not os.path.isfile(target):
                err = f"Target file not found: {p['file']} in {mod}"
                log(f"[ERROR] {err}")
                raise FileNotFoundError(err)
            log(f"[INFO] Applying patch from {os.path.basename(mod)} -> {p['file']} section '{p['section']}'")
            try:
                changed = _apply_patch_to_file(target, p["section"], p["data"], p.get("next_section"))
                pending.setdefault(target, []).extend(changed)
                if p.get("next_section") is None:
                    _append_summary_comment(target, pending.pop(target, []), mod_name, author)
            except Exception as exc:
                log(f"[ERROR] Failed patch {p['file']} from {os.path.basename(mod)}: {exc}")
                raise
        for path, lines_list in pending.items():
            _append_summary_comment(path, lines_list, mod_name, author)
        log(f"[OK] Applied mod: {os.path.basename(mod)}")
    final_name = merge_name or mod_name
    log(f"\n[Done] Mods applied for '{final_name}'. Ready for repack.")
