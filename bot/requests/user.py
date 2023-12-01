import httpx

from root import settings


async def get_or_create_user(data: dict):
    url = settings.base_url + 'user/user/'
    response = httpx.post(url, data=data)
    return response.json()
