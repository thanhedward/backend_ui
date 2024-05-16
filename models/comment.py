from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel
from datetime import datetime

class Comment(Document):
    idDestination: int
    username: str
    body: str
    createDate: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "idDestination": "1",
                "username": "thanhtd",
                "body": "mê li luôn ạ, hội người thích ngắm hoàng hôn siêu thích điều này ạ",
                "createDate": datetime.now()
            }
        }
    
    class Settings:
        name="comments"