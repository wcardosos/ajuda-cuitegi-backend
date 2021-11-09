from .Address import Address
from .Helper import Helper

class Help:
    def __init__(
        self,
        id: str,
        address: Address,
        helper: Helper,
        description: str,
        image_url: str,
        active: bool
    ) -> None:
        self.id = id
        self.address = address
        self.helper = helper
        self.description = description
        self.image_url = image_url
        self.active = active