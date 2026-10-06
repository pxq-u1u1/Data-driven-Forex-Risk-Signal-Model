"""New portfolio-preparation illustration, NOT original competition code.

Synthetic, same-date cash flows. Standard library only; no AI/network calls.
"""
import csv
import json
import math
from pathlib import Path


def number(value, name):
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f'{name} must be finite')
    return result


def evaluate(rows, shocks, hedge_ratio=0.5, hedge_cost_rate=0.002):
    """Net within currency; return CNY scenario values under an ideal hedge."""
    h = number(hedge_ratio, 'hedge_ratio')
    k = number(hedge_cost_rate, 'hedge_cost_rate')
    if not 0 <= h <= 1 or k < 0:
        raise ValueError('hedge ratio must be in [0,1]; cost rate must be nonnegative')
    net, rates = {}, {}
    for row in rows:
        currency = str(row['currency']).strip().upper()
        if len(currency) != 3 or not currency.isascii() or not currency.isalpha():
            raise ValueError('currency must be a three-letter code')
        amount = number(row['signed_amount_fc'], 'signed_amount_fc')
        rate = number(row['cny_per_fc'], 'cny_per_fc')
        if rate <= 0:
            raise ValueError('exchange rates must be positive')
        if currency in rates and not math.isclose(rates[currency], rate, rel_tol=1e-12):
            raise ValueError('a currency must have one consistent baseline rate')
        rates[currency] = rate
        net[currency] = net.get(currency, 0.0) + amount
    if not net:
        raise ValueError('at least one cash flow is required')
    if set(shocks) != set(net):
        raise ValueError('supply one shock per input currency, with no extras')
    scenario = {c: number(shocks[c], 'shock') for c in net}
    if any(s <= -1 for s in scenario.values()):
        raise ValueError('shocks must leave FX rates positive')
    values = {c: net[c] * rates[c] for c in net}
    gross = sum(abs(v) for v in values.values())
    if not math.isfinite(gross):
        raise ValueError('cash-flow values overflow')
    impacts = {c: values[c] * scenario[c] for c in net}
    pnl = sum(impacts.values())
    cost = gross * h * k
    if not all(math.isfinite(v) for v in [pnl, cost, *impacts.values()]):
        raise ValueError('scenario values overflow')
    return {
        'status': 'Synthetic educational illustration; not a forecast or backtest',
        'reporting_currency': 'CNY',
        'net_exposure_fc': net,
        'net_exposure_cny': values,
        'gross_netted_exposure_cny': gross,
        'absolute_exposure_weights': {c: abs(v) / gross if gross else 0 for c, v in values.items()},
        'scenario_shocks': scenario,
        'scenario_pnl_by_currency_cny': impacts,
        'unhedged_scenario_pnl_cny': pnl,
        'hedge_ratio_assumption': h,
        'hedge_cost_rate_assumption': k,
        'assumed_hedge_cost_cny': cost,
        'hedged_scenario_pnl_after_cost_cny': (1 - h) * pnl - cost,
    }


def main():
    path = Path(__file__).resolve().parents[1] / 'examples/synthetic_cashflows.csv'
    with path.open(newline='', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    print(json.dumps(evaluate(rows, {'USD': -0.05, 'EUR': 0.03}), indent=2))


if __name__ == '__main__':
    main()
