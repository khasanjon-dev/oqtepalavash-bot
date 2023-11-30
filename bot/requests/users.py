import httpx

from root import settings


async def get_user_or_create(telegram_id):
    url = settings.base_url + 'user/user/'
    data = {
        'telegram_id': telegram_id
    }
    response = httpx.post(url, data=data)
    return response
