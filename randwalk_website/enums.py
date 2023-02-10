from enum import Enum


class PublicationType(Enum):
    BOOK = "Book"
    JOURNAL = "Journal"
    PUBLICATION = "Publication"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
