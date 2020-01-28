#Kayshale Ortiz
#IS437 Group Assignment 1: Shopping List App

menuOption = None

mylist = []
maxLengthList = 6

menuText = '''
1.) Add Item
2.) Print List
3.) Remove item by number
4.) Save List to file
5.) Load List from file
6.) Exit
'''
while menuOption != '6':
    print(menuText)
    menuOption = input('Enter Selection\n')
    print(menuOption)
    if menuOption == '1':
        #print('Add Item')
        item = ''
        while item == '':
            item = input("Enter your new item: ")
        mylist.append(item)
        #temp = input('Enter Item\n')
        #mylist.append(temp)
        print(mylist)
    elif menuOption == '2':
        #print(mylist)
        n = 1
        for item in mylist:
            print (str(n) + ".)" + item)
            n+=1
            #print(mylist)
    elif menuOption == '3':
        req = None
        while req == None:
            req = input('Enter item number to delete\n')
            index = None
            try:
                index = int(req) - 1
            except:
                print('Invalid Selection')
            if index >= 0 and index <= 5:
                del(mylist[index])
    else:
        print('Your selection was not recognized')
