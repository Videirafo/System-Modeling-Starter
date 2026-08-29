# Modeling Method

## 1. Discover

Antes de modelar, identifique:

- problema e objetivo;
- usuários/atores;
- regras de negócio;
- sistema atual, se existir;
- integrações externas;
- restrições técnicas e regulatórias;
- dados principais;
- riscos e ambiguidades.

## 2. Requirements

Escreva requisitos pequenos, identificáveis e testáveis.

### Functional

```text
FR-001 — O cliente deve conseguir criar uma reserva.
```

### Non-functional

```text
NFR-001 — 95% das consultas críticas devem responder dentro do SLO definido.
```

### Business rule

```text
BR-001 — Um horário não pode ser reservado por dois clientes simultaneamente.
```

## 3. Use cases

Use casos de uso para representar objetivo observável de um ator externo.

Evite:

- usar "Sistema" como ator genérico;
- transformar cada clique em caso de uso;
- duplicar regra de negócio dentro de todos os casos;
- usar `include`/`extend` apenas para deixar diagrama mais complexo.

## 4. Process modeling

Use BPMN quando o foco é processo de negócio, responsabilidades, eventos e handoffs.

Use Activity Diagram quando o foco é comportamento/algoritmo do sistema.

## 5. Architecture

Comece pelo nível mais alto necessário.

```text
C4 Context
→ C4 Container
→ C4 Component (somente quando útil)
```

O objetivo não é desenhar cada classe; é comunicar decisões e fronteiras.

## 6. Data

Modele:

1. conceitos;
2. relacionamentos;
3. cardinalidade;
4. invariantes;
5. chaves;
6. isolamento/ownership quando multi-tenant;
7. histórico/auditoria quando necessário.

## 7. Contracts

### HTTP

Use OpenAPI para operações, parâmetros, schemas, autenticação e respostas.

### Events

Use AsyncAPI para canais, mensagens, payloads e operações send/receive.

## 8. Decisions

Quando houver escolha arquitetural relevante, crie ADR com contexto, decisão, alternativas e consequências.

## 9. Traceability

Conecte:

```text
Requirement
→ Business Rule
→ Use Case
→ Architecture/Data/API
→ Implementation
→ Test
```

Não é necessário rastrear cada linha de código. Priorize fluxos críticos e decisões importantes.

## 10. Documentation sync

Mudanças em comportamento relevante exigem verificar:

- requisitos;
- diagramas;
- contracts;
- ADRs;
- testes;
- runbooks.

## AS-IS vs TO-BE

Em sistemas existentes, não misture os dois modelos.

- **AS-IS:** evidencia o que existe hoje.
- **TO-BE:** evidencia a mudança aprovada.

A diferença entre ambos vira backlog/roadmap de implementação.