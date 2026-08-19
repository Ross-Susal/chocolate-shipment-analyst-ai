from tools import (
    get_shipment_status,
    get_top_profitable_shipments_tool,
    get_profit_by_region_tool,
    get_cancelled_shipments_tool,
)


# Test shipment status tool
print("Shipment status:")
print(get_shipment_status("S00000004"))


# Test top profitable shipments tool
print("\nTop 5 profitable shipments:")
print(get_top_profitable_shipments_tool(5))


# Test profit by region tool
print("\nProfit by region:")
print(get_profit_by_region_tool())


# Test cancelled shipments tool
print("\nCancelled shipments:")
print(get_cancelled_shipments_tool(5))