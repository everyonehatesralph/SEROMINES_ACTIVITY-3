tax = .06
amount = eval(input("Enter purchase amount: "))
salestax = float(amount) * float(tax)

print ("Amount: ", amount)
print ("Sales tax is,", round(salestax, 2))