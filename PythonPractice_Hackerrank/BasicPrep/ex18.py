def print_two(*args):
    arg1,arg2 = args
    print("Arg1:%s, Arg2:%s"%(arg1,arg2))

def print_two_again(args1,args2):
    print("Arg1:{0},Arg2:{1}".format(args1,args2))

def print_none():
    print("Geeerooo")

print_two("Hello",1)
print_two_again("Hello",1)
print_none()
