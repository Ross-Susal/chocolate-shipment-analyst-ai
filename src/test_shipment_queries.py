from shipment_queries import (
    get_shipment,
    get_cancelled_shipments,
    get_top_profitable_shipments,
    get_profit_by_region,
)


def test_get_shipment():
    result = get_shipment("S00000004")

    assert result is not None
    assert result["shipmentid"] == "S00000004"


def test_get_shipment_not_found():
    result = get_shipment("Invalid")

    assert result is None


def test_get_cancelled_shipments():
    result1, result2 = get_cancelled_shipments(5)

    assert isinstance(result1, int)
    assert isinstance(result2, list)
    assert len(result2) <= 5

    for shipment in result2:
        assert shipment["shipmentid"] is not None


def test_get_top_profitable_shipments():
    result = get_top_profitable_shipments(5)

    assert isinstance(result, list)
    assert len(result) <= 5

    for shipment in result:
        assert shipment["shipmentid"] is not None
        assert shipment["profit"] is not None


def test_get_profit_by_region():
    result = get_profit_by_region()

    assert isinstance(result, list)

    for row in result:
        assert row["region"] is not None
        assert row["total_profit"] is not None