import logging
from typing import Optional

import aiohttp

logger = logging.getLogger(__name__)


class BackendAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def register_user(
        self,
        telegram_id: int,
        username: Optional[str],
        first_name: str,
        last_name: Optional[str] = None,
    ):
        url = f"{self.base_url}/api/v1/auth/telegram"
        data = {
            "telegram_id": telegram_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Backend error: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Connection error: {e}")
            return None


# Создаем экземпляр API
backend_api = BackendAPI("http://localhost:8000")
