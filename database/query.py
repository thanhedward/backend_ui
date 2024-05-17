from typing import List, Union

from beanie import PydanticObjectId
import pymongo

from models.comment import Comment


comment_collection = Comment

async def add_new_comment(new_comment: Comment) -> Comment:
    newCmt = await new_comment.create()
    return newCmt


async def find_comment_des(idDes: int) -> List[Comment]:
    comments_destination = await comment_collection.find({"idDestination": idDes}).sort("createDate", pymongo.DESCENDING).to_list()
    return comments_destination


async def retrieve_comments() -> List[Comment]:
    rewards = await comment_collection.all().to_list()
    return rewards

async def retrieve_single_comment(id: PydanticObjectId) -> Comment:
    reward = await comment_collection.get(id)
    if reward:
        return reward
    
async def count_single_destination(idDes: int) -> int:
    num_reward_by_type = await comment_collection.find({"idDestination": idDes}).count()
    return num_reward_by_type


