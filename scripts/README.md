# scripts/ch09_forecast.py

An optional Python script that reproduces the illustrative 2026 net sales forecast in Chapter 9 (Figure 9.8). **You do not need it, or Python, for anything in the book.** Excel readers can use the Forecast Try It in Chapter 9 instead.

## What it does

It adds up net sales by month from `sales.csv` (24 months, January 2024 to December 2025) and fits an exponential smoothing model (statsmodels `ETSModel`: additive error, additive trend, multiplicative seasonality, 12-month season). It then:

- sums the model's twelve monthly forecasts for 2026 to get the point forecast, and
- simulates 20,000 possible versions of 2026 (with a fixed random seed, so the result is repeatable), sums each one, and reports the middle 95 percent of those annual totals as the range.

## What you need

- Python 3.10 or later
- pandas
- numpy
- statsmodels 0.14 or later

Install the three libraries once, from a terminal (Command Prompt or PowerShell on Windows, Terminal on a Mac):

```
python -m pip install pandas numpy statsmodels
```

On a Mac, type `python3` instead of `python` in the commands on this page.

## How to run it

The script reads `sales.csv` from the folder you run it in, so run it from the **data** folder:

1. Open a terminal.
2. Go to the `data` folder inside the unzipped companion files. For example, on Windows:
   ```
   cd "%USERPROFILE%\Documents\CedarLane\data"
   ```
   or on a Mac:
   ```
   cd ~/Documents/CedarLane/data
   ```
   (Adjust the path to wherever you unzipped the files.)
3. Run the script from the neighboring `scripts` folder:
   ```
   python ../scripts/ch09_forecast.py
   ```

It takes a few seconds.

## Expected output

```
2026 point forecast: $9,290,566
2026 95% range (simulated annual totals): $8,613,233 to $9,967,947
Monthly point forecasts:
  Jan 2026: $480,598
  Feb 2026: $464,707
  Mar 2026: $700,363
  Apr 2026: $778,431
  May 2026: $863,722
  Jun 2026: $737,554
  Jul 2026: $718,809
  Aug 2026: $715,803
  Sep 2026: $703,217
  Oct 2026: $806,126
  Nov 2026: $1,068,425
  Dec 2026: $1,252,811
```

The two lines that matter are the point forecast, **$9,290,566**, and the range, **$8,613,233 to $9,967,947**: the numbers quoted in Chapter 9.

## If something goes wrong

- **`FileNotFoundError: sales.csv`**: you are not in the `data` folder. Repeat step 2.
- **`ModuleNotFoundError: No module named 'statsmodels'`** (or pandas, numpy): install the libraries as shown above.
- **`python` is not recognized**: Python is not installed, or not on your PATH. Install it from python.org (on Windows, tick **Add python.exe to PATH** in the installer), or try `py` instead of `python`.
- **Slightly different numbers**: very old or very new library versions can change the fitted model in the last digits. The book's numbers were produced with statsmodels 0.14 or later; a forecast is an estimate, so small differences do not matter.

## License

The script is released under the MIT License (see `LICENSE` in the main folder). The data it reads is licensed under CC BY 4.0.
