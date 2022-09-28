
'''string1="    file "
string2="Biscuit    "
string3="   sandwitch"


print(string1.upper())
print(string2.upper())
print(string3.upper())

string1="    file "
string2="Biscuit    "
string3="   sandwitch"
print(string1.strip())
print(string2.strip())
print(string3.strip())




string1="Becomes"
string2="BEEHIVE"
string3=" bEautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))




integer_string="6"
print(int(integer_string)*7)


float_string="6.01"
print(float(float_string)*7)



weight=0.2
animal="tiger"
print(str(weight)+"kg is the weight os the tiger"+animal+".")
print("{} kg is the weiight of the {}.".format(weight,animal))


print("AAA".find("a"))

phrase = "somebody said something to sumana"
phrase = phrase.replace("s","x")
print(phrase)


num1=25_000_000
num2=25000000
print(num1)
print(num2)
num = 1.75e5
print(num)


print(2e308)


base=input("enter a base")
exponential=input("enter an exponent")
result=float(base)**float(exponential)
print(f"{base} to power of {exponential}={result}")


user_input=input("enter num")
num=float(user_input)
print(f"{num}rounded to 2 decimal place is {round(num,2)}")

user_input=input("enter a num")
num=float(user_input)
print(f"the absolute value of {num} is {abs(num)}")

num1=float(input("enter a num"))
num2=float(input("enter another number"))
print(
    f"the diff between {num1} and {num2}is an integer?"
    f"{(num1-num2).is_integer()}!"
)

print(f"{3**.125:3f}")
print(f"${150000:,.2f")

print(f"{2/10:0%}")



def cube(num):
    cube_num=num**3
    return cube_num
print(f"0 cubed is {cube(0)}")
print(f"2 cubed is {cube(2)}")


def greet(name):
    """display a greeting """
    print(f"hello{name}!")
    greet("guido")
    
    
 def convert_cel_to_far(temp_cel):
     """return the celcius temperature temp_cel converted to fahrenite"""
     temp_far=temp_cel*(9/5)+32
     return temp_far
 
 
 
 temp_far=input("enter the temperature in f")   
 temp_cel=input("enter the temperature in c")
 print(f"{temp_far}degree F= {temp_cel:.2f}degrees c")
 print(f"{temp_far}degree F= {round(temp_cel,2)}degrees c")
 
def invest(amount,rate,year):
     for year in range (1,year+1):
         amount=amount*(1+rate)
         print(f"year {year}:${amount:,.2f}")
     
        
amount=float(input("enter a  principal amount"))   
rate=float(input("enter an anual rate of return:"))
year=int(input("enter a number of years"))
invest(amount,rate,year)'''

