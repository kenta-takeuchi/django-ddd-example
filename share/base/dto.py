from dataclasses import asdict, dataclass


@dataclass
class Dto:
    def as_dict(self):
        return asdict(self)
