import eoc
import asyncio

EBS = eoc.client('Your Token')


async def run():
    data = await EBS.getClass(dns='', class_name='', class_number='')
    print(data['data']['list'][-1])


asyncio.get_event_loop().run_until_complete(run())
