from pydantic import BaseModel, field_validator, model_validator
from typing import List

class Person(BaseModel):
    sex: str
    age: int
    full_name: List[str]

    @field_validator("sex")
    def validate_sex(cls, value):
        if value not in ("male", "female"):
            raise ValueError("wrong sex (no LGBTQ+)")
        return value

    @field_validator("age")
    def validate_age(cls, value):
        if not (0 <= value <= 120):
            raise ValueError("person is too young/old")
        return value

    @field_validator("full_name")
    def validate_full_name(cls, value):
        if len(value) != 3:
            raise ValueError("bad full name provided")
        for part in value:
            if not isinstance(part, str) or len(part) > 40:
                raise ValueError("bad full name provided")
        return value


class Results(BaseModel):
    nature: int
    tech: int
    human: int
    sign_system: int
    image: int

    @model_validator(mode="after")
    def validate_results_range(self):
        for field_name in self.model_fields:
            value = getattr(self, field_name)
            if not (-20 <= value <= 20):
                raise ValueError(f"bad results provided")
        return self


class Result(BaseModel):
    person: Person
    results: Results
