# Traceability

Rastreabilidade liga necessidade de negócio a evidência técnica.

## Cadeia recomendada

```text
FR/NFR/BR
→ UC / Process
→ Architecture / Data / Contract
→ Implementation
→ TEST
```

## Exemplo

| Requirement | Rule | Use Case | Contract | ADR | Test |
|---|---|---|---|---|---|
| FR-001 | BR-001 | UC-001 | API-001 | ADR-002 | TEST-001 |

## O que rastrear

Priorize:

- fluxos críticos;
- regras com impacto financeiro/regulatório;
- segurança e autorização;
- multi-tenancy/ownership;
- integrações externas;
- decisões arquiteturais relevantes;
- regressões de incidentes.

## O que não fazer

- mapear cada linha de código;
- duplicar backlog inteiro;
- manter planilhas sem owner;
- criar IDs sem uso posterior;
- aceitar matriz desatualizada como verdade.

## Definition of synced

Uma mudança está documentalmente sincronizada quando o comportamento implementado, o contrato e o teste correspondem ao requisito/decisão vigente.