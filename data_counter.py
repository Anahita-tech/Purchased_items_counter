items=input('Enter a list of purchased items please(space-separated):') .split()# Getting list of purchased items by user and transform string to list by space-separated
result={} # We want to show the final result as an dictionary so we create an empty dictionary
for i in items: # loop through each item in the list
    result.setdefault(i,items.count(i)) # use 'setdefault' , 'i' as key and 'count(i)' as a value
print('result=',result) # show result
