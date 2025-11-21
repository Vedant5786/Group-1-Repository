# IS477 Milestone 3 – Interim Status Report

**Project Title:** Exploring the Relationship Between Unemployment and Consumer Spending in the United States

**Team Members:** Vedant Patel and Alex Vasilevich

**Date:** [Current Date]

**GitHub Release Tag:** status-report

## 1. Project Progress Update

### Task Update: Data Acquisition (Step 2)
* Status: Completed
* Lead: Vedant
* Artifacts & Progress: I successfully set up the data acquisition part of our project. I created a Python script called data_acquisition.py that pulls data from the FRED API for both the unemployment rate and consumer spending data.
* The script uses an environment variable to keep our API key secure and downloads data from 1990 to 2024. I saved the raw data as CSV files in our data/raw/ folder: unrate_raw.csv and pce_raw.csv.
* I made sure the script checks that we're actually getting data back from the API and logs what it's doing so we can troubleshoot if anything goes wrong.

### Task Update: Data Cleaning and Integration (Step 3)
* Status: Completed
* Lead: Vedant
* Artifacts & Progress: I created another script called data_cleaning_integration.py that takes the raw data and gets it ready for analysis.

Here's what the script does:
* Reads the CSV files we downloaded
* Makes sure the date columns are in the right format and sets them as the index
* Checks for any missing data (luckily there wasn't any in our date range)
* Combines both datasets into one file using the dates to match them up
* The final combined dataset is saved as unemployment_pce_merged.csv in our data/processed/ folder, which is what we'll use for all our analysis.

### Task Update: Exploratory Data Analysis (EDA) (Step 4)
* Status: In Progress
* Lead: Alex
* Artifacts & Progress: I started exploring the combined dataset to see what patterns we can find. I made a script called eda.py that creates some basic statistics and charts.

So far I've made:

* A line chart showing how unemployment and consumer spending have changed over time (trends_over_time.png)
* A scatter plot to see how they relate to each other (correlation_scatter.png)
* From these first charts, I can already see that when unemployment goes up, consumer spending tends to go down, especially during big events like the 2008 crisis and COVID-19. This matches what we expected to find.

### Task Update: Modeling and Trend Analysis (Step 5)
* Status: Not Started
* Progress: We haven't started the formal statistical modeling yet. We want to finish exploring the data first to make sure we understand what we're working with.

### Task Update: Visualization Development (Step 6)
* Status: In Progress
* Lead: Alex
* Progress: The charts I made for the EDA are our starting point for the final visualizations. We decided to use Seaborn and Matplotlib for all our charts because they make good-looking graphs that we can customize easily.

### Task Update: Report Compilation and Review (Step 7)
* Status: Not Started
* Progress: We'll start putting together the final report once we have all our analysis and charts finished.

## 2. Updated Timeline

| Step | Task | Responsible Member(s) | Original Status | Updated Status & Deadline |
|------|------|----------------------|-----------------|---------------------------|
| 1 | Project Planning | Both | Completed | Completed |
| 2 | Data Acquisition | Vedant | Not Started | Completed |
| 3 | Data Cleaning and Integration | Vedant | Not Started | Completed |
| 4 | Exploratory Data Analysis (EDA) | Alex | Not Started | In Progress - Deadline: Nov 15, 2025 |
| 5 | Modeling and Trend Analysis | Both | Not Started | Not Started - Deadline: Nov 22, 2025 |
| 6 | Visualization Development | Alex | Not Started | In Progress - Deadline: Nov 25, 2025 |
| 7 | Final Report & Reproducibility Check | Both | Not Started | Not Started - Deadline: Dec 5, 2025 |
| 8 | Final Submission (Milestone 4) | Both | Not Started | On Track - Deadline: Dec 7, 2025 |

## 3. Changes to the Project Plan

Closed Gaps:
* We decided to analyze data from 1990 to 2024 because it gives us enough recent data to see clear patterns across different economic periods.
* After looking at the PCE documentation, I found out the data is already adjusted for inflation, so we don't need to do that ourselves.
* We're going with Seaborn and Matplotlib for our charts since they work well and we're already comfortable using them.

Plan Evolution:
* I've been setting up our scripts so they'll work well with Snakemake later on. Each script produces output that the next script can use as input.
* We set up a clear folder structure with separate places for raw data, processed data, scripts, and output files. This makes everything easier to find and work with.

## 4. Individual Contributions

### Contribution Summary by Vedant Patel
I handled getting our data and getting it ready for analysis. I wrote the data_acquisition.py script that downloads the unemployment and consumer spending data from the FRED API, and the data_cleaning_integration.py script that cleans up the data and combines both datasets. I also set up our project folder structure to keep everything organized.

### Contribution Summary by Alex Vasilevich
I worked on exploring the data and creating our first visualizations. I wrote the eda.py script that loads our combined dataset and creates line charts and scatter plots to show the relationship between unemployment and spending. I also wrote most of this status report and have been keeping track of our deadlines to make sure we stay on schedule.