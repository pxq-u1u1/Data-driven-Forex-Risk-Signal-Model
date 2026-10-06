# Corporate treasury case

## Question

How could a treasury analyst explain net foreign-currency exposure and a partial-hedge trade-off to a finance manager?

This standalone educational example uses synthetic cash flows to explain exposure netting and hedge-cost trade-offs. It is separate from the project’s historical shock-event studies.

## Inputs and conventions

All cash flows settle on the same assumed date and belong to the same hypothetical entity. Reporting currency is CNY. Each FX rate is **CNY per unit of foreign currency**. Positive cash flows are receipts and negative cash flows are payments. FX rates and shocks are invented, not current market quotes.

| Cash flow | Foreign-currency amount | CNY per unit | Baseline value CNY |
| --- | ---: | ---: | ---: |
| USD receivable | +1,000,000 | 7.20 | +7,200,000 |
| USD payable | -400,000 | 7.20 | -2,880,000 |
| EUR payable | -300,000 | 7.80 | -2,340,000 |

USD net exposure = +600,000 USD, worth +4,320,000 CNY. EUR net exposure = -300,000 EUR, worth -2,340,000 CNY.

Gross exposure **after same-currency netting** = |4,320,000| + |-2,340,000| = 6,660,000 CNY. USD and EUR account for approximately 64.9% and 35.1% of this absolute total. The signed total is +1,980,000 CNY but must not be treated as the gross risk exposure; different currencies do not automatically offset each other's shocks.

## One adverse scenario

Assume USD/CNY falls by 5% and EUR/CNY rises by 3%. Under the quote convention above:

- USD receipt exposure loses 4,320,000 × 5% = 216,000 CNY.
- EUR payment exposure loses 2,340,000 × 3% = 70,200 CNY because the payable becomes more expensive.
- Total change in net cash-flow value = **-286,200 CNY**.

This measures a scenario change in baseline cash-flow value, not total revenue, accounting profit or a statistical loss probability. It deliberately assumes simultaneous shocks and supplies no probability estimate.

## Partial hedge illustration

Assume 50% of each net exposure is covered by a perfectly offsetting hedge locked at the baseline rate. Assume a flat cost of 0.2% of the hedged CNY notional:

- Hedged notional: 6,660,000 × 50% = 3,330,000 CNY.
- Residual adverse scenario impact: -286,200 × 50% = -143,100 CNY.
- Assumed cost: 3,330,000 × 0.2% = 6,660 CNY.
- Net impact after cost: **-149,760 CNY**.

The arithmetic illustrates a trade-off, not an optimised hedge ratio. The assumed cost is not a market option premium or a forward-points calculation. Real instruments also require maturities, executable quotes, forward points, counterparty terms, settlement mechanics and appropriate accounting treatment. The example excludes discounting, basis risk, slippage and collateral requirements.

## Financial interpretation

Start by matching USD receipts against USD payments before discussing derivatives. Then identify the remaining USD receipt and EUR payment risks separately. Compare more than one shock and hedge ratio rather than choosing a policy from a single adverse scenario. A hedge also reduces favourable FX outcomes and adds costs.

The default example contains no VaR calculation because it contains no historical returns or covariance estimates. No annualised Sharpe ratio, prediction accuracy or realised risk reduction is reported.

## Where AI fits

AI could draft a narrative from these calculated numbers or suggest additional macro scenarios for human review. It must not replace the arithmetic, invent live market rates, infer a probability from the scenario, or execute a trade. The offline example makes **no AI call**; the AI architecture is described in [Technical architecture](TECHNICAL_ARCHITECTURE.md).
