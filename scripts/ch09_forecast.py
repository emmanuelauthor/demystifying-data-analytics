"""Reproduce the illustrative 2026 forecast in Chapter 9 (Figure 9.8).

Model: statsmodels ETSModel on 24 monthly net sales totals (Jan 2024 to Dec 2025),
error="add", trend="add", seasonal="mul", seasonal_periods=12, fitted by maximum likelihood.
Point forecast: the model's mean for Jan to Dec 2026, summed for the annual total.
Annual 95% range: 20,000 simulated 12-month future paths (normal errors with the fitted
residual variance, generated with numpy default_rng(2026));
each path is summed to a 2026 total, and the 2.5th and 97.5th percentiles of
those totals form the range. (Adding up monthly limits would overstate the range.)
Requires: Python 3.10+, pandas, numpy, statsmodels 0.14 or later.
Run: python3 ch09_forecast.py   (with sales.csv in the same folder)
"""
import numpy as np, pandas as pd
from statsmodels.tsa.exponential_smoothing.ets import ETSModel

s = pd.read_csv("sales.csv")
y = s.groupby(s.OrderDate.str[:7]).NetSales.sum()
y.index = pd.date_range("2024-01-01", periods=len(y), freq="MS")
fit = ETSModel(y, error="add", trend="add", seasonal="mul", seasonal_periods=12).fit(disp=False)
mean = fit.forecast(12)
errors = np.random.default_rng(2026).normal(0, np.sqrt(fit.mse), size=(12, 20000))
sims = fit.simulate(nsimulations=12, repetitions=20000, anchor="end", random_errors=errors)
totals = sims.sum(axis=0)
lo, hi = np.percentile(totals, [2.5, 97.5])
print(f"2026 point forecast: ${mean.sum():,.0f}")
print(f"2026 95% range (simulated annual totals): ${lo:,.0f} to ${hi:,.0f}")
print("Monthly point forecasts:")
for d, v in mean.items():
    print(f"  {d:%b %Y}: ${v:,.0f}")
