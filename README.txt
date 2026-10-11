DEMYSTIFYING DATA ANALYTICS: COMPANION FILES
============================================

Free practice files for the book Demystifying Data Analytics: Data Analysis,
Visualization and AI-Assisted Insights for Beginners and Business
Professionals by Emmanuel K. Okunola.

For the first edition, 2026. Package version 1.1.0.

These are the files you need to follow along with Maya and the Cedar & Lane
Home Goods case in the book: the practice workbook, the data as CSV files, a
SQLite database, a deliberately messy file for the cleaning chapter, a
completed answer workbook, and an optional Python script.

You do not need a GitHub account. Reading this page and downloading the files
are free and need no sign-up.

HOW TO DOWNLOAD
---------------

Option 1 (recommended): download the release ZIP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Go to the latest release:
     https://github.com/emmanuelauthor/demystifying-data-analytics/releases/latest
       (Or, on this page, click Releases in the right-hand column on a
       computer, or near the bottom of the page on a phone, then open the
       latest release.)
  2. Under Assets, click CedarLane_Companion_Files_v1.1.0.zip. Your browser
     downloads it, usually to your Downloads folder.

Option 2: download everything from this page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Near the top of this page, click the green Code button.
  2. Click Download ZIP.

Both options give you the same files. The release ZIP in Option 1 is named for
its version, so you always know which version you have.

Unzip the files (important)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the files from the unzipped folder, not from inside the ZIP. A file
opened straight from a ZIP is a temporary read-only copy, and your work can be
lost when you close it.

  * Windows: open your Downloads folder, right-click the ZIP, choose Extract
    All, pick a folder you will remember (such as Documents\CedarLane), and
    click Extract.
  * Mac: double-click the ZIP in Downloads. A new folder appears next to it;
    drag that folder to Documents.

Then make a working copy of CedarLane_Practice.xlsx (for example,
CedarLane_MyWork.xlsx) and do every Try It in the copy. Keep the original
untouched so you can always start again.

WHAT IS IN THE PACKAGE
----------------------

  * data/CedarLane_Practice.xlsx
      What it is: The main practice workbook: a README sheet, one sheet per
      table (Sales, Products, Customers, Stores, Returns, WebFunnel,
      Marketing, ABTest) and a DataDictionary sheet. Headers in row 1, data
      from row 2, plain ranges (you turn them into tables in Chapter 4).
      Used in: Chapters 1 to 4, 7 to 13 and 15, and the Chapter 16 capstone
  * answers/CedarLane_Answers.xlsx
      What it is: Completed reference answers for the Try Its and hands-on
      exercises, laid out cell by cell as the book describes, plus a Checks
      sheet listing every "Check your result" value. Open it after you have
      tried each task.
      Used in: Every chapter with hands-on work (2 to 16)
  * data/sales.csv
      What it is: One row per order line: 82,167 rows, January 1, 2024 to
      December 31, 2025.
      Used in: Chapters 3, 4, 9 (Python script), 12, 16
  * data/products.csv
      What it is: The 60 products, with category, list price, unit cost and
      collection.
      Used in: Chapters 3, 4, 12, 16
  * data/customers.csv
      What it is: 24,405 customers, with fictional names and example.com email
      addresses.
      Used in: Chapters 3, 14, 16
  * data/stores.csv
      What it is: The eight stores plus the online store (9 rows).
      Used in: Chapters 3, 12, 16
  * data/returns.csv
      What it is: 2,634 returned order lines, with reason and refund amount.
      Used in: Chapters 3, 4, 8, 12, 16
  * data/web_funnel.csv
      What it is: Monthly website sessions, product views, carts, checkouts
      and orders.
      Used in: Chapters 3, 9, 16
  * data/marketing.csv
      What it is: Monthly marketing spend by channel (96 rows).
      Used in: Chapters 3, 6, 7, 16
  * data/ab_test.csv
      What it is: Results of the checkout redesign A/B test (2 rows).
      Used in: Chapters 3, 9, 16
  * data/store_export_aug2025_messy.csv
      What it is: A deliberately messy store export to clean (1,066 raw rows).
      Used in: Chapter 6, and the Chapter 16 capstone
  * data/cedar_lane.db
      What it is: A SQLite database with all eight tables, for SQL.
      Used in: Chapter 5, the SQL examples in Chapters 6, 7, 9, 13, 14 and 15,
      and Chapter 16
  * scripts/ch09_forecast.py
      What it is: Optional Python script that reproduces the Chapter 9
      forecast. You do not need it, or Python, for anything in the book. See
      scripts/README.md.
      Used in: Chapter 9 (optional)
  * README.md, README.txt
      What it is: This guide (README.txt is the same text, for opening in
      Notepad or TextEdit).
  * LICENSE
      What it is: The license terms (summary below).
  * CHANGELOG.md, VERSION
      What it is: What changed in each version, and the version number.
  * MANIFEST-SHA256.txt
      What it is: A fingerprint (SHA-256 checksum) of every file, so you can
      confirm a download is complete and unchanged.

