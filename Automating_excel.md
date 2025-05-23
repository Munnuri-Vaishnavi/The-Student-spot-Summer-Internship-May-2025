# Titanic Excel Report Automation with Pandas and openpyxl

This project automates the cleaning, transformation, and visualization of the Titanic dataset using **pandas** and **openpyxl**. The final output is a fully formatted Excel report with charts that summarize the data in an intuitive way.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Data Cleaning](#data-cleaning)
- [Excel Formatting & Charting](#excel-formatting--charting)
- [Generated Report](#generated-report)
- [How to Run](#how-to-run)
- [Credits](#credits)

## Overview

As part of an internship at *The Student Spot*, this project automates the following:

- Cleans raw Titanic dataset (train.csv)
- Handles missing values and duplicate records
- Converts data types and renames columns
- Saves the cleaned data to an Excel file
- Enhances Excel file with formatting and visual charts

## Technologies Used

- Python 3.x
- pandas
- openpyxl

## Data Cleaning

Steps performed:

- *Missing Values:*  
  - Filled missing Age values with the median.
  - Replaced missing Embarked values with the mode.
  - Dropped the Cabin column due to excessive null values.

- *Duplicate Removal:* Checked and confirmed there are no duplicate rows.

- *Type Conversion:*  
  - Converted Sex to numerical values (male: 0, female: 1).
  - Converted Survived, Pclass, and Embarked to categorical types.

- *Column Renaming:*  
  - Renamed Embarked to Passenger_started.

## Excel Formatting & Charting

- *Header Formatting:* Bold and colored headers for clarity.
- *Auto-adjust Column Widths:* Improved readability.
- *Charts Created:*
  - *Survival Counts (Bar Chart)*
  - *Passenger Class Distribution (Pie Chart)*
  - *Age Distribution (Bar Chart)*

These charts are placed in a new worksheet titled *Charts*.

## Generated Report

- cleaned_titanic.xlsx - Cleaned dataset
- cleaned_titanic_report_with_charts.xlsx - Final report with charts

## How to Run

1. Install required libraries:

   ```bash
   pip install pandas openpyxl
