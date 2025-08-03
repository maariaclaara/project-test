from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

client = AsyncIOMotorClient(config('MONGO_URL'))
db = client["pedidos_db"]
