from pydantic import BaseModel


class SettingsSchema(BaseModel):
    BOT_TOKEN: str
    WEATHER_API_KEY: str
