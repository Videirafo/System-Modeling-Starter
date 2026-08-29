<div align="center">

# System Modeling Starter

### Requirements · UML · BPMN · C4 · ERD · OpenAPI · AsyncAPI · ADR · Traceability

**Starter público para transformar problema de negócio em documentação implementável e verificável.**

</div>

---

## Objetivo

Evitar dois extremos comuns:

1. construir software sem especificação suficiente;
2. criar documentação bonita que não corresponde ao sistema real.

Este starter propõe um fluxo simples:

```text
DISCOVER
→ REQUIREMENTS
→ BUSINESS RULES
→ USE CASES
→ PROCESS / ARCHITECTURE
→ DATA
→ API / EVENT CONTRACTS
→ ADR
→ TRACEABILITY
→ IMPLEMENTATION
→ TESTS
→ DOC SYNC
```

## Identificadores recomendados

```text
FR-###   Functional Requirement
NFR-###  Non-Functional Requirement
BR-###   Business Rule
UC-###   Use Case
API-###  API Contract
EVT-###  Event Contract
ADR-###  Architecture Decision Record
TEST-### Test / Acceptance Scenario
```

## Qual diagrama usar?

| Pergunta | Artefato sugerido |
|---|---|
| Quem usa o sistema e para quê? | UML Use Case |
| Como um processo atravessa atores/áreas? | BPMN |
| Qual o fluxo de decisão? | UML Activity |
| Quem chama quem e em qual ordem? | UML Sequence |
| Quais estados existem? | UML State Machine |
| Quais conceitos e relações existem? | UML Class / ERD |
| Como o sistema se encaixa no ecossistema? | C4 System Context |
| Quais apps, serviços e stores compõem o sistema? | C4 Container |
| Quais módulos internos importam? | C4 Component |
| Como a API HTTP é contratada? | OpenAPI |
| Como eventos/mensagens são contratados? | AsyncAPI |
| Por que uma decisão arquitetural foi tomada? | ADR |

O C4 oficial recomenda usar apenas os níveis que agregam valor; para muitas equipes, Context + Container já cobrem a maior parte das necessidades.

## AS-IS antes de TO-BE

Em sistemas existentes:

```text
EVIDENCE
→ CURRENT IMPLEMENTATION
→ AS-IS MODEL
→ GAPS
→ TO-BE DECISION
→ CHANGE PLAN
```

Não invente endpoints, entidades, regras ou componentes para "completar" um diagrama.

## Estrutura do starter

```text
docs/
├── METHOD.md
├── DIAGRAM_SELECTION.md
└── TRACEABILITY.md

templates/
├── USE_CASE_TEMPLATE.md
├── ADR_TEMPLATE.md
└── TRACEABILITY_MATRIX.md

contracts/
├── openapi.yaml
└── asyncapi.yaml

examples/diagrams/
├── c4-context.mmd
├── use-case.puml
└── erd.mmd
```

## Diagram source + render

Sempre que possível mantenha a fonte editável e o render:

```text
diagrams/
├── system-context.dsl
├── system-context.svg
├── booking-sequence.puml
└── booking-sequence.svg
```

Ferramentas possíveis:

- PlantUML — UML;
- Mermaid — documentação Markdown e diagramas leves;
- Structurizr DSL — C4;
- Astah — quando `.asta` fizer parte da entrega;
- ferramentas ERD compatíveis com o banco/projeto.

## Standards base

O starter acompanha:

- UML 2.5.1 — OMG;
- BPMN 2.0.2 — OMG;
- C4 Model — site oficial de Simon Brown;
- OpenAPI Specification — contratos HTTP;
- AsyncAPI — contratos event-driven.

## Templates

- [Caso de Uso](./templates/USE_CASE_TEMPLATE.md)
- [ADR](./templates/ADR_TEMPLATE.md)
- [Matriz de rastreabilidade](./templates/TRACEABILITY_MATRIX.md)

## Contratos iniciais

- [OpenAPI starter](./contracts/openapi.yaml)
- [AsyncAPI starter](./contracts/asyncapi.yaml)

## Regra principal

> Documentação deve reduzir ambiguidade e tornar implementação/teste mais verificáveis. Se não muda nenhuma decisão nem ajuda ninguém a entender o sistema, provavelmente não precisa existir.

## Segurança

Não publique diagramas de topologia sensível, IPs, secrets, credenciais, requisitos confidenciais ou dados de clientes. Consulte [SECURITY.md](./SECURITY.md).

## Status

**v0.1 — foundation.** Próximas versões devem incluir um exemplo completo requirements → diagrams → contracts → tests.

---

Criado por [Fernando Videira](https://github.com/Videirafo) como parte de uma base pública de engenharia de software.
