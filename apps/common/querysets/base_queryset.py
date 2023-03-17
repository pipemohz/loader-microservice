from sqlalchemy.orm import Session


class BaseQuerySet:
    def __init__(self, model, db: Session) -> None:
        self.db = db
        self.model = model

    def get(self):
        return self.db.query(self.model).all()

    def find(self, id: int):
        return self.db.query(self.model).get(id)

    def where(self, expr):
        return self.db.query(self.model).where(expr)
