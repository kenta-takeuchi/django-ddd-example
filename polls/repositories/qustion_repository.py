from polls.models import Choice, Question
from polls.entities.choice_entity import ChoiceEntity
from polls.entities.question_entity import QuestionEntity


class QuestionRepository:
    @classmethod
    def get_by_id(cls, question_id: str) -> QuestionEntity:
        question = Question.objects.prefetch_related('choice_set').get(pk=question_id)
        choice_entities = [
            ChoiceEntity(c.choice_text, c.votes, question.id, id=c.id) for c in question.choice_set.all()
        ]
        return QuestionEntity(question.question_text, question.pub_date, choice_entities, id=question.id)

    @classmethod
    def save(cls, question_entity: QuestionEntity) -> QuestionEntity:
        question, _ = Question.objects.get_or_create(pk=question_entity.id)
        question.question_text = question_entity.question_text
        question.pub_date = question_entity.pub_date
        question.save()

        for choice_entity in question_entity.choice_entities:
            choice, _ = Choice.objects.get_or_create(pk=choice_entity.id, question=question)
            choice.choice_text = choice_entity.choice_text
            choice.votes = choice_entity.votes
            choice.save()

        return question_entity
