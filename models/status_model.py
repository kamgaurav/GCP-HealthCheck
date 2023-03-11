from typing import List
from pydantic import BaseModel
from datetime import datetime

class status(BaseModel):
    Service_Name: str
    Status_Impact: str
    Description: str
    Location: str
    Most_Recent_Update: str
    Begin: datetime
    End: datetime

class Status_Model(BaseModel):
    statusses: List[status]