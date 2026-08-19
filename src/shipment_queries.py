from sqlalchemy import func, select
from sqlalchemy.orm import Session

from sqlalchemy_db import engine
from models import Shipment


def get_shipment(shipment_id):

    with Session(engine) as session:

        query = select(Shipment).where(
            Shipment.shipmentid == shipment_id
        )

        shipment = session.execute(query).scalar_one_or_none()

        if shipment is None:
            return None

        return shipment.to_dict()


def get_cancelled_shipments(limit=10):

    with Session(engine) as session:

        count_query = (
            select(func.count())
            .select_from(Shipment)
            .where(Shipment.order_status == "Cancelled")
        )

        total_cancelled = session.execute(
            count_query
        ).scalar_one()

        query = (
            select(Shipment)
            .where(Shipment.order_status == "Cancelled")
            .limit(limit)
        )

        shipments = session.execute(query).scalars().all()

        return total_cancelled, [
            shipment.to_dict()
            for shipment in shipments
        ]


def get_top_profitable_shipments(limit=5):

    with Session(engine) as session:

        query = (
            select(
                Shipment.shipmentid,
                Shipment.profit,
                Shipment.country,
            )
            .order_by(Shipment.profit.desc())
            .limit(limit)
        )

        result = session.execute(query)

        return [
            {
                "shipmentid": row.shipmentid,
                "profit": float(row.profit),
                "country": row.country,
            }
            for row in result
        ]


def get_profit_by_region():

    with Session(engine) as session:

        query = (
            select(
                Shipment.region,
                func.sum(Shipment.profit).label("total_profit"),
            )
            .group_by(Shipment.region)
            .order_by(func.sum(Shipment.profit).desc())
        )

        result = session.execute(query)

        return [
            {
                "region": row.region,
                "total_profit": float(row.total_profit),
            }
            for row in result
        ]