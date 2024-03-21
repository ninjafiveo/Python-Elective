import random

my_answers= [
"No",
"Yes",
"I doubt you should.",
"Pizza, Pizza",
"Are you crazy?"
"Can't Answer that Right Now.",
"What would your mom say?",
"Maybe you shouldn't do that.",
"Dino Nuggies",
"BBQ Ribs"
]
while True:
    my_number = random.randrange(0, 9)
    question = input("What would you like to ask the magic 8 ball? ")
    print(my_answers[my_number])
    ask_again = input("Would you like to ask another question?  ")
    if ask_again != "yes":
        print("Thank you for asking questions. Have a lovely day.")
        break

# print(my_number)