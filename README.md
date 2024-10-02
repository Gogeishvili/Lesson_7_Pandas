# Student Score Analysis

## Overview
This project analyzes student scores across various subjects and semesters using Pandas and Matplotlib. It provides insights into students' performance, identifies those who are struggling, and visualizes the data through various plots.

## Features
- Load student score data from a CSV file.
- Identify students who have failed in any subject.
- Calculate average scores by semester for each subject.
- Calculate the GPA for each student and find the highest achievers.
- Identify the subject with the lowest average score.
- Save average scores by semester to an Excel file.
- Visualize average scores and overall performance by semester using bar and line charts.

## Requirements
- Python 3.x
- Pandas
- Matplotlib
- OpenPyXL (for saving to Excel)

## Installation
To get started with the project, you need to have Python installed. You can create a virtual environment and install the required packages using pip:

```bash
# Create a virtual environment (optional)
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install required packages
pip install pandas matplotlib openpyxl
