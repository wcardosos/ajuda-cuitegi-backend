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
        active: bool,
        created_at: str,
        updated_at: str = None
    ) -> None:
        self.id = id
        self.address = address
        self.helper = helper
        self.description = description
        self.image_url = image_url
        self.active = active
        self.created_at = created_at
        self.updated_at = updated_at