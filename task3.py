import json

# Read json file into applicants variable
with open("Applicants3.json") as json_file:
    applicants = json.load(json_file)

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

# max_students conversion from str to int
max_students = int(max_students)

# Function definition of add_to_dep_list, accepting 5 parameters and returning a sorted list that contains solely the applicants' data needed and leaves remaining applicants 
def add_to_dep_list(dictionary, dictionary_option, departments_index, sorted_list, exam_score, output_list):
    templist1 = []
    for applicant in dictionary:
        # If applicant option# == departments[index] then append it to temporary_list1
        if applicant[dictionary_option] == departments[departments_index]:
            templist1.append(applicant)        

    # Looping through temporary_list1 to append to sorted list the info we need
    for applicant in templist1:
        temporary_list2 = []
        temporary_list2.append(applicant[exam_score])
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


# Function definition of output, taking two parameters and printing department and respective accepted students
def output(departments_index, output_list):
    print("\n")
    print(departments[departments_index])
    # Looping through the range of max_students to print according top successful applicants' names and  department_score
    for i in range(max_students):
        try:
            print(output_list[i][1], output_list[i][2], ":", output_list[i][0])
        except:
            pass


# Calling add_to_dep_list for OPTION1
add_to_dep_list(applicants, "OPTION1", 0, biotech_sorted, "chemistry_score", biotech_output)   
add_to_dep_list(applicants, "OPTION1", 1, chemistry_sorted, "chemistry_score", chemistry_output)
add_to_dep_list(applicants, "OPTION1", 2, engineering_sorted, "cs_score", engineering_output)
add_to_dep_list(applicants, "OPTION1", 3, maths_sorted, "math_score", maths_output)
add_to_dep_list(applicants, "OPTION1", 4, physics_sorted, "physics_score", physics_output)

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


# Nested loop using option2 last_name as lookup value to extract applicants' data from json file 
for applicant in applicants:
    for rem_applicant in remaining_applicants:
        if applicant["last_name"] == rem_applicant[1]:
            option2.append(applicant)


# Calling add_to_dep_list for OPTION2
add_to_dep_list(option2, "OPTION2", 0, biotech_sorted, "chemistry_score", biotech_output)   
add_to_dep_list(option2, "OPTION2", 1, chemistry_sorted, "chemistry_score", chemistry_output)
add_to_dep_list(option2, "OPTION2", 2, engineering_sorted, "cs_score", engineering_output)
add_to_dep_list(option2, "OPTION2", 3, maths_sorted, "math_score", maths_output)
add_to_dep_list(option2, "OPTION2", 4, physics_sorted, "physics_score", physics_output)

# Calling sort_list to sort lists before output
sort_list(biotech_output)
sort_list(chemistry_output)
sort_list(engineering_output)
sort_list(maths_output)
sort_list(physics_output)

# Calling output in order to diplay results 
output(0, biotech_output)
output(1, chemistry_output)
output(2, engineering_output)
output(3, maths_output)
output(4, physics_output)