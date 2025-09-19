from pydantic import BaseModel
from typing import List

class Lesson(BaseModel):
    lesson: str
    topic: str

class Module:
    module_id: int
    name: str
    lessons: List[Lesson]

class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]