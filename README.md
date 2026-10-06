# RiskFX | Data-driven Forex Risk Signal Model

**FX exposure monitoring, historical shock-event analysis and hedging decision support for cross-border businesses.**

RiskFX combines professional FX market data, financial-event text analysis and portfolio risk information to help treasury users understand how market shocks may affect their currency exposures. The project connects three business workflows: **risk monitoring → risk assessment → risk treatment**.

[中文](README.zh-CN.md) · [Business requirements](docs/BUSINESS_REQUIREMENTS.md) · [Technical architecture](docs/TECHNICAL_ARCHITECTURE.md) · [Financial example](docs/FINANCIAL_CASE.md)

## Project highlights

- **Professional market data:** integration with Tonghuashun iFinD real-time and high-frequency/intraday interfaces to refresh FX market information. Data frequency and availability depend on the subscribed service and source timestamps.
- **Historical shock-event backtesting:** event-focused analysis of selected currency pairs and broader FX market co-movements during major disruptions, rather than relying only on ordinary market conditions.
- **30+ mainstream currency pairs:** coverage for reviewing multiple currency exposures and comparing market signals across pairs.
- **Financial-event analysis:** text features, event-relevance scores, sentiment and estimated volatility-impact scores support identification of potentially affected currency pairs and directional signals.
- **Integrated product design:** documented requirements and frontend workflows connect market monitoring, exposure assessment, stress scenarios and hedging considerations.

## Financial use case

A cross-border business may receive revenue in one currency and pay suppliers in another. A market shock can change the reporting-currency value of those cash flows, increase the cost of outstanding payments and make previously diversified exposures move together.

RiskFX frames the analysis around four questions:

1. Which currency exposures and concentrations deserve attention?
2. Which economic, policy or geopolitical developments may affect them?
3. How could those exposures behave under historical or hypothetical shocks?
4. How do potential hedges change residual risk and costs under the user's risk preferences?

| Workflow | Financial focus | Product design |
| --- | --- | --- |
| Risk monitoring | FX movements and emerging event risks | Market dashboard, currency-pair charts, economic and policy event tracking |
| Risk assessment | Exposure concentration, volatility, input VaR and risk transmission | Position review, risk signals, risk classification and event interpretation |
| Risk treatment | Scenario losses and hedging trade-offs | Multi-currency exposure analysis, historical-event review, stress testing and decision summaries |

## Historical shocks and stress scenarios

Historical event backtesting focuses on how shocks affect selected currency pairs and their co-movement with the wider FX market. The project's event-study windows are:

| Project study window | Event focus | Financial question |
| --- | --- | --- |
| 2007–2009 | Subprime mortgage crisis | How do funding stress and changing risk appetite affect FX exposures? |
| 2008–2013 | European debt crisis and surrounding stress period | How do sovereign-credit concerns and regional financial stress transmit across currencies? |
| 2015 | Equity-market crash | How does equity-market turbulence coincide with currency movements and risk repricing? |
| 2020 | Public-health shock | How do abrupt disruptions affect FX volatility and exposure sensitivity? |

These are the project's analysis windows, not precise start and end dates for each crisis. The purpose is to use traceable historical shocks as references for analysing new conditions, including tariff disputes and geopolitical conflicts.

**Historical backtesting and forward-looking stress testing serve different purposes.** Historical analysis studies observed events; stress testing applies explicit hypothetical assumptions, ranging from routine fluctuations to severe tail scenarios. Historical analogies inform scenario selection and hedging discussion; they do not establish that future events will repeat or that unprecedented black-swan events can be predicted.

## Financial-event signals

The event-analysis approach combines financial-text representations with event-relevance, sentiment and estimated volatility-impact scores. Downstream model components associate these features with currency-pair, direction and confidence-score outputs to support risk review.

Text-derived volatility-impact scores describe an interpretation of news, distinct from volatility calculated from price returns. Signal confidence is a model score, not a guaranteed probability of a market outcome.

## ReAct-based collaborative hedging architecture

The technical design, set out in Section 4.2 of the project business plan, combines **ReAct, LangGraph and LangChain** to organise financial analysis and tool use. It includes a multi-agent research workflow and a LangSmith observability component.

| Component | Role in the documented design | Financial purpose |
| --- | --- | --- |
| ReAct | Iterative reasoning, tool calls and observation of results | Analyse positions, request relevant risk calculations and refine the assessment |
| LangGraph | Shared task state, conditional routing and analysis subgraphs | Coordinate exposure, market-volatility, correlation and event-analysis tasks |
| LangChain | Model interfaces, prompt templates, tool wrappers and structured outputs | Reuse financial-analysis components and return consistent decision-support information |
| Multi-agent research | Subtopic decomposition, parallel analysis and aggregation | Combine different analytical perspectives into a coherent risk report |
| Human review | Review scope, assumptions and recommendations | Keep hedging decisions under user control |
| LangSmith | Tracing and error/performance monitoring in the architecture | Inspect tool calls and diagnose problems in the analysis workflow |

The architecture describes the project's intended analytical workflow. This release contains frontend source, business and architecture documentation, and a separate offline financial example; backend services and model-training code are outside this release.

## Explore the repository

| Path | Contents |
| --- | --- |
| `frontend/` | React interface source for monitoring, risk signals and decision support |
| `docs/BUSINESS_REQUIREMENTS.md` | Financial needs, workflow requirements and page mapping |
| `docs/TECHNICAL_ARCHITECTURE.md` | ReAct workflow and multi-agent collaboration design |
| `docs/FINANCIAL_CASE.md` | Synthetic cash-flow netting and partial-hedge example |
| `docs/RUNNING.md` | Scope and execution instructions |
| `demo/`, `examples/`, `tests/` | Offline calculation example, synthetic inputs and tests |

Run the standalone example with Python 3.10 or later:

```bash
python demo/treasury_case.py
python -m unittest discover -s tests -v
```

The example needs no credentials or external services. Its synthetic cash flows illustrate netting, FX shocks and hedge costs; they are separate from the historical event backtests. The frontend requires compatible backend services for live data and analysis; it is provided as interface source, not a hosted live terminal.

## Project context

Developed as a team project for the 20th Citi Financial Innovation Application Competition. The project received a national third prize and placed in the national top 20.

RiskFX is an academic prototype for research and decision support. It does not execute live trades or provide investment advice. Market-data access is subject to provider authorisation; this release does not distribute provider credentials, licensed market datasets or model weights.
