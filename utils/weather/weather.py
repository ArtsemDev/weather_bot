from aiohttp import ClientSession


class OpenWeatherMapAPI(object):
    BASE_URL: str = 'https://api.openweathermap.org'

    def __init__(self, token: str):
        self.__token = token

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with ClientSession(
                    base_url=OpenWeatherMapAPI.BASE_URL,
                    headers={
                        'Accept-Language': 'ru'
                    }
            ) as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    async def _get(self, url: str, session: ClientSession = None, **kwargs) -> dict | None:
        response = await session.get(url=url, params=kwargs | {'appid': self.__token, 'lang': 'ru'})
        if response.status == 200:
            return await response.json()

    async def current_weather(self, lat: float, lon: float) -> dict | None:
        return await self._get(url='/data/2.5/weather', lat=lat, lon=lon, units='metric')
