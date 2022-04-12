import sqlalchemy

metadata = sqlalchemy.MetaData()

status_table = sqlalchemy.Table(
    "status",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(20))
)

orders_table = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("order_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("order_name", sqlalchemy.String(100)),
    sqlalchemy.Column("payment_url", sqlalchemy.String(100)),
    sqlalchemy.Column("email", sqlalchemy.String(40), index=True),
    sqlalchemy.Column("status", sqlalchemy.String(15)),
    sqlalchemy.Column("payment_id", sqlalchemy.String(40)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime())
)