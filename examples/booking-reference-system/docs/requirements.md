# Requirements — Booking Reference System

## Escopo

Exemplo público e simplificado para demonstrar rastreabilidade entre requisito, regra de negócio, API e teste.

### FR-001 — Criar agendamento

O sistema deve permitir criar um agendamento informando tenant, profissional, início e fim.

**Aceite**
- retorna `201` quando o intervalo é válido e não há conflito;
- retorna o identificador do agendamento criado.

### FR-002 — Consultar agendamento

O sistema deve permitir consultar um agendamento existente pelo identificador.

**Aceite**
- retorna `200` para identificador existente;
- retorna `404` para identificador inexistente.

### BR-001 — Intervalo válido

`ends_at` deve ser posterior a `starts_at`.

### BR-002 — Sem sobreposição no mesmo escopo

Um profissional não pode possuir dois agendamentos sobrepostos dentro do mesmo tenant.

Agendamentos em tenants diferentes são escopos independentes neste exemplo.

### UC-001 — Registrar agendamento

**Ator:** consumidor da API.

**Pré-condição:** payload válido.

**Fluxo principal**
1. consumidor envia `POST /bookings`;
2. sistema valida intervalo;
3. sistema procura sobreposição no mesmo tenant/profissional;
4. sistema cria o booking;
5. sistema retorna `201`.

**Exceções**
- intervalo inválido → `422`;
- conflito de agenda → `409`.
