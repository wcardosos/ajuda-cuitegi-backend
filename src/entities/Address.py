class Address:
    def __init__(
        self,
        id: str,
        street: str,
        neighborhood: str,
        complement: str,
        number: str,
    ):
        self.id = id
        self.street = street
        self.neighborhood = neighborhood
        self.complement = complement
        self.number = number