# exercise 1

birthdays = {}
birthdays["Marty"] = 1990/12/10
birthdays["Ann"] = 1987 / 0o3 / 0o4
birthdays["Dan"] = 2000/12/12
birthdays["Kolin"] = 1976/0o5/25
birthdays["Megan"] = 1999/10/30

print("Hey there. You can look up the birthdays of the people in the list!")

person_name = input("Enter a person's name to look up their birthday: ").capitalize()

birthday = birthdays.get(person_name)

if birthday is not None:
    print(f"The birthday of {person_name} is {birthday}.")
else:
    print(f"Sorry, there is no birthday information available for {person_name}.")

# Ex 2
birthdays = {}

birthdays["Marty"] = 1990/12/10
birthdays["Ann"] = 1987/0o3/0o4
birthdays["Dan"] = 2000/12/12
birthdays["Kolin"] = 1976/0o5/25
birthdays["Megan"] = 1999/10/30

print("Names in the dictionary:")
for name in birthdays.keys():
    print(name)

print("\nWelcome!")
print("You can look up the birthdays of the people in the list!")

person_name = input("\nEnter a person's name to look up their birthday: ").capitalize()

birthday = birthdays.get(person_name)

if birthday is not None:
    # Print out the birthday with a nicely-formatted message
    print(f"The birthday of {person_name} is {birthday}.")
else:
    # Print an error message if the person is not found in the dictionary
    print(f"Sorry, we don't have the birthday information for {person_name}.")

# Exercise 3
birthdays = {}

birthdays["Marty"] = 1990/12/10
birthdays["Ann"] = 1987/0o3/0o4
birthdays["Dan"] = 2000/12/12
birthdays["Kolin"] = 1976/0o5/25
birthdays["Megan"] = 1999/10/30

print("\nWelcome!")
user_name = input("Please, enter person's name: ").capitalize()
user_birth_date = input("Please, enter hus/her/ their birth date in YYYY/MM/DD format: ")
birthdays[user_name] = user_birth_date
print("You can look up the birthdays of the people in the list!")
print("Names in the dictionary:")
for name in birthdays.keys():
    print(name)
person_name = input("\nEnter a person's name to look up their birthday: ").capitalize()

birthday = birthdays.get(person_name)

if birthday is not None:
    # Print out the birthday with a nicely-formatted message
    print(f"The birthday of {person_name} is {birthday}.")
else:
    # Print an error message if the person is not found in the dictionary
    print(f"Sorry, we don't have the birthday information for {person_name}.")

# Exercise 4

items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0

for item, details in items.items():
    total_cost += details["price"] * details["stock"]

print("Total cost to buy everything in stock:", total_cost)



