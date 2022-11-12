from dataclasses import dataclass

from share.base.entity import Entity


@dataclass
class ChoiceEntity(Entity):
    choice_text: str
    votes: int
    question_id: int

    def vote(self):
        self.votes += 1
