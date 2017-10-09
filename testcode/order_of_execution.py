'''
Some print statements to show order of execution 

'''


class sample():
    print("CLASS DEF LINE 1")

    var1 = ''

    def __init__(self):
        print("CLASS INIT 1")
        self.var1 = 10

    def get_val(self):
        print("CLASS FUNC DEF LINE 1")
        return self.var1

    print("CLASS DEF END")


def main():
    print("IN FUNC LINE 1")
    s = sample()
    print("IN FUNC AFTER CLASS INIT")
    print(s.get_val())
    print("IN FUNC END")


if __name__ == "__main__":
    print("IF main LINE 1")
    main()
    print("IF main END")
