#Take a Number from user 
Number = int(input("Enter a no."))

#Find it's square root
root = Number**0.5

x = int(root + 0.5)**2

#Here we check weather number is a perfect square or not
if x == Number:
  print(Number," is a perfect square of",root)
else:
  print(Number," is not a perfect square")
#your program is ready to run
