"""
https://docs.python.org/3/tutorial/classes.html
"""
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print("in defining scope of nonlocal spam", spam)

    def do_global():
        global spam
        spam = "global spam"
        print("in defining scope of global spam", spam)

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    #do_global()
    #print("After global assignment:", spam)
    nonlocal spam2 # using spam gives error as it is already bound in local
    spam2 = "nonlocal in top level fn spam"


scope_test()
print("In global scope:", spam)
