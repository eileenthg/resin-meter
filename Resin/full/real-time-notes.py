import asyncio
import genshin
from datetime import datetime, timedelta
from sys import platform

async def main():
    client = genshin.Client({"ltuid":"40357978", "ltoken":"4cxrpwPIsGOVHShPITi5t2rIumvNSLqUwRX26ocg"}) #Must log in with your own account in your web browser.

    notes = await client.get_notes(807040435) #UID HERE
    
    #print(notes) #only for debugging, if mhy changes the name again.
    
    # set current time
    ini_time_for_now = datetime.now()
    
    # resin stats
    resin_left_time = notes.remaining_resin_recovery_time
    resin_cap = ini_time_for_now + resin_left_time
    resin_hours, resin_minutes = divmod(resin_left_time.seconds // 60, 60)
    
    # realm currency stats
    realm_left_time = notes.remaining_realm_currency_recovery_time
    realm_cap = ini_time_for_now + realm_left_time
    realm_hours, realm_minutes = divmod(realm_left_time.seconds // 60, 60)
    
    # output
    print(f"Current resin: {notes.current_resin}/{notes.max_resin}")
    print(f"Resin full in {resin_hours:.0f} hours {resin_minutes:.0f} minutes at {resin_cap.strftime('%m/%d/%Y, %H:%M:%S')}")
    print(f"Comissions done: {notes.completed_commissions}/{notes.max_commissions}")
    print(f"Current realm currency: {notes.current_realm_currency}/{notes.max_realm_currency}")
    print(f"Realm currency full in {realm_hours:.0f} hours {realm_minutes:.0f} minutes at {realm_cap.strftime('%m/%d/%Y, %H:%M:%S')}")
    print(f"Expeditions finished: {sum(expedition.finished for expedition in notes.expeditions)}")

if platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
