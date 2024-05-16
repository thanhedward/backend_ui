from fastapi import BackgroundTasks, APIRouter, Body, Request, Response, HTTPException, Query, Depends
import logging
from pydantic import EmailStr, BaseModel
from base.base_response import DataResponse
from database.query import *
from models.comment import *

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/get-all-comment", response_description="Comment retrieved", response_model=DataResponse[List])
async def get_all_reward():
    rewards = await retrieve_comments()
    return DataResponse().success_response(rewards)

@router.get("/get-destination-comment/{idDes}", response_description="Comment destination retrieved", response_model=DataResponse[List])
async def get_des_comments(idDes: int):
    logger.info("idDestinationnn", idDes)
    comments = await find_comment_des(idDes)
    return DataResponse().success_response(comments)

@router.get("/get-comment-by-id/{id}", response_model=Union[DataResponse[str], DataResponse[Comment]])
async def get_cmt_by_id(id: PydanticObjectId):
    comment = await retrieve_single_comment(id)
    if comment:
        return DataResponse().success_response(comment)
    return DataResponse().custom_response("1", "Failed", "Can not find ID in your request!")


@router.get("/count-comment-destination/{id}", response_model=DataResponse[int])
async def get_des_comments(idDes: int):
    num_comments = await count_single_destination(idDes)
    return DataResponse().success_response(num_comments)


