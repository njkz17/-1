print("Hello, World")

print()

print("value1", "value2", "value3")

print()

name = "Alex"
print(name)

print()

name = input("What is your name? ")
print("Hello,", name)
x = float(input("First number: "))
y = float(input("Second number: "))
operation = input("Operation: ")

result = None

if operation == "+":
  result = x + y
elif operation == "-":
  result = x - y
elif operation == "*":
  result = x * y
elif operation == "/":
  result = x / y
else:
   print("Unsupported operation")
if result is not None:
   print("Result:", result)
   pass
number = int(input("Enter a number: "))
if number > 5:

   print("This number is greater than five.")

pass

if number is not None:
   pass # TODO: add some logic here later
x = float(input("x = "))
if x>0:
  y=x** 0.5
else:
  y=x** 12
print(y)
name = input("Enter your name: ")

if name == "Alexey":
   print("You have entered", name)
   print("This is my name, too.")
else:
   print("Your name differs from mine.")
   # x = float(input("x = "))

# if 0<x< 7:
#  print("Value is in range, let's continue")
#  y=2*x-5
#  if y <0:
#    print("y is negative")
#  else:
#     if y >0:
#       print("y is positive")
#     else:
#          print("y = 0")
x = float(input("x = "))
if 0<x<7:
  print("Value is in range, let's continue")
  y=2*x-5
  if y <0:
    print("y is negative")
  elif y > 0:
    print("y is positive")
  else:
    print("y = 0")
    print("""Menu
1. File
2. View
3. Exit
""")

 

choice = int(input("Enter your choice: "))
if choice == 1:
 print("You have selected 'File' menu")
elif choice == 2:
 print("You have selected 'View' menu")
elif choice == 3:
 print("Stopping.")
else:
 print("Incorrect choice")
 is_ready = False

# if is_ready:
#  state_msg = "Ready"
# else:
#  state_msg = "Not ready yet"
state_msg = is_ready and "Ready" or "Not ready yet"
print (state_msg)
response = exit
while response != "exit":
 response = input("Type 'exit' to exit: ") 
 number = 0
while number <= 0:
 number = int(input("Enter a positive integer: "))
print("You have entered", number)
n=1
while n <= 3:
 print("n =",n )
 n+=1
 while True:
 print("Enter 'exit' to exit loop")
 response = input("> ")
 if response == "exit":
   break
number = 0
while number < 10:
 number += 1
 if number == 5:
  continue
 print("Current number is", number)
 counter = 5
while counter:
  print (counter)
  counter -= 1
print('Loop is complete') 
print('counter =', counter)
attempts_left = 3
while attempts_left > 0:
   attempts_left -= 1
   password = input("Enter your password "
       "(you have {} attempts left): ".format(attempts_left + 1))
   if password == "98eaxc":
     print("Access granted")
     break
else:
 print("Access denied")
 for row in range(5):
  for column in range(30):
   print("*", end="")
   print()

