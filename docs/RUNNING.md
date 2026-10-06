# Running the included example

## Offline financial calculation

Use Python 3.10 or later from the repository root:

```bash
python demo/treasury_case.py
python -m unittest discover -s tests -v
```

No third-party package, network connection, market-data subscription or API key is required. Inputs are in `examples/synthetic_cashflows.csv`.

The example reports:

- Net exposure by currency after matching same-currency receipts and payments.
- Exposure weights measured on an absolute reporting-currency basis.
- Changes in cash-flow value under an assumed FX shock.
- A partial hedge illustration with an explicit assumed cost.

Default values yield gross netted exposure of CNY 6,660,000, an unhedged scenario impact of CNY -286,200, and a 50% hedge scenario impact after assumed cost of CNY -149,760. These are synthetic calculations, not historical backtest returns.

## Frontend source

The React/Vite source is in `frontend/`. It includes market monitoring, risk signals and decision-support pages. The source expects compatible backend endpoints, including local API calls, for live market information and analytical results.

This release does not include those services, provider credentials, trained model weights or a full historical-backtest runner. Frontend dependencies and service integration have not been validated as an end-to-end running application in this release. See the source package for its existing development and build scripts.

## Test scope

The Python tests cover signed netting, scenario arithmetic, partial/full/zero hedging, favourable and adverse movements, natural offsets, and invalid-input handling. They validate the included financial example only; they do not validate the historical-event model or forecast accuracy.
