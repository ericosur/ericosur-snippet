#!/usr/bin/env python3
#coding: utf-8

'''
pydantic base model class
'''

from datetime import date
from pydantic import BaseModel
from loguru import logger

logd = logger.debug

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    ''' main '''
    return user_id

class User(BaseModel):
    ''' A Pydantic model '''
    id: int
    name: str
    joined: date

my_user: User = User(id=3, name="John Doe", joined="2018-07-19")
logd(my_user)

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)
logd(my_second_user)
