#write a program to check if a person is eligible for discount the criteria is he must be a student and age must be below 21, without if else , input values to take are role and age , example : eligible : true 


person = str(input("Enter your occupation: "))
age = int(input("Enter your age: "))

eligible = person == "student" and age < 21

print("Eligible:", eligible)