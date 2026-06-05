import logging
import os
from pathlib import Path
from typing import TypedDict

logger = logging.getLogger(__name__)

DEFAULT_VERBOSE = "true"
DEFAULT_CACHE_DIR = None

__all__ = [
    "DEFAULT_CACHE_DIR",
    "DEFAULT_VERBOSE",
    "EnvConfig",
    "get_cache_dir",
    "get_verbose",
    "load_env_config",
    "resolve_as_of",
]


class EnvConfig(TypedDict):
    BARANGAY_AS_OF: str | None
    BARANGAY_VERBOSE: str
    BARANGAY_CACHE_DIR: str | None


def load_env_config() -> EnvConfig:
    config: EnvConfig = {
        "BARANGAY_AS_OF": os.getenv("BARANGAY_AS_OF"),
        "BARANGAY_VERBOSE": os.getenv("BARANGAY_VERBOSE", DEFAULT_VERBOSE),
        "BARANGAY_CACHE_DIR": os.getenv("BARANGAY_CACHE_DIR", DEFAULT_CACHE_DIR),
    }
    return config


def resolve_as_of(as_of_param: str | None = None) -> str | None:
    if as_of_param is not None:
        return as_of_param

    try:
        import barangay

        if hasattr(barangay, "as_of") and barangay.as_of is not None:
            return barangay.as_of
    except ImportError:
        pass

    env_config = load_env_config()
    if env_config["BARANGAY_AS_OF"]:
        return env_config["BARANGAY_AS_OF"]

    return None


def get_verbose() -> bool:
    env_config = load_env_config()
    return env_config["BARANGAY_VERBOSE"].lower() in ("true", "1", "yes", "on")


def get_cache_dir() -> Path:
    env_config = load_env_config()

    if env_config["BARANGAY_CACHE_DIR"]:
        return Path(env_config["BARANGAY_CACHE_DIR"])

    if os.name == "nt":
        local_app_data = os.getenv("LOCALAPPDATA")
        if local_app_data:
            return Path(local_app_data) / "barangay" / "cache"

    xdg_cache_home = os.getenv("XDG_CACHE_HOME")
    if xdg_cache_home:
        return Path(xdg_cache_home) / "barangay"

    return Path.home() / ".cache" / "barangay"
