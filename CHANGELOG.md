# Changelog

All notable changes to the companion files are listed here. Version numbers follow the pattern MAJOR.MINOR.PATCH: a new PATCH or MINOR version fixes or adds files for the same edition of the book; a new MAJOR version would go with a new edition.

The latest release is always at https://github.com/emmanuelauthor/demystifying-data-analytics/releases/latest

## [1.1.0] - 2026-10-10

Updated answer workbook, to match the final text of the first edition. The data files are unchanged.

### Changed

- `answers/CedarLane_Answers.xlsx`, sheet **Ch15 Scenarios**: rebuilt to the book's final scenario model.
  - Refunds follow the price paid. The Option A model now starts from the discount on kept lines ($350,344). Row 10 shows +$115,432, +$214,172 and +$271,748.
  - The Goal Seek break-evens are 54.1% (base) and 44.0% (cautious). The Data Table check (H10) is $165,587.
  - Option B uses change = (1 - share lost) x S - share lost x P. It gives +$7,049, +$10,454 and +$12,838, with a 45.7% break-even (Exercise 2(c), new cell G20).
  - Table 15.3 is the joint model: +$451,483 before costs, $9,791 more than the simple sum, and +$384,643 after costs.
- `answers/CedarLane_Answers.xlsx`, sheet **Ch09 Cohort**: matches the book's formula route for Excel for Mac and the web.
  - Grid 1 (counts, A1:I9) leaves quarters after December 2025 blank, meaning not observed.
  - Grid 2 (percentages, K1:R9) uses `=IF(B2="","",B2/$B2)`.
  - The repeat-customer cells moved to A12:B13.
- The **Checks** sheet now lists 783 values, all reproduced.
- The package version on the README sheets of both workbooks is now 1.1.0.

## [1.0.0] - 2026-10-09

Initial release, for the first edition of *Demystifying Data Analytics* (2026).

### Included

- `data/CedarLane_Practice.xlsx`: practice workbook (README, Sales, Products, Customers, Stores, Returns, WebFunnel, Marketing, ABTest, DataDictionary). The README sheet gives the address of the latest files and the package version.
- `data/` CSV files: sales (82,167 rows), products (60), customers (24,405), stores (9), returns (2,634), web_funnel (24), marketing (96), ab_test (2).
- `data/store_export_aug2025_messy.csv`: the messy store export for Chapter 6 (1,066 raw rows; 1,043 after cleaning).
- `data/cedar_lane.db`: SQLite database with the same eight tables.
- `answers/CedarLane_Answers.xlsx`: completed reference workbook with one or more sheets per chapter that has hands-on work, laid out cell by cell as the book describes, and a Checks sheet listing every "Check your result" value with the cell that reproduces it.
- `scripts/ch09_forecast.py` and `scripts/README.md`: optional Python script for the Chapter 9 forecast (point forecast $9,290,566; range $8,613,233 to $9,967,947).
- `README.md`, `README.txt`, `LICENSE` (CC BY 4.0 for data, workbooks and documentation; MIT for the script), `VERSION`, `MANIFEST-SHA256.txt`.
