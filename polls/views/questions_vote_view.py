from dataclasses import asdict

from rest_framework.views import APIView
from rest_framework.response import Response

from polls.use_cases.question_use_case import QuestionUseCase


class QuestionsVoteView(APIView):
    def post(self, request, question_id):
        choice_id = request.data['choice_id']
        question_entity = QuestionUseCase.vote(question_id, choice_id)
        return Response(asdict(question_entity), status=200)
