from tools import (
    get_shipment_status,
    get_top_profitable_shipments_tool,
    get_profit_by_region_tool,
    get_cancelled_shipments_tool,
)


def test_get_shipment_status():
    result = get_shipment_status("S00000004")

    assert isinstance(result, dict)
    assert result["success"]
    assert result["shipmentid"] == "S00000004"


def test_get_shipment_status_not_found():
    result = get_shipment_status("INVALID")

    assert isinstance(result, dict)
    assert result["success"] is False


def test_get_top_profitable_shipments_tool():
    result = get_top_profitable_shipments_tool(5)

    assert isinstance(result, dict)
    assert result["success"]
    assert isinstance(result["shipments"], list)
    assert len(result["shipments"]) <= 5


def test_get_profit_by_region_tool():
    result = get_profit_by_region_tool()

    assert isinstance(result, dict)
    assert result["success"]
    assert isinstance(result["regions"], list)


def test_get_cancelled_shipments_tool():
    result = get_cancelled_shipments_tool(5)

    assert isinstance(result, dict)
    assert result["success"]
    assert isinstance(result["shipments"], list)
    assert len(result["shipments"]) <= 5