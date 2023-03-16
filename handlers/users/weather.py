from aiogram import Router, F
from aiogram.types import Message

from loader import weather
from utils.nominatim import NominatimAPI

weather_router = Router()


weather_emoji = {
    'clouds': '☁️',
    'sun': '☀',
    'rain': '🌧',
    'snow': '❄',
    'clear': '☀',
}


@weather_router.message(F.content_type == 'text')
async def get_weather_by_city_name(message: Message):
    await message.delete()
    data = await NominatimAPI.search(city=message.text)
    if data:
        weather_data = await weather.current_weather(
            lat=data[0]['lat'],
            lon=data[0]['lon'],
        )
        if weather_data:
            print(weather_data)
            emoji = weather_emoji.get(weather_data.get('weather')[0].get('main').lower())
            await message.answer(text=emoji)
            await message.answer(
                text=f'''
***ПОГОДА В ГОРОДЕ {data[0].get('display_name').upper()}***

***{weather_data.get('weather')[0].get('description').upper()}***
__Температура:__ ***{weather_data.get("main").get("temp")}***
__Ощущается как:__ ***{weather_data.get("main").get("feels_like")}***
'''
            )
        else:
            await message.answer(
                text='Не смогли определить город!'
            )
    else:
        await message.answer(
            text='***Определение погоды по реопозиции временно не доступно!***'
        )


@weather_router.message(F.content_type == 'location')
async def get_weather_by_user_location(message: Message):
    await message.delete()
    weather_data = await weather.current_weather(lat=message.location.latitude, lon=message.location.longitude)
    if weather_data:
        emoji = weather_emoji.get(weather_data.get('weather')[0].get('main').lower())
        await message.answer(text=emoji)
        await message.answer(
            text=f'''
***ПОГОДА В ГОРОДЕ {weather_data.get('name').upper()}***

***{weather_data.get('weather')[0].get('description').upper()}***
__Температура:__ ***{weather_data.get("main").get("temp")}***
__Ощущается как:__ ***{weather_data.get("main").get("feels_like")}***
'''
        )
    else:
        await message.answer(
            text='***Определение погоды по реопозиции временно не доступно!***'
        )
