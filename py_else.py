pizza_type = input("Chicken or Beef pizza (c/b): ").upper()
price = 0
if pizza_type == "C":
    pizza_type = "chicken"
    pizza_size = input("Small 7 USD, Medium 12 USD, Large 30 USD (s/m/l): ").upper()
elif pizza_type == "B":
    pizza_type = "beef"
    pizza_size = input("Small 7 USD, Medium 12 USD, Large 30 USD (s/m/l): ").upper()
    price=1
if pizza_size == "S":
    pizza_size = "small"
    price +=7
elif pizza_size == "M":
    pizza_size = "medium"
    price +=12
elif pizza_size == "L":
    pizza_size = "large"
    price +=18

extra = input("Extra cheese (+2 USD) (y/n): ").upper()

if extra == "Y":
    extra = "with extra cheese"
    price+=2
else:
    extra = ""

print("Order summary:")
print(f"{pizza_size} {pizza_type} pizza {extra} cosetyl : {price}")
