import requests
import json
import csv

# Getting a response from an API and converting it into json format
response = requests.get("https://my.api.mockaroo.com/applicants4j.json?key=94adc0d0")
results = response.json()

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
def add_to_dep_list(dictionary, dictionary_option, departments_index, sorted_list, exam_score1, exam_score2, output_list):
    temporary_list1 = []
    for applicant in dictionary:
        # If applicant option# == departments[index] then append it to temporary_list1
        if applicant[dictionary_option] == departments[departments_index]:
            temporary_list1.append(applicant)        

    # Looping through temporary_list1 to append to sorted list the info we need
    for applicant in temporary_list1:
        temporary_list2 = []
        # If applicant option# == Physics, Engineering or Biotech then append the mean of the 2 exam results to temporary_list1 & all other info needed
        if applicant[dictionary_option] == "Physics" or applicant[dictionary_option] == "Engineering" or applicant[dictionary_option] == "Biotech":
            temporary_list2.append(((applicant[exam_score1] + applicant[exam_score2])/2))
            temporary_list2.append(applicant["last_name"])
            temporary_list2.append(applicant["first_name"])
            temporary_list2.append(applicant["OPTION2"])
            # Take all applicants from temporary_list2 and append it to respective sorted_list
            sorted_list.append(temporary_list2)
        # Else append only the one exam score needed & all other info needed
        else:
            temporary_list2.append(applicant[exam_score1])
            temporary_list2.append(applicant["last_name"])
            temporary_list2.append(applicant["first_name"])
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


# Function definition of output, taking two parameters and creating a separate csv file for each department and writing respective accepted applicants full names and final mean scores
def output(departments_index, output_list):
    # Using f-string to name each csv file
    with open(f"{departments[departments_index]}.csv", "w", newline= "") as file:
        writer = csv.writer(file)
        writer.writerow(["FULL NAME", "MEAN FINAL SCORE"])
        # Looping through the range of max_students to print according top successful applicants' names and mean scores
        for i in range(max_students):
            try:
                output_list[i][0] = float(output_list[i][0])
                writer.writerow([output_list[i][1] + " " + output_list[i][2], output_list[i][0]])
            except:
                pass


# Calling add_to_dep_list for OPTION1
add_to_dep_list(results,"OPTION1", 0, biotech_sorted, "chemistry_score", "physics_score", biotech_output)
add_to_dep_list(results, "OPTION1", 1, chemistry_sorted, "chemistry_score", "blank", chemistry_output)
add_to_dep_list(results,"OPTION1", 2, engineering_sorted, "math_score", "cs_score", engineering_output)
add_to_dep_list(results, "OPTION1", 3, maths_sorted, "math_score", "blank", maths_output)
add_to_dep_list(results,"OPTION1", 4, physics_sorted, "math_score", "physics_score", physics_output)


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


# Nested loop using option2' last_name as lookup value to extract applicants' data from results dictionary 
for applicant in results:
    for rem_applicant in remaining_applicants:
        if applicant["last_name"] == rem_applicant[1]:
            option2.append(applicant)

# Calling add_to_dep_list for OPTION2
add_to_dep_list(option2,"OPTION2", 0, biotech_sorted, "chemistry_score", "physics_score", biotech_output)
add_to_dep_list(option2,"OPTION2", 1, chemistry_sorted, "chemistry_score", "blank", chemistry_output)
add_to_dep_list(option2,"OPTION2", 2, engineering_sorted, "math_score", "cs_score", engineering_output)
add_to_dep_list(option2,"OPTION2", 3, maths_sorted, "math_score", "blank", maths_output)
add_to_dep_list(option2,"OPTION2", 4, physics_sorted, "math_score", "physics_score", physics_output)

# Calling sort_list to sort lists before output
sort_list(biotech_output)
sort_list(chemistry_output)
sort_list(engineering_output)
sort_list(maths_output)
sort_list(physics_output)

# Calling output in order to diplay results in separate csv files 
output(0, biotech_output)
output(1, chemistry_output)
output(2, engineering_output)
output(3, maths_output)
output(4, physics_output)