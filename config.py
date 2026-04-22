import os

from faker import Faker

PATH=os.path.dirname(__file__)
BASE_URL ="https://manager-bbc.shoptnt.cn"
BASE_URL1="https://manager-bbc.shoptnt.cn/dashboard"

fk=Faker(locale="zh_CN")

NAME=fk.name()
PHONE=fk.phone_number()


if __name__ =="__main__":
    print(NAME,PHONE)