The data is fictional but realistic: 82,167 order lines from January 1, 2024
through December 31, 2025. A quick check that you have the right file: open
CedarLane_Practice.xlsx, click the Sales tab, click cell A1 and press
Ctrl+Down Arrow (Cmd+Down Arrow on a Mac). You should land on row 82,168,
OrderLineID 82167.

SOFTWARE YOU NEED
-----------------

  * Microsoft 365 Excel (Windows or Mac) for the workbooks and CSV files.
    Excel for the web handles most early chapters. A few functions (XLOOKUP,
    UNIQUE, FILTER, LET, GROUPBY) need a current Microsoft 365 version.
  * Power BI Desktop, free from Microsoft, Windows only, for Chapter 12.
    Chapter 12 ends with an Excel version of the dashboard for Mac users.
  * DB Browser for SQLite, free for Windows, Mac and Linux
    (sqlitebrowser.org), for cedar_lane.db in Chapter 5.
  * Python is optional, only for scripts/ch09_forecast.py.
  * Any AI assistant for the AI Assist boxes.

TROUBLESHOOTING
---------------

Excel shows a yellow "Protected View" bar. Files downloaded from the internet
open read-only at first. Click Enable Editing. The files contain no macros. If
the bar appears every time you open a file, right-click the file in File
Explorer, choose Properties, tick Unblock at the bottom of the General tab,
and click OK.

Dates or leading zeros change when I double-click a CSV file. Excel guesses
each column's type when it opens a CSV directly, and it can turn text into
dates or numbers. Use Data > Get Data > From File > From Text/CSV instead
(Chapter 4 shows how), or use CedarLane_Practice.xlsx, which already has the
right types.

The workbook is slow to open or scroll. The Sales sheet has 82,167 rows, and
the answer workbook also recalculates thousands of formulas when it opens.
Give it a minute, close other large files, and use the desktop Excel app
rather than Excel for the web for the answer workbook.

DB Browser says "database is locked". Another program, or a second DB Browser
window, has the database open. Close the other window (or click Close Database
first) and open it again. Never open cedar_lane.db from inside the ZIP; unzip
it first. The book only reads data, so you never need Write Changes.

I use a Mac and cannot install Power BI Desktop. Power BI Desktop runs only on
Windows. Use the Excel version of the dashboard at the end of Chapter 12, or a
Windows computer, virtual machine or cloud PC if you have one. Every other
chapter works on a Mac.

My browser or antivirus blocks the ZIP download. Try another browser first; a
browser extension or an office network setting is the usual cause. In your
browser's downloads list, choose Keep if it asks. Work or school networks
sometimes block ZIP files; try from a home network, or use Option 2 above. You
can confirm the download is complete with the checksums in
MANIFEST-SHA256.txt.

The ZIP will not open, or it stops partway. The download was probably cut
short. Delete it and download again from the latest release.

I changed a practice file and want a clean copy. Download the ZIP again from
the latest release and unzip it into a new folder. To avoid this, keep the
original files untouched and work in a copy (for example,
CedarLane_MyWork.xlsx).

My answer does not match the book. Compare with
answers/CedarLane_Answers.xlsx. Its Checks sheet lists every "Check your
result" value and the cell that reproduces it. The usual culprits are a filter
you forgot was on, a formula dragged sideways instead of copied, or a missing
helper column.

How do I know which version I have? The VERSION file and the README sheet of
each workbook state the package version. Version 1.1.0 matches the first
edition (2026). CHANGELOG.md lists what changed in each version.

LICENSE (SUMMARY)
-----------------

  * Data, workbooks and documentation: Creative Commons Attribution 4.0
    International (CC BY 4.0) (https://creativecommons.org/licenses/by/4.0/).
    You may use, share and adapt them for any purpose, including practice work
    and public portfolio projects, as long as you give credit. Suggested
    credit line: Data from Demystifying Data Analytics by Emmanuel K. Okunola.
  * The Python script (scripts/ch09_forecast.py): MIT License.

The book itself is not covered by these licenses. See LICENSE for the full
terms.

ABOUT THE DATA
--------------

Cedar & Lane Home Goods, its stores, its staff and its customers are
fictional. All names, email addresses (example.com) and numbers were generated
for teaching and do not describe any real company or person. The data behaves
like a real retailer's, with seasonal peaks, returns, promotions and a few
surprises, so you can practice on something that feels real.

REPORT A PROBLEM
----------------

Found a broken link, a file that will not open, or a number that does not
match the book? Open an issue at
https://github.com/emmanuelauthor/demystifying-data-analytics/issues and
include the file name, the chapter, and what you expected to see.

Opening an issue requires a free GitHub account. Reading this page and
downloading the files do not.

Corrections are published as new versions (see CHANGELOG.md). The link above
to the latest release always points to the newest version.
