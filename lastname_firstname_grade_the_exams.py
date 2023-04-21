import re
import numpy as np
import pandas as pd

# Path to dataset folder
data_path = "./dataset/"
# Right answer for 25 questions
answer_key = ["B", "A", "D", "D", "C", "B", "D", "A", "C", "C", "D", "B", "A", "B", "A", "C", "B", "D", "A", "C", "A", "A", "B", "D", "D"]


# Function to read lines of file
def read_file(file_name):
    try:
        with open(data_path + file_name,'r') as f:
            list_data = f.readlines()
        list_data = [x.strip() for x in list_data] # Strip string
        print("Successfully opened " + file_name + ".txt" + "\n")
        return list_data
    except Exception as ex:
        print("File cannot be found.",ex)


# Function uses regex to check whether student id is valid
def check_valid_student_id(student_id):
    pattern = r'^N\d{8}$'
    if re.match(pattern, student_id):
        return True
    else:
        return False


# Function use pandas to compute mean, max, min, values range, median of dataframe
def scores_statistic(file_grades):
    grades_df = pd.read_csv(file_grades, names = ["Student ID", "Score"]) # Load student's scores of a class from file to pandas dataframe
    scores_df = grades_df["Score"]
    return scores_df.mean(), scores_df.max(), scores_df.min(), scores_df.max() - scores_df.min(), scores_df.median()


# Main function to process file
def process_file(list_data, file_name):
    return
# Main execution code
if __name__ == "__main__":
    file_name = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    list_data = read_file(file_name + ".txt") # Read file first