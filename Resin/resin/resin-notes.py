import asyncio
import genshin
from datetime import datetime, timedelta
from sys import platform

async def main():
    client = client = genshin.Client({"ltuid":"XXX", "ltoken":"XXX"})

    notes = await client.get_notes(XXX) #UID HERE
        
    # output
    print(f"Current resin: {notes.current_resin}/{notes.max_resin}")
    
if platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
