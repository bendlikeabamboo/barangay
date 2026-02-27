import os
import pytest
from pathlib import Path

from barangay.config import load_env_config, get_verbose, get_cache_dir


class TestLoadEnvConfig:
    @pytest.fixture(autouse=True)
    def clear_env(self, monkeypatch):
        monkeypatch.delenv("BARANGAY_AS_OF", raising=False)
        monkeypatch.delenv("BARANGAY_VERBOSE", raising=False)
        monkeypatch.delenv("BARANGAY_CACHE_DIR", raising=False)

    def test_load_env_config_defaults(self):
        config = load_env_config()
        assert config["BARANGAY_AS_OF"] is None
        assert config["BARANGAY_VERBOSE"] == "true"
        assert config["BARANGAY_CACHE_DIR"] is None

    def test_load_env_config_with_as_of(self, monkeypatch):
        monkeypatch.setenv("BARANGAY_AS_OF", "2025-01-01")
        config = load_env_config()
        assert config["BARANGAY_AS_OF"] == "2025-01-01"

    def test_load_env_config_with_verbose_true(self, monkeypatch):
        monkeypatch.setenv("BARANGAY_VERBOSE", "true")
        config = load_env_config()
        assert config["BARANGAY_VERBOSE"] == "true"

    def test_load_env_config_with_verbose_false(self, monkeypatch):
        monkeypatch.setenv("BARANGAY_VERBOSE", "false")
        config = load_env_config()
        assert config["BARANGAY_VERBOSE"] == "false"

    def test_load_env_config_with_cache_dir(self, monkeypatch):
        monkeypatch.setenv("BARANGAY_CACHE_DIR", "/tmp/cache")
        config = load_env_config()
        assert config["BARANGAY_CACHE_DIR"] == "/tmp/cache"

    def test_load_env_config_all_vars(self, monkeypatch):
        monkeypatch.setenv("BARANGAY_AS_OF", "2025-01-01")
        monkeypatch.setenv("BARANGAY_VERBOSE", "false")
        monkeypatch.setenv("BARANGAY_CACHE_DIR", "/custom/cache")
        config = load_env_config()
        assert config["BARANGAY_AS_OF"] == "2025-01-01"
        assert config["BARANGAY_VERBOSE"] == "false"
        assert config["BARANGAY_CACHE_DIR"] == "/custom/cache"


class TestGetVerbose:
    @pytest.fixture(autouse=True)
    def clear_env(self, monkeypatch):
        monkeypatch.delenv("BARANGAY_VERBOSE", raising=False)

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("true", True),
            ("True", True),
            ("TRUE", True),
            ("1", True),
            ("yes", True),
            ("Yes", True),
            ("YES", True),
            ("on", True),
            ("On", True),
            ("ON", True),
        ],
    )
    def test_get_verbose_true_values(self, monkeypatch, value, expected):
        monkeypatch.setenv("BARANGAY_VERBOSE", value)
        assert get_verbose() is expected

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("false", False),
            ("False", False),
            ("FALSE", False),
            ("0", False),
            ("no", False),
            ("No", False),
            ("NO", False),
            ("off", False),
            ("Off", False),
            ("OFF", False),
            ("", False),
            ("invalid", False),
            ("2", False),
        ],
    )
    def test_get_verbose_false_values(self, monkeypatch, value, expected):
        monkeypatch.setenv("BARANGAY_VERBOSE", value)
        assert get_verbose() is expected

    def test_get_verbose_default(self, monkeypatch):
        monkeypatch.delenv("BARANGAY_VERBOSE", raising=False)
        assert get_verbose() is True


class TestGetCacheDir:
    @pytest.fixture(autouse=True)
    def clear_env(self, monkeypatch):
        monkeypatch.delenv("BARANGAY_CACHE_DIR", raising=False)
        monkeypatch.delenv("LOCALAPPDATA", raising=False)
        monkeypatch.delenv("XDG_CACHE_HOME", raising=False)

    def test_get_cache_dir_from_env(self, monkeypatch):
        monkeypatch.setenv("BARANGAY_CACHE_DIR", "/custom/cache")
        cache_dir = get_cache_dir()
        assert cache_dir == Path("/custom/cache")

    def test_get_cache_dir_default_linux(self, monkeypatch):
        if os.name == "nt":
            pytest.skip("Windows-specific test")
        monkeypatch.delenv("BARANGAY_CACHE_DIR", raising=False)
        monkeypatch.delenv("XDG_CACHE_HOME", raising=False)
        cache_dir = get_cache_dir()
        assert cache_dir == Path.home() / ".cache" / "barangay"

    def test_get_cache_dir_with_xdg_cache_home(self, monkeypatch):
        if os.name == "nt":
            pytest.skip("Windows-specific test")
        monkeypatch.delenv("BARANGAY_CACHE_DIR", raising=False)
        monkeypatch.setenv("XDG_CACHE_HOME", "/tmp/xdg_cache")
        cache_dir = get_cache_dir()
        assert cache_dir == Path("/tmp/xdg_cache") / "barangay"

    @pytest.mark.skipif(os.name != "nt", reason="Windows-only test")
    def test_get_cache_dir_windows_localappdata(self, monkeypatch):
        monkeypatch.delenv("BARANGAY_CACHE_DIR", raising=False)
        monkeypatch.setenv("LOCALAPPDATA", "C:\\Users\\test\\AppData\\Local")
        cache_dir = get_cache_dir()
        assert (
            cache_dir == Path("C:\\Users\\test\\AppData\\Local") / "barangay" / "cache"
        )

    @pytest.mark.skipif(os.name != "nt", reason="Windows-only test")
    def test_get_cache_dir_windows_xdg_fallback(self, monkeypatch):
        monkeypatch.delenv("BARANGAY_CACHE_DIR", raising=False)
        monkeypatch.delenv("LOCALAPPDATA", raising=False)
        cache_dir = get_cache_dir()
        assert cache_dir == Path.home() / ".cache" / "barangay"

    @pytest.mark.skipif(os.name == "nt", reason="Non-Windows test")
    def test_get_cache_dir_linux_xdg_priority(self, monkeypatch):
        monkeypatch.delenv("BARANGAY_CACHE_DIR", raising=False)
        monkeypatch.setenv("XDG_CACHE_HOME", "/tmp/xdg_cache")
        cache_dir = get_cache_dir()
        assert cache_dir == Path("/tmp/xdg_cache") / "barangay"

    def test_get_cache_dir_path_object(self, monkeypatch):
        monkeypatch.setenv("BARANGAY_CACHE_DIR", "/custom/cache")
        cache_dir = get_cache_dir()
        assert isinstance(cache_dir, Path)
