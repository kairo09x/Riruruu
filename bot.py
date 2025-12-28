# bot.py (Root Directory)
import asyncio
from pyrogram import idle
from anony import (app, userbot, anon, db, logger, stop, yt, config)
from anony.plugins import all_modules
import importlib

async def start_bot():
    print("--- Starting Bot ---")
    
    # 1. Database connect karein
    await db.connect()
    
    # 2. Main Bot, Userbot aur Calls ko boot karein
    await app.boot()
    await userbot.boot()
    await anon.boot()

    # 3. Saare plugins load karein
    for module in all_modules:
        importlib.import_module(f"anony.plugins.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    # 4. Sudo users update karein
    sudoers = await db.get_sudoers()
    app.sudoers.update(sudoers)
    
    print("--- Bot is Online ---")
    await idle()
    await stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        pass
