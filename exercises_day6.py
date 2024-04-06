# Ex1 Convert the two following lists, into dictionaries.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

pairs = zip(keys, values)

dict1 = dict(pairs)

print(dict1)

# Ex 2 Exercise 2 : Cinemax

family = {}

num_family_members = int(input("Enter the number of family members: "))
for i in range(num_family_members):
    name = input("Enter family member's name: ")
    age = int(input("Enter family member's age: "))
    family[name] = age

cost_toddler = 0
cost_child = 10
cost_other = 15

total_cost = 0
individual_costs = {}

for name, age in family.items():
    if age < 3:
        cost = cost_toddler
    elif 3 <= age <= 12:
        cost = cost_child
    else:
        cost = cost_other
    individual_costs[name] = cost
    total_cost += cost

print("Individual Costs:")
for name, cost in individual_costs.items():
    print(f"{name}: ${cost}")

print("Total Cost for the Family:", total_cost)

# Ex 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": {"pink", "green"}
    }
}

brand["number_stores"] = 2

print(f"The clients of Zara are {', '.join(brand['type_of_clothes'])}.")

brand["country_creation"] = "Spain"


if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print("Last international competitor:", brand["international_competitors"][-1])

print("Major clothes colors in the US:", brand["major_color"]["US"])

print("Amount of key-value pairs:", len(brand))

print("Keys of the dictionary:", list(brand.keys()))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print("Value of the key number_stores:", brand["number_stores"])

# Ex 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}

for index, user in enumerate(users):
    disney_users_A[user] = index

print(disney_users_A)

disney_users_B = {}

for index, user in enumerate(users):
    disney_users_B[index] = user

print(disney_users_B)

disney_users_C = {}

for index, user in enumerate(sorted(users)):
    disney_users_C[user] = index

print(disney_users_C)

disney_users_I = {}

for index, user in enumerate(users):
    if 'i' in user:
        disney_users_I[user] = index

print(disney_users_I)


