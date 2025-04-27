from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

client = AsyncIOMotorClient(os.getenv('MONGODB_URL'))
db = client.get_database() 


#never show ur login|pass here 