class DeleteOrderUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, order_id: str):
        return await self.repo.delete(order_id)
