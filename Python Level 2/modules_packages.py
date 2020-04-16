#Before you've seen Python import statement, but have probably wondered, how do they work and how do we create our own
import mymodule

mymodule.func_in_module()

#when you run this file you probably noticed that you got __pycache__ folder and inside of that mumodule.cpython-38.py file
#and basically what happens is when you run a program in Python the interpreter compiles it to byte code first
#That's kind of an oversimplification but essentially it stores that in the __pycache__folder
#that bitecodes does make your program start a little faster the next time you run it and when your script changes you'er going to be recompiled
#And if you delete the files with the whole folder and run your program again they're going to reappear

#Let's see the other various you can import from a mymodule
# other way: import mymodule as something, so you don't wanna write mymodule everytime
import mymodule as mm
#then you can shorten mymodule as mm:
mm.func_in_module()

#if you just plan on using a few specific functions from mymodule.py you probably don't want to import the entire module you want to import a few functions.
from mymodule import func_in_module
func_in_module()

#The following imports all from module, that's not recommended:
from mymodule import * #this is frowned upon, you shouldn't do this sort of * behaviour. It's kind of waste a lot of memory and importing everything with *
func_in_module()
