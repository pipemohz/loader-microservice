from apps.common.querysets.base_queryset import BaseQuerySet
from apps.common.models.records import Record


class RecordQuerySet(BaseQuerySet):
    def __init__(self, db) -> None:
        super().__init__(Record, db)
