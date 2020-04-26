def func1():
    print("Hello")
def func2():
    print("Goodbye")
def func3():
    print("Default")

def inline_try(x):
    try:
        return int(x)
    except ValueError:
        return x

switch = {
    1 : func1,
    2 : func2,
    }

if __name__ == "__main__":
    import time
    start = time.time()
    for i in range(5):
        if i == 1:
            func1()
        elif i == 2:
            func2()
        else:
            func3()
    print(f"Time for if/elif/else: {time.time() - start}")

    start = time.time()
    for i in range(5):
        switch.get(i, func3)()
    print(f"Time for switch: {time.time() - start}")

    
    while True:
        switch.get(inline_try(input(": ")), func3)()

