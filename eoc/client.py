from eoc.error import EmptyArguments

import aiohttp
from typing import Union


class client:
    def __init__(self, token: str = None):
        if token is None:
            raise EmptyArguments('X-AUTH-TOKEN 값이 비어있습니다.')
        self.token = token

    async def getClass(self, dns: str, class_name: str, class_number: Union[str, int]):
        URL = f'https://{dns}.ebsoc.co.kr/lecture/api/v1/{class_name}/lesson/lecture/attend/list/{class_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(URL, headers={"X-AUTH-TOKEN": self.token}) as res:
                return await res.json()
