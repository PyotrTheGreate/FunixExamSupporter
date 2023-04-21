# Funix Exam Supporter - A cool way for teachers to deal with exams
This application helps teachers automate the computation of scores for thousands of students taking exams by author Hoang Nguyen

## Features
- Fast computation on thousands of exams
- Statistical features: **Mean, Min, Max, Point Range, Median**.
## Techniques
- Python (pandas, numpy)
- Regular Expression
- Version Control, Source Code Management (Git/Github)
## Usage
Exams in dataset folder, each file is a set of lines, each line structured with below format
```N00000021,B,A,C,D,C,C,D,D,C,C,D,B,,B,A,C,B,,A,D,A,A,B,D,``` <br />
26 values are separated by a comma, first value is student id, next 25 values are questions answers of that students. Answers can be one of the following: <br />
*None (This means student skipped that question)* <br />
*Letter amongs A,B,C,D* <br />
Edit this line in *lastname_firstname_grade_the_exams.py* to whatever answers key you have: <br />
```answer_key = ["B", "A", "D", "D", "C", "B", "D", "A", "C", "C", "D", "B", "A", "B", "A", "C", "B", "D", "A", "C", "A", "A", "B", "D", "D"]```<br />
Then run the code
```python lastname_firstname_grade_the_exams.py```
## Example of running code
- Running against file with no error
```
>> python lastname_firstname_grade_the_exams.py
Enter a class to grade (i.e. class1 for class1.txt): class1
Successfully opened class1.txt

**** ANALYZING ****

No errors found!

**** REPORT ****

Total valid lines of data: 20
Total invalid lines of data: 0

Mean (average) score: 75.60
Highest score: 91
Lowest score: 59
Range of scores: 32
Median score: 73.0

Question that most people skip: 3 - 4 - 0.2 , 5 - 4 - 0.2 , 23 - 4 - 0.2

Question that most people answer incorrectly: 10 - 4 - 0.20, 14 - 4 - 0.20, 16 - 4 - 0.20, 19 - 4 - 0.20, 22 - 4 - 0.20
```
## About Author
A passionate IT engineer with specialist skills in Artificial Intelligence and Cyber Security.
Contact me for work: **hoangnt@vinorsoft.com**.
Phone: **+84978763468**.