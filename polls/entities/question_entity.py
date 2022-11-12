from dataclasses import dataclass
from typing import List

from share.base.entity import Entity
from polls.entities.choice_entity import ChoiceEntity


@dataclass
class QuestionEntity(Entity):
    question_text: str
    pub_date: str
    choice_entities: List[ChoiceEntity]

    def vote(self, choice_id: str):
        choice_entity = self.get_choice_entity(choice_id)
        choice_entity.vote()

    def get_choice_entity(self, choice_id: str) -> ChoiceEntity:
        return next(filter(lambda c: str(c.id) == choice_id, self.choice_entities))

    def add_choice(self, choice_entity: ChoiceEntity):
        self.choice_entities.append(choice_entity)
