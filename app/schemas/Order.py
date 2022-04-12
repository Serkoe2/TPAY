from pydantic import BaseModel, EmailStr

class OrderCreate(BaseModel):
    """ Валидация запроса на оплату заказа """
    email: EmailStr
    amount: int

class OrderGet(BaseModel):
    """ Get заказов """
    offset: int
