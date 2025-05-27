
import asyncio

def keep_alive():
    async def pulse():
        while True:
            await asyncio.sleep(60)
            print("✅ Bot is alive")
    asyncio.get_event_loop().create_task(pulse())
