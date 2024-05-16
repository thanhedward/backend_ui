from typing import Optional, TypeVar, Generic
from pydantic.generics import GenericModel

from pydantic import BaseModel

T = TypeVar("T")


class ResponseSchemaBase(BaseModel):
    __abstract__ = True

    code: str = ''
    message: str = ''

    def custom_response(self, code: str, message: str):
        self.code = code
        self.message = message
        return self

    def success_response(self):
        self.code = '0'
        self.message = 'Successful'
        return self


class DataResponse(ResponseSchemaBase, GenericModel, Generic[T]):
    data: Optional[T] = None

    def custom_response(self, code: str, message: str, data: T):
        self.code = code
        self.message = message
        self.data = data
        return self

    def success_response(self, data: T):
        self.code = '0'
        self.message = 'Successful'
        self.data = data
        return self
