# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Challenge 1
word = input("Please enter a word: ")

indexes_dict = {}

for index, char in enumerate(word):
    char = str(char)

    if char in indexes_dict:
        indexes_dict[char].append(index)
    else:
        indexes_dict[char] = [index]

print(indexes_dict)

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

wallet_amount = int(wallet.replace("$", "").replace(",", ""))

affordable_items = []

for item, price_str in items_purchase.items():
    price = int(price_str.replace("$", "").replace(",", ""))
    if price <= wallet_amount:
        affordable_items.append(item)

affordable_items.sort()

if not affordable_items:
    print("Nothing")
else:
    print(affordable_items)