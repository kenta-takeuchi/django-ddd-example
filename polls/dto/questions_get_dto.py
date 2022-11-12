from dataclasses import dataclass

from typing import List


@dataclass(frozen=True)
class QuestionDto:
    id: int
    question_text: str
    pub_date: str


@dataclass(frozen=True)
class QuestionsGetDto:
    questions: List[QuestionDto]
