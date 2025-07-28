import os
import sys
import json
import shutil
import logging

# ----------- Setup paths relative to this script -----------
if getattr(sys, "frozen", False):
    APP_DIR = os.path.dirname(sys.executable)
    BUNDLED_DIR = os.path.join(sys._MEIPASS, "bundled")
else:
    APP_DIR = os.path.dirname(os.path.abspath(__file__))
    BUNDLED_DIR = os.path.join(APP_DIR, "bundled")

CONFIG_FILE = os.path.join(APP_DIR, "fa_mod_manager_config.json")
CONFIG_EXAMPLE = os.path.join(BUNDLED_DIR, "fa_mod_manager_config.example.json")
LOG_FILE = os.path.join(APP_DIR, "fa_mod_manager.log")

logger = logging.getLogger("fa_mod_manager")
logger.setLevel(logging.INFO)
LOGGING_ENABLED = False
COMMENTS_ENABLED = True


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def load_config():
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


def init_logger(enabled: bool):
    global LOGGING_ENABLED
    LOGGING_ENABLED = enabled
    logger.handlers.clear()
    if enabled:
        handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        logger.addHandler(handler)


def get_logging_enabled() -> bool:
    return LOGGING_ENABLED


def init_comments(enabled: bool):
    global COMMENTS_ENABLED
    COMMENTS_ENABLED = enabled


def get_comments_enabled() -> bool:
    return COMMENTS_ENABLED


def log(msg: str):
    print(msg)
    if LOGGING_ENABLED:
        logger.info(msg)


def save_game_paths(game_paths):
    data = load_config()
    data["game_paths"] = game_paths
    save_config(data)


def load_game_paths():
    return load_config().get("game_paths", {})
