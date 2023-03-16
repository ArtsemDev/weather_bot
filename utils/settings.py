from pathlib import Path

from .schemas.settings import SettingsSchema


BASE_DIR = Path(__file__).resolve().parent.parent


def load_settings() -> SettingsSchema:
    from json import load
    with open(BASE_DIR.joinpath('settings.json'), 'r', encoding='utf-8') as file:
        return SettingsSchema(**load(file))


SETTINGS: SettingsSchema = load_settings()
