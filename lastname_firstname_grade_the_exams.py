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
    # Counting error lines
    error_lines_count = 0
    error_found = False     # Check if error line is found in class file
    # Student point list and number of high score students (score > 80)
    list_student_point = []
    high_student_point_count = 0
    # Numpy array to count student that skipped questions and chose wrong questions
    skip_students = np.zeros(25)
    wrong_students = np.zeros(25)
    # Analyze to find error lines
    print("**** ANALYZING ****" + "\n")
    for each_item in list_data:
        list_values = each_item.split(",")
        current_student_id = list_values[0]
        if not check_valid_student_id(current_student_id): # Check if student id is valid
            error_found = True
            error_lines_count += 1
            print("Invalid line of data: N# is invalid")
            print(each_item + "\n")
        elif len(list_values) != 26: # Check if number of values is exactly 26
            error_found = False
            error_lines_count += 1
            print("Invalid line of data: does not contain exactly 26 values:")
            print(each_item + "\n")
        else:
            list_answer = list_values[1:]
            current_student_point = 0
            for i,eachAnswer in enumerate(list_answer):
                if list_answer[i] == "": # Skip questions +0 point
                    current_student_point += 0
                    skip_students[i] += 1
                elif list_answer[i] == answer_key[i]: # Right answer +4 points
                    current_student_point += 4
                else:
                    wrong_students[i] += 1 # Wrong answer -1 point.
                    current_student_point -= 1
            if current_student_point > 80: # Check high score student
                high_student_point_count += 1
            list_student_point.append(current_student_id + "," + str(current_student_point))
    if not error_found:
        print("No errors found!" + "\n")
    # Report score statistic of a class
    print("**** REPORT ****"+"\n")
    print("Total valid lines of data: "  + str(len(list_data)-error_lines_count))
    print("Total invalid lines of data: " + str(error_lines_count))
    print("Total student of high scores: " + str(high_student_point_count)+"\n")
    # Save class grades file
    with open(data_path + file_name + "_grades.txt", "w") as f:
        for each_student_point in list_student_point:
            f.write(each_student_point + "\n")
    # Compute various values
    mean, highest_score, lowest_score, range_of_scores, median_score = scores_statistic(data_path + file_name + "_grades.txt")
    print("Mean (average) score: {:.2f}".format(mean))
    print("Highest score: {:}".format(highest_score))
    print("Lowest score: {:}".format(lowest_score))
    print("Range of scores: {:}".format(range_of_scores))
    print("Median score: {:}".format(median_score) + "\n")
    # Display most skipped question in format: skipped question - number of students skipped - skipped ratio
    max_skip_question = np.where(skip_students == np.amax(skip_students))[0]
    print("Question that most people skip: ", end='')
    for i,each_skip_question in enumerate(max_skip_question):
        print(str(int(each_skip_question+1))
        +" - " 
        +str(skip_students[each_skip_question]) 
        +" - "
        +str(float(skip_students[each_skip_question])/len(list_data)), end='')
        if i != len(max_skip_question)-1:
            print(" , ", end='')
    print('')
    # Display most wrong question in format: wrong question - number of students chose wrong - wrong ratio
    max_wrong_question = np.where(wrong_students == np.amax(wrong_students))[0]
    print("Question that most people answer incorrectly: ", end='')
    for i,each_wrong_question in enumerate(max_wrong_question):
        print(str(int(each_wrong_question+1)) 
        + " - " 
        +str(wrong_students[each_wrong_question]) 
        + " - "
        + str(float(wrong_students[each_wrong_question])/len(list_data)), end='')
        if i != len(max_wrong_question)-1:
            print(" , ", end='')
    print('\n')

# Main execution code
if __name__ == "__main__":
    file_name = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    list_data = read_file(file_name + ".txt") # Read file first
    process_file(list_data, file_name) # Then process