# Traceability Matrix

| Requirement / Rule | API / Code | Test evidence |
|---|---|---|
| FR-001 Criar agendamento | `POST /bookings` · `BookingRepository.create` | `test_create_and_get_booking` |
| FR-002 Consultar agendamento | `GET /bookings/{booking_id}` | `test_create_and_get_booking` |
| BR-001 Intervalo válido | `BookingRepository.create` | `test_rejects_invalid_time_range` |
| BR-002 Sem sobreposição | `BookingRepository.create` | `test_rejects_overlapping_booking_for_same_professional` |
| Tenant scope do exemplo | `BookingRepository.create` | `test_allows_same_time_for_different_tenant` |

## Regra de manutenção

Quando requisito, contrato ou regra mudar, a mesma Pull Request deve revisar esta matriz e os testes relacionados.
