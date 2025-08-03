from fastapi import APIRouter, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

from app.repositories.mongo_order_repository import MongoOrderRepository
from app.usecases.create_order import CreateOrderUseCase
from app.usecases.list_orders import ListOrdersUseCase
from app.usecases.count_orders import CountOrdersUseCase
from app.usecases.get_order_detail import GetOrderDetailUseCase
from app.usecases.delete_order import DeleteOrderUseCase
from app.utils.date_utils import format_brazilian_date, format_brazilian_datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

templates.env.filters["brazilian_date"] = format_brazilian_date
templates.env.filters["brazilian_datetime"] = format_brazilian_datetime

repo = MongoOrderRepository()

@router.get("/orders", response_class=HTMLResponse)
async def list_orders(request: Request,
                      name: str = Query(None),
                      start_date: str = Query(None),
                      end_date: str = Query(None),
                      page: int = Query(1)):
    filters = {}
    if name:
        filters["customer_name"] = {"$regex": name, "$options": "i"}
    if start_date and end_date:
        filters["order_date"] = {
            "$gte": datetime.fromisoformat(start_date),
            "$lte": datetime.fromisoformat(end_date)
        }
    page_size = 10
    skip = (page - 1) * page_size
    orders = await ListOrdersUseCase(repo).execute(filters, skip, page_size)
    total = await CountOrdersUseCase(repo).execute(filters)
    return templates.TemplateResponse("orders.html", {
        "request": request,
        "orders": orders,
        "name": name or "",
        "start_date": start_date or "",
        "end_date": end_date or "",
        "page": page,
        "total_pages": (total // page_size) + int(total % page_size > 0)
    })

@router.get("/orders/new", response_class=HTMLResponse)
async def new_order(request: Request):
    return templates.TemplateResponse("new_order.html", {"request": request})

@router.post("/orders")
async def create_order(customer_name: str = Form(...),
                       customer_email: str = Form(...),
                       order_date: str = Form(...),
                       item_name: list[str] = Form(...),
                       item_quantity: list[int] = Form(...),
                       item_unit_price: list[float] = Form(...)):
    items = []
    for name, qty, price in zip(item_name, item_quantity, item_unit_price):
        items.append({
            "name": name,
            "quantity": qty,
            "unit_price": price
        })
    order = {
        "customer_name": customer_name,
        "customer_email": customer_email,
        "order_date": datetime.fromisoformat(order_date),
        "items": items
    }
    await CreateOrderUseCase(repo).execute(order)
    return RedirectResponse(url="/orders", status_code=303)

@router.get("/orders/{order_id}", response_class=HTMLResponse)
async def order_detail(request: Request, order_id: str):
    order = await GetOrderDetailUseCase(repo).execute(order_id)
    return templates.TemplateResponse("order_detail.html", {"request": request, "order": order})

@router.post("/orders/{order_id}/delete")
async def delete_order(order_id: str):
    await DeleteOrderUseCase(repo).execute(order_id)
    return RedirectResponse(url="/orders", status_code=303)