class GetOrderDetailUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, order_id: str):
        return await self.repo.get(order_id)
