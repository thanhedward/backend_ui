from fastapi import APIRouter

from api import  get_comment, add_comment, api_delete
from api import add_comment

router = APIRouter()


router.include_router(get_comment.router, tags=["comment"], prefix="/get")

router.include_router(add_comment.router, tags=["user"], prefix="/post")

router.include_router(api_delete.router, tags = ["delete-comment"], prefix="/delete")