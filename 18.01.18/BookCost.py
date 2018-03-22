# cost of the books

num = int(input("Enter the number of books : "))
cover_price = 24.95

without_discount =  num * cover_price
with_discount = without_discount - (without_discount * 0.4)

if(num >= 1):
    shipping_cost = (0.75 * (num - 1))
    shipping_cost += 3.00
    total_cost = with_discount + shipping_cost
    print ("Total cost of book = %d $\n" %(total_cost))

else:
    print("No price for 0 books\n")
