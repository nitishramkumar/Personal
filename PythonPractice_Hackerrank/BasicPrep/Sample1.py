def  StairCase(n):
    for i in range(0,n):
        #print n-i-1 spaces,print i+1 #
        for spaceC in range(0,n-i-1):
            print(' ',end='')
        for hashC in range(0,i+1):
            print('#',end='')
        print('\n')
