from dataclasses import dataclass
from typing import List

from share.base.dto import Dto


@dataclass
class QuestionDto(Dto):
    id: int
    question_text: str
    pub_date: str


@dataclass
class QuestionsGetDto(Dto):
    questions: List[QuestionDto]
