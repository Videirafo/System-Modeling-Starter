# Diagram Selection Guide

Use o menor conjunto de diagramas que responda às perguntas reais do projeto.

| Necessidade | Diagrama | Quando evitar |
|---|---|---|
| atores e objetivos | UML Use Case | quando o problema é fluxo interno detalhado |
| processo entre áreas/sistemas | BPMN | quando basta um fluxo técnico simples |
| fluxo lógico | UML Activity | quando o objetivo é processo organizacional |
| interação temporal | UML Sequence | quando não há ordem relevante de chamadas |
| estados/transições | UML State Machine | para CRUD simples sem ciclo de vida significativo |
| estrutura de domínio | UML Class | quando ERD ou código já comunica melhor |
| dados relacionais | ERD | para arquitetura de runtime |
| ecossistema | C4 Context | para detalhes internos |
| apps/services/datastores | C4 Container | quando só contexto já basta |
| módulos internos | C4 Component | se não muda decisão nem entendimento |
| runtime/deploy | C4 Deployment | se infraestrutura não é relevante ao problema |

## Regras de legibilidade

- título explícito;
- escopo claro;
- legenda quando a notação não for óbvia;
- nomes reais de sistemas externos;
- relações direcionais quando direção importa;
- evitar cruzamento excessivo de linhas;
- não colocar detalhes de implementação em diagramas de alto nível.

## Source of truth

Sempre que possível mantenha o arquivo fonte editável no Git e gere o render a partir dele.

Exemplos:

```text
checkout-sequence.puml → checkout-sequence.svg
system-context.dsl → system-context.svg
process.bpmn → process.svg
schema.dbml → schema.svg
```

## C4 pragmático

Na maioria dos times, **System Context + Container** é suficiente. Component/Code entram apenas quando agregam informação útil para uma decisão, onboarding ou manutenção.