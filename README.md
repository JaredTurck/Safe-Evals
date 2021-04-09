# Safe Evals
`eval(input())` and `exec(input())` are dangerous as they allow the user of your program to potentially execute malicious code. This can range anything from importing dangerous modules like os then issuing commands to harm your pc, to causing your code to hang by using a lot of system resources. 

```python
def calc():
    print("Calculator:")
    user = input("input: ")
    while set([i in "0123456789.+-*/%() " for i in user]) != {True}:
        user = input("Invalid input!\ninput: ")

    answer = eval(user)
    print(f"answer: {user} = {answer}")
```
Here we have a simple calculator that takes an input from the user, then uses eval to compute the input and print the result. For example, the code below shows a user using the calculator to work out the area of a circle.
```python
>>> calc()
Calculator:
input: (3.1415 * (9**2))
answer: (3.1415 * (9**2)) = 254.4615
>>> 
```
The problem is that the user could input a calculation that takes a long time to compute, resulting in your code hanging or even crashing (such as with a memory overflow error). we can use validation in the form of the while loop to double check that the input is a valid equation (e.g. contains only number and uses valid operators). but trying to stop the user from inputting equations that require a lot processor time to compute is harder to do.
```python
>>> calc()
Calculator:
input: 1000000 ** 1000000

```

# How to use
executes the code `print('Hello World!')`, and returns the result using the execute method.
```python
from execute_code import execute_code

ex = execute_code()
output = ex.execute("print('Hello World!')")
print(output)
```

```python
while True:
    output = ex.execute(input('> '))
    print(output)
```

# Testing malicious code
Safe evals tries to minimize the threat of malicious or processor intensive code, by checking the users input for dangerous modules, functions, and keywords before executing it. any code that takes longer then 5 seconds to compute is halted. Below are some examples of users trying to execute harmful code.
trying to import os and shutdown the computer
```python
> __import__("o" + "s").system("shutdown /r")
Attempted to load untrusted module!
> 
```
```python
> __import__(repr(chr(111) + chr(115))).system("shutdown /r")
Attempted to load untrusted module!
> 
```
user tries to import os through global vars
```python
> print(globals()["o" + "s"].system("shutdown /r").read())
globals is not allowed!
> print(locals()["o" + "s"].system("shutdown /r").read())
locals is not allowed!
> print(vars()["o" + "s"].system("shutdown /r").read())
vars is not allowed!
> 
```
trying to cause program to hang by running an endless while loop
```python
> while True: 
  print(True)
Script was terminated, as it ran for longer then 5 seconds!
> 
```
endless for loop
```python
> x = [1]
for i in x:
    x.append(i)
Script was terminated, as it ran for longer then 5 seconds!
> 
```
