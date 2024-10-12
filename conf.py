import os

import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from telebot.async_telebot import AsyncTeleBot

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELE_TOKEN")
bot = AsyncTeleBot(TELEGRAM_TOKEN)

conn = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
)

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost/{os.getenv('DB_NAME')}",
    isolation_level="SERIALIZABLE",
)

