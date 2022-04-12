from app.schemas.Order import OrderCreate, OrderGet
from app.utils.TinkoffApi import TinkoffApi
from app.utils.Order import Order
from fastapi import APIRouter, Request
from app.models.orders import orders_table, status_table
from datetime import datetime

router = APIRouter()

@router.get("/order")
async def get():
    orders = await Order.getOrders()
    return orders

@router.post("/order/create")
async def create(order: OrderCreate):
    """ Создает новый заказ """
    order_id, order_name = Order.newOrderId()
    data = {
        "OrderId": order_name,
        "Amount": order.amount * 100
    }
    response = TinkoffApi.init(data)
    if not response:
        return {"Status": False, "Message": "Ошибка в работе с платежной системой не найден"}
    if not response["Success"]:
        return response
    await Order.saveNewOrder({
        "order_id": order_id,
        "order_name": response["OrderId"],
        "email": order.email,
        "payment_url": response["PaymentURL"],
        "payment_id": response["PaymentId"],
        "status": "NEW",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    })
    return response

@router.post("/order/handle")
async def handle(request: Request):
    """ Обработка нотификаций"""
    r = await request.json()
    if not TinkoffApi.compareToken(r):
        return "Token is not correct"
    order = await Order.getOrder(r["OrderId"])
    if not order:
        return "Order not found"
    await Order.updateOrder(order, {
        "status": r["Status"]
    })
    return "OK"

@router.get("/order/getState/")
async def getState(number: str = ''):
    order = await Order.getOrder(number)
    if not order:
        return {"Status": False, "Message": "Заказ не найден"}
    result = TinkoffApi.getState(order)
    return await Finish(result, order)

@router.get("/order/confirm/")
async def confirm(number: str = ''):
    order = await Order.getOrder(number)
    if not order:
        return {"Status": False, "Message": "Заказ не найден"}
    result = TinkoffApi.getState(order)
    if (result and result["Status"] == "AUTHORIZED"):
        result = TinkoffApi.confirm(order)
    return await Finish(result, order)

@router.get("/order/refund/")
async def refund(number: str = ''):
    order = await Order.getOrder(number)
    if not order:
        return {"Status": False, "Message": "Заказ не найден"}
    result = TinkoffApi.getState(order)
    if (result and result["Status"] == "CONFIRMED"):
        result = TinkoffApi.refund(order)
    if not result:
        return {"Status": False, "Message": "Ошибка платежной системы"}
    return await Finish(result, order)

async def Finish(result, order):
    if (not result):
        return {"Status": False, "Message": "Ошибка платежной системы"}
    if (not result["Success"]):
        return result
    if (result["Status"] != order.get("status")):
        await Order.updateOrder(order, {
            "status": result["Status"]
        })
    return {"Success": True,"Status": result["Status"]}