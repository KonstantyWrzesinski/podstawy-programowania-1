price = float(input('Enter price: '))
discount = int(input('Enter discount %: '))
print('Price with discount: ',"{:.2f}".format(price-price*discount/100))
print('Reduction: ',"{:.2f}".format(price*discount/100))