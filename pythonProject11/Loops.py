# # for number in range(5):
# #     print("Tojtech", number)
# #     if number == 2:
# #         print("Tojtech index 2")
# #         break
# # print("Irakli, great question man")
#
# call_attempt = ""
#
# name = "  Naseem   "
# print(name)
# while call_attempt.lower() != "QUIT ":  # .upper means that whatever letter case you type the word
#     # "quit in the terminal, it will turn it into upper case and if it matches
#     # "QUIT", which in this case it does, the terminal exits the code
#     call_attempt = input("Enter your call attempt: ")
#     print("This is the first call  attempt 1: " + call_attempt)
# # Age = 13, the application checks if the user meets the age requirements, above 13
#
# number = 100
# print("The number is: " + str(number))  # turns the variable number into a string instead of int
# print("{}{}".format("The number is: ", number))  # the curly braces are like characters for each str, int, and so on
#
# year_of_birth = 1991
# name = "Naseem"
# print("The year of birth is:", f"{year_of_birth} {name}")
#
# for number in range(30):
#     print("Tojtech", number)
#     if number == 2:
#         print("Emil cool man")
#         break
# print("emil, great question man")
# #
# call_attempt = ""
# while call_attempt.upper() != "QUIT":
#     call_attempt = input("Enter your call attempt: ")
#     print("This is the call_attempt: " + call_attempt)
# name = "   Good morning  Naseem   "
# print(name.split())
year_of_birth = 1982
name = "Emil"
print("{}{}{}{}".format("The year of birth is: ", year_of_birth, " ", name))
print("The year of birth is:", f"{year_of_birth} {name}")