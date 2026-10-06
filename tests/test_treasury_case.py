import unittest
from demo.treasury_case import evaluate


class TreasuryTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {'currency': 'USD', 'signed_amount_fc': 1000000, 'cny_per_fc': 7.2},
            {'currency': 'USD', 'signed_amount_fc': -400000, 'cny_per_fc': 7.2},
            {'currency': 'EUR', 'signed_amount_fc': -300000, 'cny_per_fc': 7.8},
        ]
        self.shocks = {'USD': -0.05, 'EUR': 0.03}

    def test_case_numbers(self):
        r = evaluate(self.rows, self.shocks)
        self.assertAlmostEqual(r['gross_netted_exposure_cny'], 6660000)
        self.assertEqual(r['net_exposure_fc']['USD'], 600000)
        self.assertAlmostEqual(r['unhedged_scenario_pnl_cny'], -286200)
        self.assertAlmostEqual(r['assumed_hedge_cost_cny'], 6660)
        self.assertAlmostEqual(r['hedged_scenario_pnl_after_cost_cny'], -149760)
        self.assertAlmostEqual(sum(r['absolute_exposure_weights'].values()), 1)

    def test_no_hedge(self):
        r = evaluate(self.rows, self.shocks, 0)
        self.assertEqual(r['assumed_hedge_cost_cny'], 0)
        self.assertEqual(r['hedged_scenario_pnl_after_cost_cny'], r['unhedged_scenario_pnl_cny'])

    def test_full_ideal_hedge(self):
        r = evaluate(self.rows, self.shocks, 1)
        self.assertAlmostEqual(r['hedged_scenario_pnl_after_cost_cny'], -13320)

    def test_no_shock_only_cost(self):
        r = evaluate(self.rows, {'USD': 0, 'EUR': 0})
        self.assertEqual(r['unhedged_scenario_pnl_cny'], 0)
        self.assertAlmostEqual(r['hedged_scenario_pnl_after_cost_cny'], -6660)

    def test_favourable_scenario(self):
        r = evaluate(self.rows, {'USD': 0.05, 'EUR': -0.03})
        self.assertAlmostEqual(r['unhedged_scenario_pnl_cny'], 286200)
        self.assertLess(r['hedged_scenario_pnl_after_cost_cny'], r['unhedged_scenario_pnl_cny'])

    def test_complete_natural_offset(self):
        rows = [{'currency':'USD','signed_amount_fc':x,'cny_per_fc':7.2} for x in (100,-100)]
        r = evaluate(rows, {'USD': -0.05})
        self.assertEqual(r['gross_netted_exposure_cny'], 0)
        self.assertEqual(r['absolute_exposure_weights']['USD'], 0)
        self.assertEqual(r['hedged_scenario_pnl_after_cost_cny'], 0)

    def test_invalid_parameters(self):
        for h,k in [(-.1,.002),(1.1,.002),(.5,-1),(float('nan'),.002)]:
            with self.subTest(h=h,k=k), self.assertRaises(ValueError):
                evaluate(self.rows,self.shocks,h,k)

    def test_invalid_inputs(self):
        for key,value in [('signed_amount_fc','nan'),('cny_per_fc',0),('currency','USD/JPY')]:
            rows = [dict(row) for row in self.rows]
            rows[0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                evaluate(rows,self.shocks)

    def test_inconsistent_rates(self):
        self.rows[1]['cny_per_fc'] = 7.3
        with self.assertRaises(ValueError):
            evaluate(self.rows,self.shocks)

    def test_missing_or_invalid_shock(self):
        for shocks in [{'USD':0},{'USD':-1,'EUR':0},{'USD':0,'EUR':float('inf')}, {'USD':0,'EUR':0,'JPY':0}]:
            with self.subTest(shocks=shocks), self.assertRaises(ValueError):
                evaluate(self.rows,shocks)

    def test_empty(self):
        with self.assertRaises(ValueError):
            evaluate([], {})


if __name__ == '__main__':
    unittest.main()
