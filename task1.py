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

# Assinging the total number of students to the Total variable
Total = input("Total applicants: ")

# Calling positive_int on Total variable 
positive_int(Total)

# Assinging the number of students that can be accepted to the Accepted variable
Accepted = input("Of the total applicants how many can be accepted? ")

# Calling positive_int on Accepted variable
positive_int(Accepted)

# Instructing user on how to input applicant information 
print("\nType the first name, last name and GPA (separated by whitespace) of each applicant: ")

# Creation of empty lists for later use
all_applicants_list = []
output_list = []

# Ask for input on applicant information based on Total variable
for i in range(int(Total)):
    applicant = input("Enter applicant details: ")
    # Assign a value to applicant information split from a string to a list of strings
    applicant_info = applicant.rstrip().split()
    # If there are more or less than the 3 substrings instructed to input, disregard
    if len(applicant_info) > 3 or len(applicant_info) < 3:
        continue
    # If structure of the list of strings is as instructed, add to all_applicants_list
    elif applicant_info[0].isalpha() == True and applicant_info[1].isalpha() == True and (applicant_info[2].replace(".","").isdigit() == True or applicant_info[2].isdigit()):
        all_applicants_list.append(applicant_info)

# Creation of the output list where last name and first name are concatenated (full name)
for i in range(int(Total)): 
     try:
        first_name, last_name, GPA = all_applicants_list[i]
        output_list.append(((last_name + " " + first_name), GPA))
     except:
         pass
     
# Sorting the output list firstly, by descending grade and secondly, by full name alphabetically 
output_list.sort(key=lambda x: (-float(x[1]), x[0]))

# Output the Successful applicants message
print("\nSuccessful applicants: ")

# Output succesful applicants full name according to how many applicants can be accepted
for i in range(int(Accepted)):
    try: 
        print(output_list[i][0])
    except:
        pass