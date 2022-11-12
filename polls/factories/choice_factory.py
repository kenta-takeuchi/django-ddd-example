from polls.entities.choice_entity import ChoiceEntity


class ChoiceFactory:
    @classmethod
    def build(cls, question_id, choice_text: str) -> ChoiceEntity:
        return ChoiceEntity(choice_text, 0, question_id)
