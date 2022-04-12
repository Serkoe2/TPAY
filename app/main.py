import uvicorn
from app.routers import order, view
from app.db_config import database
from app.models.orders import orders_table, status_table
from app.utils.Order import Order
from fastapi import FastAPI
from sqlalchemy.inspection import inspect
from sqlalchemy import desc


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    query = orders_table.select().order_by(desc(orders_table.c.order_id))
    r = await database.fetch_one(query)
    if not r:
        Order.last_orderId = 1
    else:
        Order.last_orderId = r.get("order_id")
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/test")
async def test():
    return '1'

app.include_router(order.router)
app.include_router(view.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
