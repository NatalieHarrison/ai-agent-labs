from pydantic import BaseModel
import json
from dotenv import load_dotenv
from datetime import datetime

class Date(BaseModel):
    date: datetime

    @classmethod
    def get(cls):
        return cls(date=datetime.now())