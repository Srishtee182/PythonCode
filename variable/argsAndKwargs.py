#when we need to add more arguments for the functions and which we don't need to update again and again
#so for that we will pass the list in the argument and print that list
def function_name_print(a,b,c,d):
    print(a, b, c, d)
function_name_print("Python", "SQL", "Java", "API")

def funargs(normal, *args, **kwargs): # the args will be converted in tuple, also #we have keep normal arg first and then *kwargs
#putting kwargs means it is eligible to take kwargs,
    print(type(args))
    print(normal)
    print(args[0])
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

arg= ["Python", "SQL", "Java", "API", "HTML"]
normal = "this is just a statement"
kw = {"Python":"Backend","Java":"Backend","SQL":"Database"}
funargs(normal, *arg, **kw)