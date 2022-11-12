from polls.dto.questions_get_dto import QuestionsGetDto, QuestionDto
from polls.models import Question


class QuestionQueryService:
    @classmethod
    def get_latest_questions(cls, limit: int = 5) -> QuestionsGetDto:
        latest_question_list = Question.objects.order_by('-pub_date')[:limit]
        question_list = [QuestionDto(q.id, q.question_text, q.pub_date) for q in latest_question_list]
        return QuestionsGetDto(question_list)
