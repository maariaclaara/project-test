from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

class AbstractOrderRepository(ABC):
    @abstractmethod
    async def create(self, data: dict): pass

    @abstractmethod
    async def list(self, filters: dict, skip: int, limit: int) -> List[dict]: pass

    @abstractmethod
    async def count(self, filters: dict) -> int: pass

    @abstractmethod
    async def get(self, order_id: str) -> Optional[dict]: pass

    @abstractmethod
    async def delete(self, order_id: str): pass
