from rest_framework.views import APIView
from rest_framework.response import Response

from polls.query_services.question_query_service import QuestionQueryService
from polls.use_cases.question_use_case import QuestionUseCase


class QuestionsView(APIView):
    def get(self, _):
        questions_get_dto = QuestionQueryService.get_latest_questions()
        return Response(questions_get_dto.as_dict(), status=200)

    def post(self, request):
        question_entity = QuestionUseCase.create_question(request.data['question_text'])
        return Response(question_entity.as_dict(), status=200)


class QuestionsDetailView(APIView):
    def get(self, _, question_id):
        question_entity = QuestionUseCase.get_by_id(question_id)
        return Response(question_entity.as_dict(), status=200)
