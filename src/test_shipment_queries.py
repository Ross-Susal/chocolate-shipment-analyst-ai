from shipment_queries import (
    get_shipment,
    get_cancelled_shipments,
    get_top_profitable_shipments,
    get_profit_by_region,
)


# Test shipment lookup
shipment = get_shipment("S00000004")

if shipment is None:
    print("Shipment not found")
else:
    print("Shipment ID:", shipment["shipmentid"])
    print("Status:", shipment["order_status"])
    print("Country:", shipment["country"])
    print("Profit:", shipment["profit"])


# Test cancelled shipments
total_cancelled, cancelled = get_cancelled_shipments(5)

print("\nTotal cancelled shipments:", total_cancelled)
print("Returned cancelled shipments:", len(cancelled))

for shipment in cancelled:
    print(shipment)


# Test top profitable shipments
top_shipments = get_top_profitable_shipments(5)

print("\nTop 5 profitable shipments:")

for shipment in top_shipments:
    print(shipment)


# Test profit by region
profit_by_region = get_profit_by_region()

print("\nProfit by region:")

for row in profit_by_region:
    print(row)