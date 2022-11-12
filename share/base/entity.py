from dataclasses import asdict, dataclass, field
import uuid


@dataclass
class Entity:
    id: uuid.UUID = field(default_factory=lambda: globals()['Entity'].next_id(), kw_only=True)

    @classmethod
    def next_id(cls) -> uuid.uuid4:
        return uuid.uuid4()

    def as_dict(self):
        return asdict(self)
