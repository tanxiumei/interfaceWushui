def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print("start %s %s" %(argv,func.__name__))
            func(a, b)
            print("end")
        return nei

    return tips


@new_tips("add")
def add111(a,b):
    print(a+b)

add111(3,4)