from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


class BookingConflict(Exception):
    """Raised when a professional already has an overlapping booking."""


@dataclass(frozen=True)
class Booking:
    id: str
    tenant_id: str
    professional_id: str
    starts_at: datetime
    ends_at: datetime


class BookingRepository:
    def __init__(self) -> None:
        self._items: list[Booking] = []

    def clear(self) -> None:
        self._items.clear()

    def get(self, booking_id: str) -> Booking | None:
        return next((item for item in self._items if item.id == booking_id), None)

    def create(
        self,
        *,
        tenant_id: str,
        professional_id: str,
        starts_at: datetime,
        ends_at: datetime,
    ) -> Booking:
        if ends_at <= starts_at:
            raise ValueError("ends_at_must_be_after_starts_at")

        for existing in self._items:
            same_scope = (
                existing.tenant_id == tenant_id
                and existing.professional_id == professional_id
            )
            overlaps = starts_at < existing.ends_at and ends_at > existing.starts_at
            if same_scope and overlaps:
                raise BookingConflict("professional_schedule_conflict")

        booking = Booking(
            id=str(uuid4()),
            tenant_id=tenant_id,
            professional_id=professional_id,
            starts_at=starts_at,
            ends_at=ends_at,
        )
        self._items.append(booking)
        return booking
