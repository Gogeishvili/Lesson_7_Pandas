import matplotlib.pyplot as plt


class StudentDataVisualizer:
    @staticmethod
    def plot_average_scores_by_semester(average_scores_by_semester):
        average_scores_by_semester.plot(kind='bar', figsize=(12, 6))
        plt.title('Average Score per Subject by Semester', fontsize=16)
        plt.xlabel('Semester', fontsize=12)
        plt.ylabel('Average Score', fontsize=12)
        plt.xticks(rotation=0)
        plt.legend(title='Subjects')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_average_overall_score_by_semester(average_overall_score_by_semester):
        plt.figure(figsize=(12, 6))
        plt.plot(average_overall_score_by_semester.index, average_overall_score_by_semester.values, marker='o')
        plt.title('Average Overall Score by Semester', fontsize=16)
        plt.xlabel('Semester', fontsize=12)
        plt.ylabel('Average Overall Score', fontsize=12)
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig('average_overall_score_by_semester_line_graph.png')
        plt.show()