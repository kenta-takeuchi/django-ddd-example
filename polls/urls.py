from django.urls import path

from polls.views.questions_choices_view import QuestionsChoiceView
from polls.views.questions_view import QuestionsView, QuestionsDetailView
from polls.views.questions_vote_view import QuestionsVoteView

urlpatterns = [
    path('', QuestionsView.as_view()),
    path('<str:question_id>/', QuestionsDetailView.as_view()),
    path('<str:question_id>/vote/', QuestionsVoteView.as_view(), name='vote'),
    path('<str:question_id>/choices/', QuestionsChoiceView.as_view(), name='choices'),
]
