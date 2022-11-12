from rest_framework.views import APIView
from rest_framework.response import Response

from polls.use_cases.question_use_case import QuestionUseCase


class QuestionsChoiceView(APIView):
    def get(self, _, question_id):
        question_entity = QuestionUseCase.get_by_id(question_id)
        return Response([c.as_dict() for c in question_entity.choice_entities], status=200)

    def post(self, request, question_id):
        question_entity = QuestionUseCase.create_choice(question_id, request.data['choice_text'])
        return Response([c.as_dict() for c in question_entity.choice_entities], status=200)
