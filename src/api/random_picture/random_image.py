import aiohttp

from src.config import CAT_API_KEY


class CatAPI:
    def __init__(self):
        self.base_url = "https://api.thecatapi.com/"

    async def get_image(self):
        params = {
            "api_key": CAT_API_KEY,
            "size": "med",
            "mime_types": "jpg,png",
            "format": "json",
            "limit": 1,
        }
        url = self._get_url("v1/images/search")
        async with aiohttp.ClientSession() as session:
            response = await session.get(url, params=params)
            try:
                data = await response.json()
                image_url = data[0]["url"]
                return image_url
            except:
                return None

    def _get_url(self, prefix: str):
        return self.base_url + prefix
