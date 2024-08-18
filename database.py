from motor.motor_asyncio import AsyncIOMotorClient # type: ignore

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.calendar_db
calendar_collection = database.get_collection("calendar")
