from app.db_config import database
from app.models.orders import orders_table
from datetime import datetime
from random import randint

class Order:
    last_orderId = 0
    prefix = "pretst_"

    @classmethod
    def newOrderId(cls) -> str:
        """ Формирует уникальный OrderId """
        cls.last_orderId += 1
        orderId = cls.last_orderId
        return [orderId, cls.prefix + str(orderId)]
    
    @classmethod
    async def getOrder(cls, order_name):
        query = orders_table.select().where(orders_table.c.order_name == order_name)
        return await database.fetch_one(query)
    
    @classmethod
    async def getOrders(cls):
        query = orders_table.select()
        return await database.fetch_all(query)
    
    @classmethod
    async def saveNewOrder(cls, data) -> None:
        """ Сохраняет заказ в БД """
        query = orders_table.insert().values(**data)
        await database.execute(query)

    @classmethod
    async def updateOrder(cls, order, data) -> None:
        """ Сохраняет заказ в БД """
        query = orders_table.update().where(
            orders_table.c.order_id == order.get("order_id")
        ).values(**data)
        await database.execute(query)
    
