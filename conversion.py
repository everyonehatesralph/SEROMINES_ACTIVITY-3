sec = 60

seconds = eval(input("Please input seconds: "))
convert = seconds / sec
convert1 = seconds % sec

print("Seconds: ", seconds)

print("The conversion of" , seconds, "seconds is equivalent to", int(convert) , "minutes and", convert1, "seconds.")