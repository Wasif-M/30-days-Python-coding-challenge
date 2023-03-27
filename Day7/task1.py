# Scope of Function
def my_global_function():
    global x
    x = "This variable has global scope!"
    print(x)
my_global_function()
print(x)

def my_local_function():
    x = "This variable has local scope!"
    print(x)
my_local_function()
print(x)
