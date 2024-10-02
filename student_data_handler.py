import  pandas as pd

class StudentDataHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_csv(self.file_name)

    def save_to_excel(self, df, output_file):
        df.to_excel(output_file, index=True)
        print(f"Data has been saved to '{output_file}'.")