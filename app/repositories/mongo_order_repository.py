from bson import ObjectId
from app.datasources.mongo import db
from app.repositories.abstract_order_repository import AbstractOrderRepository

class MongoOrderRepository(AbstractOrderRepository):
    async def create(self, data: dict):
        return await db.orders.insert_one(data)

    async def list(self, filters: dict, skip: int, limit: int):
        return await db.orders.find(filters).skip(skip).limit(limit).to_list(length=limit)

    async def count(self, filters: dict):
        return await db.orders.count_documents(filters)

    async def get(self, order_id: str):
        return await db.orders.find_one({"_id": ObjectId(order_id)})

    async def delete(self, order_id: str):
        return await db.orders.delete_one({"_id": ObjectId(order_id)})
