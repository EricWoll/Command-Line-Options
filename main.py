import Controller as c

def func1():
    print("Func1 Ran")

def func2():
    print("Func2 Ran")

def func3():
    print("Func3 Ran")

def main():
    controller = c.Auto()
    controller.addOption("func1", func1)
    controller.addOption("func2", func2)
    controller.addOption("func3", func3)

    controller.removeOption("func2")
    controller.runLoop()

if __name__ == "__main__":
    main()