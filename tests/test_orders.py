import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.orders import seed, find_orders, count_by_status

def setup_module():
    seed(100)

def test_find_orders_returns_correct_customer():
    results = find_orders("alice")
    assert all(r["customer"] == "alice" for r in results)

def test_find_orders_filters_by_status():
    results = find_orders("bob", status="pending")
    assert all(r["status"] == "pending" for r in results)

def test_count_by_status_keys():
    counts = count_by_status()
    assert "pending" in counts or "shipped" in counts
