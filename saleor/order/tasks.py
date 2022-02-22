from typing import List

from ..celeryconf import app
from ..graphql.order.mutations.utils import invalidate_order_prices
from .models import Order


@app.task
def recalculate_orders_task(order_ids: List[int]):
    orders = Order.objects.filter(id__in=order_ids)
    for order in orders:
        invalidate_order_prices(order, save=True)
