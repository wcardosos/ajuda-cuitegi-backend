class Help:
    def __init__(
        self,
        id: str,
        person_to_help_name: str,
        helper_name: str,
        description: str,
        contact: str,
        image_url: str,
        active: bool
    ) -> None:
        self.id = id
        self.person_to_help_name = person_to_help_name
        self.helper_name = helper_name
        self.description = description
        self.contact = contact
        self.image_url = image_url
        self.active = active