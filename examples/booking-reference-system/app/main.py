from datetime import datetime

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from app.domain import Booking, BookingConflict, BookingRepository

app = FastAPI(
    title="Booking Reference System",
    version="0.1.0",
    description="Traceable example: requirements -> business rules -> API -> tests.",
)
repository = BookingRepository()


class BookingCreate(BaseModel):
    tenant_id: str = Field(min_length=1)
    professional_id: str = Field(min_length=1)
    starts_at: datetime
    ends_at: datetime


class BookingView(BaseModel):
    id: str
    tenant_id: str
    professional_id: str
    starts_at: datetime
    ends_at: datetime


def to_view(booking: Booking) -> BookingView:
    return BookingView(**booking.__dict__)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "booking-reference-system"}


@app.post("/bookings", response_model=BookingView, status_code=status.HTTP_201_CREATED)
def create_booking(payload: BookingCreate) -> BookingView:
    try:
        booking = repository.create(
            tenant_id=payload.tenant_id,
            professional_id=payload.professional_id,
            starts_at=payload.starts_at,
            ends_at=payload.ends_at,
        )
    except BookingConflict as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    return to_view(booking)


@app.get("/bookings/{booking_id}", response_model=BookingView)
def get_booking(booking_id: str) -> BookingView:
    booking = repository.get(booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="booking_not_found")
    return to_view(booking)
