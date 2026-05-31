# commercial-analytics-case-study

Commercial analytics case studies using public datasets to demonstrate business question framing, hypothesis validation, data storytelling, and decision support.

## Case 001: Regional Smoking Behavior Analysis (Japan)

This case study investigates how smoking behavior changed across Japanese prefectures between 2012 and 2016 using official public health data.

The objective is to demonstrate a commercial analytics workflow from business question definition to insight generation and decision support.

---

## Business Question

Are consumer behavioral transitions occurring uniformly across Japan, or do significant regional differences exist in the pace of change?

---

## Data Source

* Ministry of Health, Labour and Welfare (厚生労働省)
* National Health and Nutrition Survey
* 2012 (平成24年) Prefecture-Level Smoking Statistics
* 2016 (平成28年) Prefecture-Level Smoking Statistics

---

## Key Findings

* National smoking rates generally declined between 2012 and 2016.
* Regional variation exceeded 15 percentage points.
* Gifu (-11.6pp), Okayama (-10.9pp), and Fukuoka (-10.0pp) experienced the largest declines.
* Gunma (+4.3pp), Yamanashi (+4.0pp), and Fukui (+3.4pp) showed increases despite the overall national decline.
* The strongest decline and strongest increase moved in opposite directions, highlighting substantial regional variation in consumer behavior.

---

## Business Implication

Consumer transition speed differs substantially across regions.

The gap between the strongest decline and strongest increase exceeded 15 percentage points.

This suggests that national averages may conceal meaningful local market dynamics.

Regional portfolio allocation, consumer engagement strategy, and marketing investment should be evaluated at the prefecture level rather than relying solely on national trends.

A one-size-fits-all commercial strategy may systematically underserve high-opportunity regions.

---

## Charts

### Top Smoking Rate Decline

![Decline](cases/case_001_regional_demand_analysis/charts/top_decline.png)

### Top Smoking Rate Increase

![Increase](cases/case_001_regional_demand_analysis/charts/top_increase.png)

---

## Analytics Workflow

Business Question

↓

Official Data Collection

↓

Data Cleaning & Validation

↓

Exploratory Analysis

↓

Insight Generation

↓

Business Implication

↓

Decision Support

---

## Repository Structure

```text
cases/
└── case_001_regional_demand_analysis/
    ├── raw_data/
    ├── processed_data/
    ├── charts/
    ├── scripts/
    └── notes/
```

---

## Skills Demonstrated

* Commercial Analytics
* Business Question Framing
* Hypothesis Development
* Data Cleaning
* Data Validation
* Exploratory Data Analysis (EDA)
* Data Storytelling
* Insight Generation
* Decision Support
* Python
* Pandas
* Data Visualization
