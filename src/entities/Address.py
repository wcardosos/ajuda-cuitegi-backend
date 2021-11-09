class Address:
    def __init__(
        self,
        id: str,
        street: str,
        neighborhood: str,
        number: int,
        complement: str
    ):
        self.id = id
        self.street = street
        self.neighborhood = neighborhood
        self.number = number
        self.complement = complement