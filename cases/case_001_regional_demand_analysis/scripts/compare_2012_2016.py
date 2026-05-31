import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------

df_2012 = pd.read_csv(
    "cases/case_001_regional_demand_analysis/data/processed/smoking_rate_prefecture_2012_clean.csv"
)

df_2016 = pd.read_csv(
    "cases/case_001_regional_demand_analysis/data/processed/smoking_rate_prefecture_2016_clean.csv"
)

# -----------------------------
# Merge & Calculate Change
# -----------------------------

comparison = df_2012.merge(
    df_2016,
    on="prefecture",
    suffixes=("_2012", "_2016")
)

comparison["change"] = (
    comparison["smoking_rate_2016"]
    - comparison["smoking_rate_2012"]
)

# -----------------------------
# Analysis Output
# -----------------------------

print("\n" + "=" * 60)
print("Top Decline (2012 → 2016)")
print("=" * 60)

print(
    comparison[
        [
            "prefecture",
            "smoking_rate_2012",
            "smoking_rate_2016",
            "change"
        ]
    ]
    .sort_values("change")
    .head(10)
)

print("\n" + "=" * 60)
print("Top Increase (2012 → 2016)")
print("=" * 60)

print(
    comparison[
        [
            "prefecture",
            "smoking_rate_2012",
            "smoking_rate_2016",
            "change"
        ]
    ]
    .sort_values("change", ascending=False)
    .head(10)
)

print("\n" + "=" * 60)
print("Highest Smoking Regions (2016)")
print("=" * 60)

print(
    df_2016[
        [
            "prefecture",
            "smoking_rate"
        ]
    ]
    .sort_values(
        "smoking_rate",
        ascending=False
    )
    .head(10)
)

# -----------------------------
# Create Chart 1
# Top Decline
# -----------------------------

top_decline = (
    comparison[
        [
            "prefecture",
            "change"
        ]
    ]
    .sort_values("change")
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_decline["prefecture"],
    abs(top_decline["change"])
)

plt.title(
    "Top 10 Smoking Rate Decline (2012-2016)"
)

plt.xlabel(
    "Percentage Point Change"
)

plt.tight_layout()

plt.savefig(
    "cases/case_001_regional_demand_analysis/charts/top_decline.png"
)

plt.close()

# -----------------------------
# Create Chart 2
# Top Increase
# -----------------------------

top_increase = (
    comparison[
        [
            "prefecture",
            "change"
        ]
    ]
    .sort_values(
        "change",
        ascending=False
    )
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_increase["prefecture"],
    top_increase["change"]
)

plt.title(
    "Top 10 Smoking Rate Increase (2012-2016)"
)

plt.xlabel(
    "Percentage Point Change"
)

plt.tight_layout()

plt.savefig(
    "cases/case_001_regional_demand_analysis/charts/top_increase.png"
)

plt.close()

print("\nCharts generated successfully:")
print(
    "cases/case_001_regional_demand_analysis/charts/top_decline.png"
)
print(
    "cases/case_001_regional_demand_analysis/charts/top_increase.png"
)