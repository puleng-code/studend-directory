#student Name, Age, Email Address, Familiar Programming Language(>1), Mentor 

student_info = {
    "Student1":{"Name":"Puleng","Age": 82, "email_address": "puleng@techupschool.com","Familiar_Languages":["C#","Java","Python"],"Mentor": "Nicol"},
    "Student2":{"Name":"Talent","Age": 25,"email_address": "talent@techupschool.com","Familiar_Languages":["Python", "Html","Javascript", "CSS"],"Mentor": "Jason"},
    "Student3":{"Name":"Nosipho","Age": 42,"email_address": "nosipho@techupschool.com","Familiar_Languages": ["Python", "Javascript"],"Mentor": "Nicol"},
    "Student4":{"Name":"Jade","Age": 64,"email_address": "jade@techupschool.com", "Familiar_Languages":["Java", "Python"],"Mentor": "Jason"},
    "Student5":{"Name":"Alvine","Age": 53,"email_address": "alvine@techupschool.com","Familiar_Languages":["CSS", "Javascript", "Html"],"Mentor": "Nicol"}
    }

print(student_info)
print("\n")
ages = []
def get_youngest_age():
    # create list to store all student ages
    student_ages = []

    # loop looks at each student and puts the age into the above list
    for student in student_info:
        student_ages.append(student_info[student]["Age"])

    # get the min age from the list and store it in a variable
    youngest_age = (min(student_ages) or 0)
    
   # loop over students again and check if that student has the min age. If it does, print the students name. You could just print the whole student by excluding ["Name"]
    for student in student_info:
        if student_info[student]["Age"] == youngest_age:
            print("The youngest student is", student_info[student]["Name"], ", with", student_info[student]["Age"], "years of age")
    print("\n")
get_youngest_age()

def get_email_addreses():
    print("Students emails are as follows: ")
    for email in student_info:
     print(student_info[email]["email_address"])
print("\n")
get_email_addreses()

def get_students_by_programming_language():
    stu_language = input("Which programming language you want to print? ")

    for student in student_info:
       familiar_languages = student_info[student]["Familiar_Languages"]
       for language in range(len(familiar_languages)):
            familiar_languages[language] = familiar_languages[language].upper()
       if stu_language.upper() in familiar_languages:
         print(student_info[student]["Name"])
           
    return stu_language
print("\n")
get_students_by_programming_language()
