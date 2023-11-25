import datetime

# Boolean - true or false
print(bool(0)) # false value such as (), {}, [], "", 0 and None
print(bool(-54)) #true value is anything but not (), {}, [], "", 0 and None
print(100.0 <= 122) # result from a condition

# Operators
# dateToday = datetime.datetime.now().strftime("%A") # will return the Day today
fltOp1 = 25
fltOp2 = 23

# Arithmetic
print(fltOp1 + fltOp2) # addition
print(fltOp1 - fltOp2) # subtraction
print(fltOp1 * fltOp2) # multiplication
print(fltOp1 / fltOp2) # division
print(fltOp1 // fltOp2) # floor division

# Comparison
print(fltOp1 == fltOp2) # equal
print(fltOp1 != fltOp2) # not equal
print(fltOp1 < fltOp2) # less than
print(fltOp1 > fltOp2) # greater than
print(fltOp1 <= fltOp2) # less than & equal
print(fltOp1 >= fltOp2) # greater than & equal

# Logical Operator
print(fltOp1 != fltOp2 and fltOp1 > fltOp2) # and - if all statement is true = true, one statement is false = false 
print(fltOp1 == fltOp2 or fltOp1 < fltOp2) # or - if one statement is true = true, all statement is false = false
print(not(fltOp1 == fltOp2 or fltOp1 < fltOp2)) # not - will reverse the result

# Identity
print(fltOp1 is fltOp2) # is - returns true if both variables are the same object

# Membership
fltOp3 = [1,0,9,25]
print(fltOp1 in fltOp3)

# Precedence
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR


