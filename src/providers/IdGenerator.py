from uuid import uuid4


class IdGenerator:
    @staticmethod
    def generate() -> str:
        return uuid4()