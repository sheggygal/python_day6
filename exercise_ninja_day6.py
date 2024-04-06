string1 = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
list1 = string1.split(", ")

print("Number of manufacturers/companies:", len(list1))

print("Manufacturers in reverse order:")
print(sorted(list1, reverse=True))

manufacturers_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

manufacturers_set = set(manufacturers_list)

print("Companies without duplicates:", ", ".join(manufacturers_set))
print("Number of companies now in the list:", len(manufacturers_set))


print("Manufacturers in ascending order with reversed letters:")
manufacturers_reversed = sorted([manufacturer[::-1] for manufacturer in manufacturers_set])
print(manufacturers_reversed)