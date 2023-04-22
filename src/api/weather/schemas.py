from datetime import datetime

from pydantic import BaseModel, validator


class CityCoord(BaseModel):
    lon: float
    lat: float


class WeatherDescriptions(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class WeatherTemperature(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class WeatherWind(BaseModel):
    speed: float
    deg: int


class WeatherClouds(BaseModel):
    all: int


class WeatherSys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

    @validator("sunrise", "sunset")
    def convert_timestamp(cls, v):
        return datetime.fromtimestamp(v).strftime("%H:%M")


class WeatherSchema(BaseModel):
    coord: CityCoord
    weather: list[WeatherDescriptions]
    base: str
    main: WeatherTemperature
    visibility: int
    wind: WeatherWind
    clouds: WeatherClouds
    dt: int
    sys: WeatherSys
    timezone: int
    id: int
    name: str
    cod: int



