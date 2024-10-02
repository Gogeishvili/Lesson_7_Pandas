class StudentDataAnalyzer:
    def __init__(self, df):
        self.df = df

    def find_failed_students(self):
        subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
        failed_students = set()
        for subject in subjects:
            failed_in_subject = self.df[self.df[subject] < 50]['Student']
            failed_students.update(failed_in_subject)
        return sorted(list(failed_students))

    def calculate_average_scores_by_semester(self):
        return self.df.groupby('Semester')[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()

    def calculate_gpa(self):
        self.df['GPA'] = self.df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis=1)
        student_gpa = self.df.groupby('Student')['GPA'].mean()
        max_gpa = student_gpa.max()
        return student_gpa[student_gpa == max_gpa]

    def find_most_difficult_subject(self):
        subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
        average_scores = self.df[subjects].mean()
        lowest_average_subject = average_scores.idxmin()
        lowest_average_score = average_scores.min()
        return lowest_average_subject, lowest_average_score
