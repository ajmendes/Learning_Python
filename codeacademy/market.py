prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3}

stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15}

for food in prices:
    print(food)
    print("price: %s" % prices[food])
    print("stock: %s" % stock[food])

total = 0
for key in prices:
    total = total + prices[key] * stock[key]

print("\nTotal price:", total)


def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total = total + prices[item]
      stock[item] = stock[item] - 1
  return total