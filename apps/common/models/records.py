from apps.api import db


class Record(db.Model):

    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    site = db.Column(db.String(100), nullable=True)
    item_id = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    nickname = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True, default=None)
