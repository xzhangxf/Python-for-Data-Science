import sys
import os
import matplotlib.pyplot as plt

# Add ex00 to sys.path to import load
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../ex00')
    )
)
from ex03.load_csv import load  # noqa: E402


def main():
    # Load the dataset
    df = load("population_total.csv")
    if df is None:
        print("Failed to load population_total.csv")
        return

    countries = ["Singapore", "Japan"]
    data = {}
    # Normalize country names in the DataFrame for robust matching
    df['country'] = df['country'].astype(str).str.strip().str.lower()
    for country in countries:
        country_norm = country.strip().lower()
        row = df[df['country'] == country_norm]
        if row.empty:
            print(f"Country '{country}' not found in dataset.")
            print("Available countries:")
            print(sorted(df['country'].unique()))
            return
        # Only keep years 1800-2050
        years = [
            int(col) for col in df.columns
            if col != 'country' and 1800 <= int(col) <= 2050
        ]
        raw_values = row.iloc[0][[str(year) for year in years]].values

        def parse_number(val):
            val = str(val).strip()
            if val.endswith('k'):
                return float(val[:-1]) * 1_000
            elif val.endswith('M'):
                return float(val[:-1]) * 1_000_000
            elif val.endswith('B'):
                return float(val[:-1]) * 1_000_000_000
            try:
                return float(val)
            except Exception:
                return float('nan')

        values = [parse_number(v) for v in raw_values]
        # Convert to millions
        values_millions = [v / 1_000_000 for v in values]
        data[country] = (years, values_millions)

    # Plot
    plt.figure(figsize=(12, 6))
    for country in countries:
        years, values = data[country]
        plt.plot(years, values, label=country)
    plt.title("Population Comparison: Singapore vs Japan (1800-2050)")
    plt.xlabel("Year")
    plt.ylabel("Population (millions)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
