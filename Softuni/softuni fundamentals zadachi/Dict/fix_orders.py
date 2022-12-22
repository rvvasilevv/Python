line = input().split(" ")
productQuantity = {}
productPrices = {}

while "buy" not in line:
    product = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if product not in productQuantity.keys():
        productQuantity[product] = 0
        productPrices[product] = 0.00
    productQuantity[product] += quantity
    productPrices[product] = price
    line = input().split(" ")

    if "buy" in line:
        break

for key, value in productQuantity.items():
    price = value * productPrices[key]
    print(f"{key} -> {price:.2f}")