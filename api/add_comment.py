from fastapi import BackgroundTasks, APIRouter, Body, Request, Response, HTTPException, Query, Depends
import logging
from pydantic import EmailStr, BaseModel
from base.base_response import DataResponse
from database.query import *
from models.comment import *
logger = logging.getLogger(__name__)

router = APIRouter()

class AddCommentDto(BaseModel):
    idDes: int
    username: str
    body: str

@router.post('/add-comment', response_model=DataResponse[Comment]) #If data response is a class, change str to class
async def add_comment_by_idDes(commentDto: AddCommentDto = Body(...)):
    logger.info("Adding comment")
    new_comment = Comment(
        username=commentDto.username,
        body=commentDto.body,
        idDestination=commentDto.idDes,
        createDate=datetime.now(),
    )

    try: 
        res_add_reward = await add_new_comment(new_comment)
        return DataResponse().success_response(res_add_reward)

    except Exception as e:
            return HTTPException(status_code=400, detail=str(e))



