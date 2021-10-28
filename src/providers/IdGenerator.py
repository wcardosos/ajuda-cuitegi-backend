from uuid import uuid4


class IdGenerator:
    @staticmethod
    def generate() -> str:
        id = str(uuid4())
        return id