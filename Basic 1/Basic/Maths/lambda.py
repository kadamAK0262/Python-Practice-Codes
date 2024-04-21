# A lambda function in Python is a anonymous function defined using the lambda keyword. 
# It can have any number of parameters but can only have one expression. 
# Lambda functions are often used when you need a simple function for a short period of time 
# and don't want to define a full-fledged function using the def keyword.

def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

result = add_lambda(3, 5)
print(result)  
