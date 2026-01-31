# src/main.py
import asyncio
import os
from dotenv import load_dotenv

from telethon_bot.bot import TelethonBot
from adk_agent.agent import GoogleADKAgent

# Load environment variables from .env file
load_dotenv()

async def main():
    # --- Configuration ---
    # Attempt to load from environment variables first, then from settings.py
    api_id = os.getenv('TELEGRAM_API_ID')
    api_hash = os.getenv('TELEGRAM_API_HASH')
    google_project_id = os.getenv('GOOGLE_PROJECT_ID')
    google_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_PATH')

    if not api_id or not api_hash:
        print("Telegram API ID and Hash not found in environment variables. Checking config/settings.py...")
        try:
            from config.settings import TELEGRAM_API_ID, TELEGRAM_API_HASH
            api_id = TELEGRAM_API_ID
            api_hash = TELEGRAM_API_HASH
        except ImportError:
            print("Error: config/settings.py not found or TELEGRAM_API_ID/TELEGRAM_API_HASH not set.")
            return

    if not google_project_id:
        print("Google Project ID not found in environment variables. Checking config/settings.py...")
        try:
            from config.settings import GOOGLE_PROJECT_ID
            google_project_id = GOOGLE_PROJECT_ID
        except ImportError:
            print("Error: config/settings.py not found or GOOGLE_PROJECT_ID not set.")
            return

    if not google_credentials_path:
        print("Google Application Credentials Path not found in environment variables. Checking config/settings.py...")
        try:
            from config.settings import GOOGLE_APPLICATION_CREDENTIALS_PATH
            google_credentials_path = GOOGLE_APPLICATION_CREDENTIALS_PATH
        except ImportError:
            print("Error: config/settings.py not found or GOOGLE_APPLICATION_CREDENTIALS_PATH not set.")
            return

    if not api_id or not api_hash or not google_project_id or not google_credentials_path:
        print("Critical configuration missing. Please ensure TELEGRAM_API_ID, TELEGRAM_API_HASH, GOOGLE_PROJECT_ID, and GOOGLE_APPLICATION_CREDENTIALS_PATH are set in environment variables or config/settings.py")
        return

    # --- Initialize Components ---
    adk_agent = GoogleADKAgent()
    telethon_bot = TelethonBot(int(api_id), api_hash)

    # Connect bot to agent
    telethon_bot.set_agent(adk_agent)
    telethon_bot.register_message_handler()

    # --- Start Bot ---
    print("Starting bot...")
    try:
        await telethon_bot.start()
    except Exception as e:
        print(f"Error starting bot: {e}")
    finally:
        await telethon_bot.stop()

if __name__ == '__main__':
    asyncio.run(main())
