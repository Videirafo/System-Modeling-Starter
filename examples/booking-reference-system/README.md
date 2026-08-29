# Booking Reference System

Projeto executável do **System Modeling Starter** que conecta documentação e implementação:

```text
FR / BR / UC
→ API
→ domain rule
→ automated test
→ traceability matrix
```

## Clonar e abrir no VS Code

```bash
git clone https://github.com/Videirafo/System-Modeling-Starter.git
cd System-Modeling-Starter/examples/booking-reference-system
code .
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
fastapi dev
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
fastapi dev
```

Abra `http://127.0.0.1:8000/docs`.

## Executar testes

```bash
pytest
```

## Artefatos conectados

- [Requirements](./docs/requirements.md)
- [Traceability Matrix](./docs/traceability.md)
- [Context diagram source](./diagrams/context.mmd)
- `app/domain.py` — regras de negócio;
- `app/main.py` — contrato HTTP;
- `tests/test_bookings.py` — evidência automatizada.

## Fluxos disponíveis

- `GET /health`
- `POST /bookings`
- `GET /bookings/{booking_id}`

### Regra principal

O mesmo profissional não pode receber horários sobrepostos dentro do mesmo tenant. O exemplo mantém armazenamento em memória para que qualquer pessoa possa clonar e executar sem banco ou credenciais.

## Evolução sugerida

1. PostgreSQL + migrations;
2. tenant resolution autenticado;
3. idempotency key no `POST /bookings`;
4. OpenAPI versionado como contrato;
5. sequence diagram e ADR de persistência;
6. teste de concorrência para double booking.

## Fazer sua branch

```bash
git checkout -b feat/minha-evolucao
git add .
git commit -m "feat: evolve booking reference system"
git push -u origin feat/minha-evolucao
```
