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
Usage
Prepare the Data: Place the student_scores_random_names.csv file in the project directory.
Run the Analysis: Execute the following command in your terminal to perform the analysis and generate visualizations:
bash
Copy code
python main.py
Project Structure
Here's a quick overview of the project directory structure:

bash
Copy code
project-directory/
│
├── main.py                                # Main script to execute the analysis
├── student_scores_random_names.csv        # CSV file containing student scores
├── average_scores_by_semester.xlsx        # Output Excel file for average scores
├── average_scores_by_semester_bar_chart.png # Bar chart output
└── average_overall_score_by_semester_line_graph.png # Line graph output
Class Structure
StudentDataHandler: Responsible for loading and saving data.
StudentDataAnalyzer: Contains methods for analyzing student data.
StudentDataVisualizer: Handles all plotting and visual representation of the data.