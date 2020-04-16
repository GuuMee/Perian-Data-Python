def func():
    print("func() in one_main.py")

print("TOP LEVEL ONE_MAIN.PY")

if __name__ == '__main__':
    print('one_main.py is being run directly')
else:
    print("one_main.py has been inported")
