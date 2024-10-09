import pandas as pd
from pandas import json_normalize
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import csv


# Function definition of positive_int, taking one parameter and testing whether a number is a positive integer
def positive_int(x):
    try:
        x = int(x)
    except:
        print("\nPlease enter positive integer number")
        quit()
    if x < 0:
            print("\nPlease enter positive integer number")
            quit()
    else:
        pass

# Assigning max applicants to accept per department in max_students variable
max_students = input("How many applicants to accept per department: ")

# Calling positive_int function
positive_int(max_students)

# Max_students conversion from str to int
max_students = int(max_students)


# Function definition of add_to_dep_list, accepting 6 parameters and returning a sorted list that contains solely the applicants' data needed and leaves remaining applicants 
def add_to_dep_list(dictionary, dicionary_option, departments_index, sorted_list, best_score, output_list):
    temporary_list1 = []
    for applicant in dictionary:
        # If applicant option# == departments[index] then append it to temporary_list1
        if applicant[dicionary_option] == departments[departments_index]:
            temporary_list1.append(applicant)        

    # Looping through temporary_list1 to append to sorted list the info we need
    for applicant in temporary_list1:
        temporary_list2 = []
        temporary_list2.append(applicant[best_score])
        temporary_list2.append(applicant["last_name"])
        temporary_list2.append(applicant["first_name"])
        temporary_list2.append(applicant["OPTION1"])
        temporary_list2.append(applicant["OPTION2"])
        # Take all applicants from temporary_list2 and append it to respective sorted_list
        sorted_list.append(temporary_list2)

    # Sorting list by descending score and by name alphabetically
    sorted_list.sort(key=lambda i: (-int(i[0]), i[1], i[2]))

    # Append to output list according to max_students and remove added apllicants from sorted_list
    k = sorted_list[0:max_students]
    output_list.extend(k)
    del sorted_list[0:max_students]


# Function definition of del_list, taking one parameter and emptying a list
def del_list(sorted_list):
    del sorted_list[:]


# Function definition of sort_list, taking one parameter and sorting a list
def sort_list(output_list):
    output_list.sort(key=lambda i: (-int(i[0]), i[1], i[2]))


# Creation of departments list to use as lookup values
departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]

# Creation of 2 empty lists per department for later use
biotech_sorted = []
biotech_output = []

chemistry_sorted = []
chemistry_output = []

engineering_sorted = []
engineering_output = []

maths_sorted = []
maths_output = []

physics_sorted = []
physics_output = []

# Getting a response from an API and converting it into json format
response = requests.get("https://my.api.mockaroo.com/applicants5j.json?key=94adc0d0")
results = response.json()

# Using json_normalize() to convert json to DataFrame
df = json_normalize(results)

# Using df.fillna() to update all missing values to 0
df = df.fillna(0)

# Creating a new column with the mean scores or singular score of exams required for admission of OPTION1
df.loc[df["OPTION1"] == "Biotech", "OPTION1 mean scores"] = df[["physics_score", "chemistry_score"]].mean(axis=1)
df.loc[df["OPTION1"] == "Chemistry", "OPTION1 mean scores"] = df["chemistry_score"]
df.loc[df["OPTION1"] == "Engineering", "OPTION1 mean scores"] = df[["math_score", "cs_score"]].mean(axis=1)
df.loc[df["OPTION1"] == "Mathematics", "OPTION1 mean scores"] = df["math_score"]
df.loc[df["OPTION1"] == "Physics", "OPTION1 mean scores"] = df[["math_score", "physics_score"]].mean(axis=1)

# Creating a new column with the mean scores or singular score of exams required for admission of OPTION2
df.loc[df["OPTION2"] == "Biotech", "OPTION2 mean scores"] = df[["physics_score", "chemistry_score"]].mean(axis=1)
df.loc[df["OPTION2"] == "Chemistry", "OPTION2 mean scores"] = df["chemistry_score"]
df.loc[df["OPTION2"] == "Engineering", "OPTION2 mean scores"] = df[["math_score", "cs_score"]].mean(axis=1)
df.loc[df["OPTION2"] == "Mathematics", "OPTION2 mean scores"] = df["math_score"]
df.loc[df["OPTION2"] == "Physics", "OPTION2 mean scores"] = df[["math_score", "physics_score"]].mean(axis=1)

