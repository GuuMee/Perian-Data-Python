#An often confusing part of Python is a mysterious line of code:
#if __name__ = "__main__":
#Sometimes when you are importing from a module, you would like to know whether a modules function is being used as an import, or if you are using the original .py file of that module
import one_main
print("TOP LEVEL NAME_AND_MAIN.PY")
one_main.func()

if __name__ == '__main__':

    #all the main logic of the code will come here
    print("name_and_main.py being run directly")
else:
    print("name_and_main.py is being imported")

#all this works because of this __name__
#__name__ is built-in variable which evaluates to the name of the current module
#So whenever I run name_and_main.py directly, then this variable __name__ above is equal to '__main__'
