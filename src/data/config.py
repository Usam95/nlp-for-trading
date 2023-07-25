import json
from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError




class Config(BaseModel):
    tickers: List[str] = Field(..., title="List of tickers")
    start_date: str
    end_date: str
    
    @validator('start_date', 'end_date')
    def validate_date(cls, v):
        try:
            return datetime.strptime(v, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            

def load_config(path: str) -> Config:
    try:
        with open(path, 'r') as f:
            config_dict = json.load(f)
        return Config(**config_dict)
    except json.JSONDecodeError:
        print("Failed to decode configuration file.")
        return None
    except ValidationError as e:
        print(f"Validation error while loading config: {e}")
        return None