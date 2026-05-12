# import sys
# import os
import matplotlib.pyplot as plt
# sys.path.insert(
#     0,
#     os.path.abspath(
#         os.path.join(os.path.dirname(__file__), '../ex00')
#     )
# )
from load_csv import load


def main():
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("../ex00/life_expectancy_years.csv")
    if gdp_df is None or life_df is None:
        print("Failed to load one or both CSV files.")
        return

    gdp_df['country'] = gdp_df['country'].astype(str).str.strip().str.lower()
    life_df['country'] = life_df['country'].astype(str).str.strip().str.lower()

    common_countries = set(gdp_df['country']).intersection(life_df['country'])
    x_gdp = []
    y_life = []
    labels = []
    for country in common_countries:
        gdp_row = gdp_df[gdp_df['country'] == country]
        life_row = life_df[life_df['country'] == country]
        if gdp_row.empty or life_row.empty:
            continue
        gdp_val = gdp_row['1900'].values[0]
        life_val = life_row['1900'].values[0]
        # Convert GDP to float (handle k/M/B)

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
        gdp_val = parse_number(gdp_val)
        life_val = parse_number(life_val)
        if (
            not (gdp_val and life_val)
            or gdp_val != gdp_val
            or life_val != life_val
        ):
            continue
        x_gdp.append(gdp_val)
        y_life.append(life_val)
#        labels.append(country.title())

    print(f"Plotting {len(x_gdp)} countries for year 1900.")
    if len(x_gdp) == 0:
        print(
            "No data to plot. Check your CSV files for valid 1900 data."
        )
        return
    plt.figure(figsize=(12, 7))
    plt.scatter(x_gdp, y_life, alpha=0.7)
    plt.title("Life Expectancy vs GDP per Capita (1900)")
    plt.xlabel("GDP per Capita (PPP, inflation adjusted, 1900)")
    plt.ylabel("Life Expectancy (1900)")
    plt.xscale('log')
    plt.xlim(300, 10000)
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])  # Custom ticks
    for i, label in enumerate(labels):
        if i % 15 == 0:
            plt.annotate(
                label,
                (x_gdp[i], y_life[i])
            )
#    plt.grid(True)
    plt.tight_layout()
    print("Displaying plot window...")
    plt.show()


if __name__ == "__main__":
    main()


# common_countries 是一个集合，包含两个数据集中都存在的国家名 遍历顺序是随机的
# 只给每第十五个个国家标注但是因为common_countries的长度可能不是15的倍数，所以会有些国家没有标注
# 可以在set前就行sorted这样就可以排序好顺序就固定了
