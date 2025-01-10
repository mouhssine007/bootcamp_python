products=["Milk","Beef","Fish","Chiken","Apple","Cake","Bread"]
days_to_expire = [7,30,0,15,1,-4,-1]

for i in range(len(products)):
    days_left=days_to_expire[i]
    if days_left<=0:
        valdity="Expired"
    elif days_left<=7:
        valdity= f"consume with {days_left} day(s)"

    else:
        valdity="Good"
    print(f"Product {i+1} : {products[i]} [{valdity}]")

