def main():
    print("Hello from greymatter!")

def hello(name):
    print(f'This is {name}')


if __name__ == "__main__":
    hello("edwin")

def conflict_test():
    print("do nothing")

def hello(name):
    print(f'hello {name}!')


if __name__ == "__main__":
    hello('world')
    # main()
