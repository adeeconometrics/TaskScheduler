class Test:
    lst = []
    def __init__(self, arg) -> None:
        self.lst.append(arg)

    def get_list(self)->list:
        return self.lst

if __name__ == '__main__':
    t = Test(1)
    b = Test(2)

    print(t.get_list())