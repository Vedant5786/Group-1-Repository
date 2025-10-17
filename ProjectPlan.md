# IS477 Milestone 2 – Project Plan

**Project Title:** Exploring the Relationship Between Unemployment and Consumer Spending in the United States  
**Team Members:** Vedant Patel and Alex Vasilevich

## 1. Overview
Economic fluctuations which play into play consumer confidence, purchasing behavior and total financial health. At times of high unemployment we see individual consumers reduce what they spend on non-essential items, put off large purchases and in fact turn to basic products. In contrast when employment is strong we see spending go up which in turn stimulates business growth and GDP growth. That which plays into the relationship between unemployment and consumer spending is what economists, policymakers and businesses pay attention to as they try to predict market trends and develop proper economic policies.

This project we set out to do is to put a number to and present how changes in unemployment rates play out in terms of consumer spending over time and across geographies. We will be working with two different public data sets  the Federal Reserve Economic Data (FRED) API and a Kaggle U.S. Consumer Spending dataset to present a unified picture of the labor market and household expenditure. The integration of these data sets will also allow us to look at trends over time and at the same which regions are affected  for example we will look at how the COVID-19 pandemic or recessions played out in terms of their impact on spending as compared to instances of large scale unemployment.

From the perspective of IS477 this project will present the full data life cycle which includes acquisition, integration, cleaning, storage and analysis at the same time we will focus on ethical issues related to data use, reproducibility of results, and open communication of our methods. At project end we aim to present interpretive visualizations and to report based on evidence which shows how variations in employment conditions play out in terms of consumer behavior.


## 2. Research Questions
Our research will focus on the following key research questions:

1. **How does the unemployment rate correlate with consumer spending trends over time?**  
   We will test whether rising unemployment is consistently associated with declines in overall consumer spending and whether this relationship varies across economic cycles such as the 2008 financial crisis and the COVID-19 pandemic.

2. **Are there regional or demographic differences in how unemployment affects spending behavior?**  
   Using available geographic information in our datasets, we will explore whether states or regions with historically higher unemployment show distinct consumption trends compared to areas with lower unemployment rates.

3. **Can changes in consumer spending serve as an early indicator of labor market recovery or decline?**  
   By analyzing lagged correlations, we aim to evaluate whether spending patterns can predict upcoming improvements or deteriorations in unemployment rates.


## 3. Team

This project is a collaborative effort between **Vedant Patel** and **Alex Vasilevich**. Both members will contribute to code development, documentation, and version control through the shared GitHub repository.

| **Vedant Patel**: *Data Acquisition & Integration Lead* - Responsible for identifying, retrieving, and integrating data from the Federal Reserve Economic Data (FRED) API and Kaggle datasets. Vedant will handle data collection scripts, schema alignment, merging, and initial quality checks.
| **Alex Vasilevich**: *Analysis & Documentation Lead* - Responsible for exploratory data analysis, visualization, and results interpretation. Will prepare Markdown documentation, coordinate milestone deliverables, and ensure workflow reproducibility and proper citation of datasets.


## 4. Datasets

### Dataset 1: U.S. Unemployment Rate (UNRATE)
The UNRATE dataset represents the monthly unemployment rate for all civilian workers aged 16 and older in the United States. It measures the percentage of individuals who are unemployed but actively seeking employment and is seasonally adjusted to remove fluctuations due to recurring seasonal patterns. The data, reported by the **U.S. Bureau of Labor Statistics (BLS)** and hosted on FRED, extends from 1948 to the present. Access will be handled through the FRED API using the `requests` library in Python, with results returned in CSV or JSON format. This dataset provides the foundational labor market indicator necessary to analyze macroeconomic changes over time.

### Dataset 2: Personal Consumption Expenditures (PCE)
The **PCE** dataset measures the total value of goods and services purchased by U.S. households each month, expressed in billions of dollars and adjusted for seasonality. It serves as one of the most comprehensive indicators of consumer spending behavior, reflecting household consumption trends across durable and nondurable goods as well as services. The PCE data, maintained by the **U.S. Bureau of Economic Analysis (BEA)** and published via FRED, will be retrieved using the same API and time range as the unemployment data to ensure perfect temporal alignment.

### Integration Strategy
Both datasets include a **monthly date variable**, which will serve as the primary key for merging. Data cleaning will involve standardizing date formats, handling missing values, and ensuring consistent time ranges. This integration will enable a time-series analysis comparing monthly changes in unemployment with shifts in consumer spending.


## 5. Timeline
| Step | Phase / Task | Description | Responsible Member(s) |
|------|---------------|--------------|-----------------------|
| **Step 1** | **Project Planning** | Finalize and submit the complete ProjectPlan.md document for Milestone 2. | Both |
| **Step 2** | **Data Acquisition** | Retrieve datasets from the FRED API and Kaggle. Document sources, access parameters, and metadata for reproducibility. | Vedant |
| **Step 3** | **Data Cleaning and Integration** | Align the two datasets by time period, standardize variable names and formats, and merge them on matching date keys. | Vedant |
| **Step 4** | **Exploratory Data Analysis (EDA)** | Generate descriptive statistics, identify trends, and visualize patterns between unemployment and spending behavior. | Alex Vasilevich |
| **Step 5** | **Modeling and Trend Analysis** | Conduct regression or time-series modeling to quantify relationships between unemployment rates and spending. | Both |
| **Step 6** | **Visualization Development** | Create final visualizations and charts summarizing findings for inclusion in the report and presentation. | Alex Vasilevich |
| **Step 7** | **Report Compilation and Review** | Prepare the final project report, validate all scripts, verify reproducibility, and ensure clarity of insights. | Both |


## 6. Constraints

Key constraints and limitations identified for this project include:

- **API limits:** FRED restricts the number of data requests per minute, requiring efficient retrieval.  
- **Granularity:** Monthly data may miss short-term fluctuations in spending or employment.  
- **Scope:** Both datasets are aggregated at the national level, limiting regional or demographic insights.  
- **Inflation effects:** PCE values may require inflation adjustment to maintain comparability over time.  
- **External shocks:** Events such as recessions or pandemics can introduce irregular patterns in the data.

These factors will be considered during analysis and discussed in the final report.

## 7. Gaps

Although the project plan outlines a clear direction, a few elements remain to be finalized:

- **Time range selection:** The specific analysis period (e.g., 2000–2024) will be confirmed after data inspection.  
- **Inflation adjustment method:** The team will decide whether to use CPI or another index for real-dollar conversion.  
- **Analytical approach:** The choice between regression and correlation analysis will depend on observed data trends.  
- **Visualization tools:** Final selection between Python libraries (Matplotlib, Seaborn, or Plotly) remains open.