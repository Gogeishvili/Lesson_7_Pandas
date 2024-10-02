from student_data_analyzer import StudentDataAnalyzer
from student_data_handler import StudentDataHandler
from student_data_visualizer import StudentDataVisualizer


def main():
    file_name = 'student_scores_random_names.csv'

    handler = StudentDataHandler(file_name)
    df = handler.df

    analyzer = StudentDataAnalyzer(df)

    failed_students_list = analyzer.find_failed_students()
    print(f"Students who failed in any subject: {failed_students_list}")

    average_scores_by_semester = analyzer.calculate_average_scores_by_semester()
    print(average_scores_by_semester)

    top_students = analyzer.calculate_gpa()
    print(f"Students with the highest GPA: {top_students}")

    lowest_average_subject, lowest_average_score = analyzer.find_most_difficult_subject()
    print(f"Most difficult subject is '{lowest_average_subject}' with an average score of {lowest_average_score:.2f}.")

    output_file = 'average_scores_by_semester.xlsx'
    handler.save_to_excel(average_scores_by_semester, output_file)

    StudentDataVisualizer.plot_average_scores_by_semester(average_scores_by_semester)

    df['Overall_Score'] = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis=1)
    average_overall_score_by_semester = df.groupby('Semester')['Overall_Score'].mean()
    StudentDataVisualizer.plot_average_overall_score_by_semester(average_overall_score_by_semester)



if __name__ == "__main__":
    main()
