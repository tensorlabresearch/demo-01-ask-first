from typing import Optional
from collections import defaultdict

_ORDERS: list[dict] = []
# (customer, status) -> [orders]; "" key used for customer-only lookups
_INDEX: dict[tuple[str, str], list[dict]] = defaultdict(list)

def seed(n: int = 50_000) -> None:
    """Populate with fake orders for demo purposes."""
    import random, string
    customers = ["alice", "bob", "carol", "dave", "eve"]
    statuses = ["pending", "processing", "shipped", "delivered"]
    _ORDERS.clear()
    _INDEX.clear()
    for i in range(n):
        order = {
            "id": i,
            "customer": random.choice(customers),
            "items": [
                "".join(random.choices(string.ascii_lowercase, k=5))
                for _ in range(random.randint(1, 4))
            ],
            "status": random.choice(statuses),
        }
        _ORDERS.append(order)
        _INDEX[(order["customer"], order["status"])].append(order)
        _INDEX[(order["customer"], "")].append(order)

def find_orders(customer: str, status: Optional[str] = None) -> list[dict]:
    key = (customer, status if status is not None else "")
    return list(_INDEX[key])

def count_by_status() -> dict[str, int]:
    counts: dict[str, int] = {}
    for order in _ORDERS:
        s = order["status"]
        counts[s] = counts.get(s, 0) + 1
    return counts
