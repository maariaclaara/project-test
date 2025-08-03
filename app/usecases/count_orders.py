class CountOrdersUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, filters: dict):
        return await self.repo.count(filters)
