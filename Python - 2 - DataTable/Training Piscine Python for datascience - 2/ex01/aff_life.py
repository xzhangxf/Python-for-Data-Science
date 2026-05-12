import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    if df is None:
        print("Failed to load life_expectancy_years.csv")
        return

    country = "Singapore"
    row = df[df['country'] == country]
    if row.empty:
        print(f"Country '{country}' not found in dataset.")
        return

    print(f"\nData for {country}:")
    print(row.to_string(index=False))

    years = [int(col) for col in df.columns if col != 'country']
    values = row.iloc[0, 1:].values.astype(float)

    plt.figure(figsize=(10, 5))
    plt.plot(years, values, label=country)
    plt.title(f"Life Expectancy in {country} Over Time")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
