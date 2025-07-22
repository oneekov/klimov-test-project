from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel, validator, EmailStr, field_validator

# Определим enum для sex
class SexEnum(str, Enum):
    male = "male"
    female = "female"

# Pydantic модель для валидации входных данных
class UserInput(BaseModel):
    username: str
    password: str
    school: Optional[str] = None
    grade: list[Union[int, str]]
    full_name: list[str]
    email: Optional[EmailStr] = None
    number: Optional[str] = None

    @validator('username')
    def validate_username(cls, v):
        if len(v) > 32:
            raise ValueError('bad username provided (max 32 characters)')
        return v

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('bad password provided (min 8 characters)')
        return v

    @validator('grade')
    def validate_grade(cls, v):
        if len(v) != 2:
            raise ValueError('bad grade format, correct [grade_number, grade_letter]')
        grade_number, grade_letter = v
        if not isinstance(grade_number, int) or grade_number < 1 or grade_number > 11:
            raise ValueError('bad grade number provided (1-11)')
        if not isinstance(grade_letter, str) or len(grade_letter) != 1:
            raise ValueError('bad grade letter provided (correct: single character)')
        return v

    @validator('full_name')
    def validate_full_name(cls, v):
        if len(v) != 3:
            raise ValueError('wrong full name format, correct [surname, name, patronymic]')
        for part in v:
            if len(part) > 40:
                raise ValueError('length overflow (max 40) in full name part')
        return v

    @validator('number')
    def validate_number(cls, v):
        if v is None:
            return v
        # Пример валидации формата номера: +79871234567
        if not v.startswith('+7') or not v[1:].isdigit() or len(v) != 12:
            raise ValueError('bad number format (correct +7XXXXXXXXXX)')
        return v
