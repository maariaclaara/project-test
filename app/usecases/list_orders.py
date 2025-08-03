class ListOrdersUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, filters: dict, skip: int, limit: int):
        return await self.repo.list(filters, skip, limit)
