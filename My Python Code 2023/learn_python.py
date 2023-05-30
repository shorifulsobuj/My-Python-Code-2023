resource = False
internet = False
computer = True

if((resource or internet) and computer):
    print('you can learn Python')
else:
    print('you can not learn python')