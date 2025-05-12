line1 = input().split()
units1 = int(line1[1])
price1 = float(line1[2])

line2 = input().split()
units2 = int(line2[1])
price2 = float(line2[2])

total = (units1 * price1) + (units2 * price2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))