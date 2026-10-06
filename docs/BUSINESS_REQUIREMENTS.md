# Business requirements and frontend workflows

RiskFX translates cross-border FX risk-management needs into three product workflows. This document summarises the project requirements and maps them to the supplied frontend pages. Requirements describe the intended product behaviour; the interface source is not a certification that every service is operational.

## 1. Risk monitoring

**User question:** What is happening in the FX market, and which developments may affect the currencies relevant to my business?

| Requirement | Financial purpose | Interface information |
| --- | --- | --- |
| Select currency pairs and chart periods | Focus monitoring on relevant exposures and horizons | Pair selector, time range and market charts |
| Refresh professional market data | Review current conditions using source timestamps | Exchange rates, intraday movements and trend charts |
| Track economic and policy events | Connect market movements with potential risk drivers | Event summaries and financial-text signals |
| Compare market signals | Prioritise currencies requiring closer review | Risk indicators and cross-pair views |

Frontend page: `frontend/src/pages/Home/Home.jsx`.

## 2. Risk assessment

**User question:** Where is risk concentrated, and how could an event affect my positions?

The position-analysis workflow uses currency-pair positions, position sizes and weights, and available risk inputs such as daily volatility, VaR and hedge costs. It connects these inputs with event signals and risk classifications to prioritise review.

| Requirement | Financial purpose | Expected output |
| --- | --- | --- |
| Import and inspect position information | Establish the scope of the analysis | Structured position view |
| Review currency and position concentration | Identify dominant sources of exposure | Exposure distribution and priority flags |
| Interpret volatility and VaR inputs | Communicate risk magnitude with consistent metric definitions | Risk-level summaries |
| Examine events and risk transmission | Explain possible links between market developments and positions | Event-linked risk interpretation |

Frontend page: `frontend/src/pages/RiskSignals/RiskSignals.jsx`.

## 3. Risk treatment

**User question:** How can I compare responses to adverse FX conditions?

| Requirement | Financial purpose | Expected output |
| --- | --- | --- |
| Review historical shock events | Learn from observed market disruptions | Historical reference scenarios |
| Apply hypothetical stress scenarios | Examine exposure sensitivity under different assumptions | Scenario impact summaries |
| Consider user risk preferences | Relate proposed responses to the user's priorities | Differentiated hedging considerations |
| Compare risk and cost | Explain the trade-off between protection and expense | Residual exposure and cost discussion |
| Review recommendations | Keep final decisions with the user | Human-reviewed decision summary |

Frontend page: `frontend/src/pages/OneClickDecision/OneClickDecision.jsx`. Its name describes the interface workflow; it does not indicate an authorised live-trading connection.

## Financial interpretation

- Currency-pair positions and corporate receivables/payables are different representations. The standalone cash-flow example demonstrates signed netting separately from the position interface.
- Interpret a VaR value with its confidence level, holding period, currency and calculation method; it is not a maximum possible loss.
- A stress result is conditional on the stated shock, not a prediction or probability estimate.
- Compare hedge costs with the remaining exposure and possible losses under each scenario, rather than evaluating a hedge only by potential return.

For a transparent numerical illustration, see [Financial case](FINANCIAL_CASE.md).