# Creating a new column that uses np to calculate whether the score of the final exams for OPTION1 or special exam score is higher
df["Best score Option 1"] = np.maximum(df["OPTION1 mean scores"], df["admissions_exam"])

# Creating a new column that uses np to calculate whether the score of the final exams for OPTION2 or special exam score is higher
df["Best score Option 2"] = np.maximum(df["OPTION2 mean scores"], df["admissions_exam"])

# Converting DataFrame to dictionary
df_dict = df.to_dict("records")

# Calling add_to_dep_list for OPTION1
add_to_dep_list(df_dict,"OPTION1", 0, biotech_sorted, "Best score Option 1", biotech_output)
add_to_dep_list(df_dict,"OPTION1", 1, chemistry_sorted, "Best score Option 1", chemistry_output)
add_to_dep_list(df_dict,"OPTION1", 2, engineering_sorted, "Best score Option 1", engineering_output)
add_to_dep_list(df_dict,"OPTION1", 3, maths_sorted, "Best score Option 1", maths_output)
add_to_dep_list(df_dict,"OPTION1", 4, physics_sorted, "Best score Option 1", physics_output)

# Creation of a list containing applicants that did not make it in their option1 department 
remaining_applicants = physics_sorted + maths_sorted + biotech_sorted + engineering_sorted + chemistry_sorted

# Calling del_list to clear department_sorted lists
del_list(physics_sorted)
del_list(maths_sorted)
del_list(biotech_sorted)
del_list(engineering_sorted)
del_list(chemistry_sorted)

# option2 empty list creation
option2 = []

# Nested loop using option2 last_name as lookup value to extract applicants' data from df_dict dictionary 
for applicant in df_dict:
    for rem_applicant in remaining_applicants:
        if applicant["last_name"] == rem_applicant[1]:
            option2.append(applicant)

# Calling add_to_dep_list for OPTION2
add_to_dep_list(option2,"OPTION2", 0, biotech_sorted, "Best score Option 2", biotech_output)
add_to_dep_list(option2,"OPTION2", 1, chemistry_sorted, "Best score Option 2", chemistry_output)
add_to_dep_list(option2,"OPTION2", 2, engineering_sorted, "Best score Option 2", engineering_output)
add_to_dep_list(option2,"OPTION2", 3, maths_sorted, "Best score Option 2", maths_output)
add_to_dep_list(option2,"OPTION2", 4, physics_sorted, "Best score Option 2", physics_output)

# Calling sort_list to sort lists before output
sort_list(biotech_output)
sort_list(chemistry_output)
sort_list(engineering_output)
sort_list(maths_output)
sort_list(physics_output)

display_list = [biotech_output, chemistry_output, engineering_output, maths_output, physics_output]

# Creating a csv file in which there is a display of successful applicants and their best score per department according to max_students
with open("AllAcceptedStudents.csv", "w", newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(["DEPARTMENT", "FULL NAME", "BEST SCORE"])
    # Using a nested loop to write into csv the department, respective top successful applicants according to max_students, their full names and best score
    for i in range(len(departments)):
        for student in range(max_students):
            try:
                writer.writerow([departments[i], display_list[i][student][1] + " " + display_list[i][student][2], display_list[i][student][0]])
            except:
                pass
    

# Creating a loop to use "1" & "2" in f-string to create 2 png files containg a bar graph that shows mean score per gender per department for OPTION1 & OPTION2, respectively
for i in range(1,3):
    # Grouping OPION{i} mean scores by OPTION{i} & gender to get the average score per department & gender
    mean_score_option = df.groupby([f"OPTION{i}", "gender"])[f"OPTION{i} mean scores"].mean()

    # Using unstack to reshape the data so that gender and OPTION{i} can be the bars of the bar chart
    mean_score_option.unstack().plot(kind="bar")

    # Adding a title and labelling the axis 
    plt.title(f"Mean score per department & gender - Option{i}")
    plt.xlabel("Department")
    plt.ylabel("Mean score")
    plt.savefig(f"Mean scores Option{i}.png")