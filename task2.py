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


# Function definition of add_to_dep_list, taking two parameters and adding applicants according to first/second option to respective department 
def add_to_dep_list(list_to_loop, option):
    # Looping applicants of a list to add them to department according to respective department[index]
    for applicant in list_to_loop:
        if applicant[option] == departments[0]:
            maths_list.append(applicant)
        elif applicant[option] == departments[1]:
            physics_list.append(applicant)
        elif applicant[option] == departments[2]:
            biotech_list.append(applicant)
        elif applicant[option] == departments[3]:
            chemistry_list.append(applicant)
        elif applicant[option] == departments[4]:
            engineering_list.append(applicant)


# Function definition of add_to_output_list, taking two parameters and adding applicants to an output list according to max students
def add_to_output_list(department_list, output_list):
    k = department_list[0:max_students]
    output_list.extend(k)
    del department_list[0:max_students]


# Function definition of del_list, taking one parameter and emptying a list
def del_list(department_list):
    del department_list[:]


# Function definition of output, taking two parameters and printing department and respective accepted students and their GPA
def output(departments_index, output_list):
    print("\n")
    print(departments[departments_index])
    # Looping through the range of max_students to print according top successful applicants' names and GPA
    for i in range(max_students):
        try:
            print(output_list[i][0], output_list[i][1])
        except:
            pass


# Creation of departments list to use as lookup values
departments = ["Mathematics", "Physics", "Biotech", "Chemistry", "Engineering"]

# Empty list creation to add applicants
ranking_applicants = []

# Creation of 2 empty lists per department for later use
biotech_list = []
biotech_output_list = []

chemistry_list = []
chemistry_output_list = []

engineering_list = []
engineering_output_list = []

maths_list = []
maths_output_list = []

physics_list = []
physics_output_list = []


# Reading and adding csv file to a list
with open('Applicants2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    applicants = list(csv_reader)

# Concatenation of last_name and first_name to full name
for i in range(len(applicants)):
    first_name, last_name, GPA, option1, option2 = applicants[i]
    ranking_applicants.append(((last_name + " " + first_name), GPA, option1, option2))

# Sorting by descending GPA and by full name alphabetically
ranking_applicants.sort(key=lambda x: (-float(x[1]), x[0]))

# Assigning max applicants to accept per department in max_students variable
max_students = input("How many applicants to accept per deparment: ")

# Calling positive_int function
positive_int(max_students)

# Max_students conversion from str to int
max_students = int(max_students)

# Calling add_to_dep_list function
add_to_dep_list(ranking_applicants, 2)

# Calling add_to_output_list function  
add_to_output_list(biotech_list, biotech_output_list)
add_to_output_list(maths_list, maths_output_list)
add_to_output_list(chemistry_list, chemistry_output_list)
add_to_output_list(engineering_list, engineering_output_list)
add_to_output_list(physics_list, physics_output_list)

# Creation of a list containing applicants that did not make it in their option1 department
remaining_applicants = biotech_list + maths_list + chemistry_list + engineering_list + physics_list

# Calling del_list function
del_list(biotech_list)
del_list(maths_list)
del_list(chemistry_list)
del_list(engineering_list)
del_list(physics_list)

# Calling add_to_dep_list function
add_to_dep_list(remaining_applicants, 3)

# Calling add_to_output_list function  
add_to_output_list(biotech_list, biotech_output_list)
add_to_output_list(maths_list, maths_output_list)
add_to_output_list(chemistry_list, chemistry_output_list)
add_to_output_list(engineering_list, engineering_output_list)
add_to_output_list(physics_list, physics_output_list)

# Calling output function  
output(2, biotech_output_list)
output(3, chemistry_output_list)
output(4, engineering_output_list)
output(0, maths_output_list) 
output(1, physics_output_list) 