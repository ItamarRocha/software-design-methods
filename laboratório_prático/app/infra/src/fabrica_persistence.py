from ..src.user_persistence import UserPersistence

class FabricaPersistence:
    def criarPersistence(self, path):
        return UserPersistence(path)