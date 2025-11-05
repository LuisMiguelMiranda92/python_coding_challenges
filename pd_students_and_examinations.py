"""
Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
 

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
 

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.
"""
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    # 1. Get the exam counts (your original code was perfect for this)
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    
    # 2. Create all possible (student, subject) pairs using a cross merge
    # This creates the "master list" of all combinations
    all_combinations = pd.merge(students, subjects, how='cross')
    
    # 3. Left merge the exam counts onto the master list
    # This keeps every student/subject pair
    merged_df = pd.merge(all_combinations, exam_counts, how='left', on=['student_id', 'subject_name'])
    
    # 4. Fill in 0 for students who didn't take an exam
    # Any pair from the master list that had no match in exam_counts
    # will have NaN. We fill this with 0.
    merged_df['attended_exams'] = merged_df['attended_exams'].fillna(0).astype(int)
    
    # 5. Sort for the final output
    merged_df = merged_df.sort_values(by=['student_id', 'subject_name'])
    
    return merged_df[['student_id', 'student_name', 'subject_name', 'attended_exams']]