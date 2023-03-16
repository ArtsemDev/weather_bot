from aiohttp import ClientSession


class NominatimAPI(object):
    BASE_URL: str = 'https://nominatim.openstreetmap.org'

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with ClientSession(base_url=NominatimAPI.BASE_URL) as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @classmethod
    @create_session
    async def _get(cls, url: str, session: ClientSession = None, **kwargs) -> dict | None:
        response = await session.get(url=url, params=kwargs)
        if response.status == 200:
            return await response.json()

    @classmethod
    async def search(cls, city: str) -> dict | None:
        return await cls._get(url='/search', city=city, format='json')
