import httpx

from root import settings


async def get_cities():
    url = settings.base_url + 'company/region/'
    response = httpx.get(url)
    return response.json()
