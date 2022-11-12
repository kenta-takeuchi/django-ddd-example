from django.utils import timezone

from polls.entities.question_entity import QuestionEntity


class QuestionFactory:
    @classmethod
    def build(cls, question_text: str) -> QuestionEntity:
        return QuestionEntity(question_text, str(timezone.now()), [])
