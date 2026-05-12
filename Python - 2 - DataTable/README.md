# Python - 2 - DataTable

This module introduces CSV/table loading and visualization using pandas and matplotlib with Gapminder-based datasets.

## Module Overview

What this module teaches:

- Loading tabular datasets from CSV
- Handling file/parse errors gracefully
- Extracting country/year slices
- Building line and scatter visualizations
- Converting compact number formats (`k`, `M`, `B`)

How it connects to repository flow:

- Extends array manipulation into real tabular analytics
- Bridges data preparation and visual storytelling

Prerequisites:

- Python basics and arrays
- Basic plotting understanding is helpful

## Learning Goals

- Write reusable CSV loader functions
- Manipulate DataFrame rows/columns safely
- Build clear comparison graphs
- Handle missing/invalid data robustly
- Explore relationship between GDP and life expectancy

## Folder Structure

```text
Python - 2 - DataTable/
├── en.subject.pdf
├── venvrun.txt
└── Training Piscine Python for datascience - 2/
    ├── ex00/load_csv.py, test_load.py, life_expectancy_year.csv, life_expectancy_years.csv
    ├── ex01/load_csv.py, aff_life.py, life_expectancy_years.csv
    ├── ex02/aff_pop.py, population_total.csv
    └── ex03/load_csv.py, projection_life.py, income_per_person_gdppercapita_ppp_inflation_adjusted.csv
```

| File / Folder | Purpose |
|---|---|
| ex00 | Base CSV loading utility with error handling |
| ex01 | Plot life expectancy for one target country |
| ex02 | Compare population between two countries |
| ex03 | Scatter GDP vs life expectancy for year 1900 |
| venvrun.txt | Environment activation note |

## Exercise-by-Exercise Explanation

### ex00 - load_csv.py (+ test_load.py)

**Path:** `Training Piscine Python for datascience - 2/ex00/load_csv.py`
**Purpose:** Generic dataset loader.
**Important Function:** `load(path: str)` returns DataFrame or `None`.
**Input:** CSV path string.
**Output:** DataFrame + printed dimensions.
**Main Logic:** `pd.read_csv` with exception handling branches.
**How to Run:**
```bash
cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex00"
python3 test_load.py
```
**Verification Note:** `test_load.py` currently imports `from ex03.load_csv import load` and fails with `ModuleNotFoundError` when run directly. **This part should be verified.**
**What I Learned:** Reusable data loader and failure-safe design.

### ex01 - aff_life.py (+ load_csv.py)

**Path:** `.../ex01/aff_life.py`
**Purpose:** Plot life expectancy over time for one country (configured as Singapore).
**Important Functions:** `load`, `main`.
**Input:** `life_expectancy_years.csv`.
**Output:** Country row print + line chart.
**Main Logic:** Load -> filter by country -> parse year columns -> plot values.
**How to Run:**
```bash
cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex01"
python3 aff_life.py
```
**What I Learned:** Row filtering and time-series plotting.

### ex02 - aff_pop.py

**Path:** `.../ex02/aff_pop.py`
**Purpose:** Compare population curves for Singapore and Japan (1800-2050).
**Important Logic:** Country normalization + suffix parsing (`k`, `M`, `B`) + million scaling.
**Input:** `population_total.csv`.
**Output:** Dual-line population chart with legends.
**How to Run:**
```bash
cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex02"
python3 aff_pop.py
```
**Verification Note:** Import path manipulation + `from ex03.load_csv import load` in this exercise is unusual for module structure. **This part should be verified.**
**What I Learned:** Practical data cleaning for plotting.

### ex03 - projection_life.py (+ load_csv.py)

**Path:** `.../ex03/projection_life.py`
**Purpose:** Plot life expectancy vs GDP per capita for year 1900.
**Important Functions:** Local `parse_number` converter, scatter plotting with log x-axis.
**Input:** GDP CSV + life expectancy CSV.
**Output:** Scatter plot over common countries.
**Main Logic:** Normalize country keys -> intersect countries -> parse 1900 values -> skip invalids -> scatter.
**How to Run:**
```bash
cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex03"
python3 projection_life.py
```
**What I Learned:** Multi-dataset alignment and correlation-style plotting.

## Important Concepts

- pandas DataFrames (`read_csv`, filtering, column selection)
- Data normalization (`strip`, lowercase keys)
- Numeric suffix parsing (`k`/`M`/`B`)
- matplotlib line and scatter charts
- Log-scaled axis for GDP-like values

## Data / Control Flow

```text
CSV files
  ↓
load(path) with pandas
  ↓
clean/filter/select country/year data
  ↓
convert values to numeric form
  ↓
plot (line/scatter) with labels/axes
```

## Common Errors / Edge Cases

| Case | Where It Is Handled | Behavior |
|---|---|---|
| Missing file | `load_csv.py` | Prints file error, returns `None` |
| Empty/bad CSV | `load_csv.py` | Prints parser/empty-data error |
| Country not found | `aff_life.py`, `aff_pop.py` | Prints clear message and exits |
| Non-numeric compact values | `aff_pop.py`, `projection_life.py` | Parses or converts to `nan` |
| No usable plotting points | `projection_life.py` | Prints “No data to plot” and exits |

## How to Test This Module

| Test | Command | Expected Result |
|---|---|---|
| Life expectancy plot | `cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex01" && python3 aff_life.py` | Loads dataset and shows country trend plot |
| Population comparison | `cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex02" && python3 aff_pop.py` | Two-country line chart for 1800-2050 |
| GDP vs life projection | `cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex03" && python3 projection_life.py` | Scatter chart with log x-axis |
| Loader test script | `cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex00" && python3 test_load.py` | Currently raises import error; verify import target |

## Key Takeaways

- Data loading should be reusable and error-tolerant.
- Visualization quality depends on cleaning and conversion steps.
- Joining datasets by consistent keys is essential.
- Correlation plots require thoughtful axis scaling.
