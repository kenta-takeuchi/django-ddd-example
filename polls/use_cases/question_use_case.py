from polls.dto.questions_get_dto import QuestionsGetDto
from polls.entities.question_entity import QuestionEntity
from polls.factories.choice_factory import ChoiceFactory
from polls.factories.question_factory import QuestionFactory
from polls.repositories.qustion_repository import QuestionRepository
from polls.query_services.question_query_service import QuestionQueryService


class QuestionUseCase:
    @classmethod
    def get_by_id(cls, question_id: str) -> QuestionEntity:
        return QuestionRepository.get_by_id(question_id)

    @classmethod
    def get_latest_questions(cls) -> QuestionsGetDto:
        return QuestionQueryService.get_latest_questions()

    @classmethod
    def create_question(cls, question_text: str) -> QuestionEntity:
        question_entity = QuestionFactory.build(question_text)
        return QuestionRepository.save(question_entity)

    @classmethod
    def create_choice(cls, question_id: str, choice_text: str) -> QuestionEntity:
        question_entity = QuestionRepository.get_by_id(question_id)
        choice_entity = ChoiceFactory.build(question_id, choice_text)
        question_entity.add_choice(choice_entity)
        return QuestionRepository.save(question_entity)

    @classmethod
    def vote(cls, question_id: str, choice_id: str) -> QuestionEntity:
        question_entity = QuestionRepository.get_by_id(question_id)
        question_entity.vote(choice_id)
        return QuestionRepository.save(question_entity)
