from shipment_queries import (
    get_shipment,
    get_top_profitable_shipments,
    get_profit_by_region,
    get_cancelled_shipments,
)


def get_shipment_status(shipment_id: str):

    shipment = get_shipment(shipment_id)

    if shipment is None:
        return {
            "success": False,
            "found": False,
            "message": f"Shipment {shipment_id} was not found.",
        }

    return {
        "success": True,
        "found": True,
        "shipmentid": shipment["shipmentid"],
        "status": shipment["order_status"],
        "shipdate": shipment["shipdate"],
        "country": shipment["country"],
        "region": shipment["region"],
    }


def get_top_profitable_shipments_tool(limit: int = 5):

    if limit < 1:
        return {
            "success": False,
            "error": "limit must be at least 1.",
        }

    if limit > 20:
        return {
            "success": False,
            "error": "limit cannot be greater than 20.",
        }

    shipments = get_top_profitable_shipments(limit)

    return {
        "success": True,
        "count": len(shipments),
        "shipments": shipments,
    }


def get_profit_by_region_tool():

    regions = get_profit_by_region()

    return {
        "success": True,
        "regions": regions,
    }


def get_cancelled_shipments_tool(limit: int = 10):

    if limit < 1:
        return {
            "success": False,
            "error": "limit must be at least 1.",
        }

    if limit > 20:
        return {
            "success": False,
            "error": "limit cannot be greater than 20.",
        }

    total_cancelled, shipments = get_cancelled_shipments(limit)

    return {
        "success": True,
        "total_cancelled": total_cancelled,
        "returned": len(shipments),
        "shipments": shipments,
    }