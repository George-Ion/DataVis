# Liquor Sales Data Analysis

This Python script performs data analysis and visualization on a liquor sales dataset. It includes two main tasks: analyzing liquor sales by zip code and analyzing sales by store. The script uses `pandas` for data manipulation and `matplotlib` for plotting graphs.

## Features

- **Data Loading**: Reads liquor sales data from a CSV file.
- **Data Preparation**: Filters data by date range, processes it to extract relevant columns, and groups data by zip code and store.
- **Visualization**: 
  - **Scatter Plot**: Shows liquor sales by zip code, visualizing the number of bottles sold in each zip code.
  - **Bar Chart**: Displays the top 15 stores by sales percentage, highlighting the sales performance of the highest-performing stores.

## Requirements

- `pandas`: For data manipulation.
- `matplotlib`: For plotting graphs.

To install the required libraries, run:

```bash
pip install pandas matplotlib
