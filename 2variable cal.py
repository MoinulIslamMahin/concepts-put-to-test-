X = int(float(input("X= ")))
Y = int(float(input("Y= ")))
#OPTIONS of MATHS ADD MINUS
operator = input("Enter your operator = ")
if operator == "+":
  print("Answer: " + str(X+Y))
elif operator == "-":
  print("Answer: " + str(X-Y))
#option of maths mul and div
if operator == "*":
  print("Answer: " + str(X*Y))
elif operator == "/":
  print("Answer: " + str(X/Y))
# Option a bit more complex
#EXPONENTIATION
if operator == "**":
  print("Answer: " + str(X**Y))
  #ROUNDING TO NEAREST INTEGER DIVISION
elif operator =="//":
  print("Answer: " + str(X//Y))
  #POWER
elif operator == "^":
  print("Answer: " + str(int(pow( X,Y))))

      
