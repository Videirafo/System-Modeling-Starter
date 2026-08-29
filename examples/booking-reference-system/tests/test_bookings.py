from fastapi.testclient import TestClient

from app.main import app, repository

client = TestClient(app)


def setup_function() -> None:
    repository.clear()


def booking_payload(start: str, end: str) -> dict[str, str]:
    return {
        "tenant_id": "alpha",
        "professional_id": "pro-01",
        "starts_at": start,
        "ends_at": end,
    }


def test_create_and_get_booking() -> None:
    response = client.post(
        "/bookings",
        json=booking_payload("2026-09-01T10:00:00Z", "2026-09-01T11:00:00Z"),
    )
    assert response.status_code == 201
    booking_id = response.json()["id"]

    fetched = client.get(f"/bookings/{booking_id}")
    assert fetched.status_code == 200
    assert fetched.json()["professional_id"] == "pro-01"


def test_rejects_overlapping_booking_for_same_professional() -> None:
    first = client.post(
        "/bookings",
        json=booking_payload("2026-09-01T10:00:00Z", "2026-09-01T11:00:00Z"),
    )
    assert first.status_code == 201

    conflict = client.post(
        "/bookings",
        json=booking_payload("2026-09-01T10:30:00Z", "2026-09-01T11:30:00Z"),
    )
    assert conflict.status_code == 409
    assert conflict.json()["detail"] == "professional_schedule_conflict"


def test_allows_same_time_for_different_tenant() -> None:
    first = client.post(
        "/bookings",
        json=booking_payload("2026-09-01T10:00:00Z", "2026-09-01T11:00:00Z"),
    )
    assert first.status_code == 201

    other_tenant = booking_payload("2026-09-01T10:00:00Z", "2026-09-01T11:00:00Z")
    other_tenant["tenant_id"] = "beta"
    response = client.post("/bookings", json=other_tenant)
    assert response.status_code == 201


def test_rejects_invalid_time_range() -> None:
    response = client.post(
        "/bookings",
        json=booking_payload("2026-09-01T11:00:00Z", "2026-09-01T10:00:00Z"),
    )
    assert response.status_code == 422
