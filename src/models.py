from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Integer, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Shipment(Base):
    __tablename__ = "shipments"

    shipmentid: Mapped[str] = mapped_column(
        "shipmentid",
        String(20),
        primary_key=True
    )

    spid: Mapped[str] = mapped_column(
        "spid",
        String(10)
    )

    pid: Mapped[str] = mapped_column(
        "pid",
        String(10)
    )

    gid: Mapped[str] = mapped_column(
        "gid",
        String(10)
    )

    shipdate: Mapped[date] = mapped_column(
        "shipdate",
        Date
    )

    amount: Mapped[Decimal] = mapped_column(
        "amount",
        Numeric(12, 2)
    )

    boxes: Mapped[int] = mapped_column(
        "boxes",
        Integer
    )

    order_status: Mapped[str] = mapped_column(
        "order_status",
        String(20)
    )

    revenue_per_box: Mapped[Decimal] = mapped_column(
        "revenue_per_box",
        Numeric(12, 2)
    )

    profit: Mapped[Decimal] = mapped_column(
        "profit",
        Numeric(12, 2)
    )

    cost_price: Mapped[Decimal] = mapped_column(
        "cost_price",
        Numeric(12, 2)
    )

    profit_margin: Mapped[Decimal] = mapped_column(
        "Profit_Margin%",
        Numeric(8, 2)
    )

    sales_person: Mapped[str] = mapped_column(
        "sales_person",
        String(100)
    )

    team: Mapped[str] = mapped_column(
        "team",
        String(50)
    )

    product: Mapped[str] = mapped_column(
        "product",
        String(150)
    )

    category: Mapped[str] = mapped_column(
        "category",
        String(100)
    )

    country: Mapped[str] = mapped_column(
        "country",
        String(100)
    )

    region: Mapped[str] = mapped_column(
        "region",
        String(50)
    )

    cost_per_box: Mapped[Decimal] = mapped_column(
        "cost_per_box",
        Numeric(12, 2)
    )

    cancelled: Mapped[int] = mapped_column(
        "cancelled",
        Integer
    )

    def to_dict(self):

        return {
            "shipmentid": self.shipmentid,
            "spid": self.spid,
            "pid": self.pid,
            "gid": self.gid,
            "shipdate": str(self.shipdate),
            "amount": float(self.amount),
            "boxes": self.boxes,
            "order_status": self.order_status,
            "revenue_per_box": float(self.revenue_per_box),
            "profit": float(self.profit),
            "cost_price": float(self.cost_price),
            "profit_margin": float(self.profit_margin),
            "sales_person": self.sales_person,
            "team": self.team,
            "product": self.product,
            "category": self.category,
            "country": self.country,
            "region": self.region,
            "cost_per_box": float(self.cost_per_box),
            "cancelled": self.cancelled
        }