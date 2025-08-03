class CreateOrderUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, data: dict):
        return await self.repo.create(data)
