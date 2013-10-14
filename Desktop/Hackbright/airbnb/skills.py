# Write a function that takes an iterable (something you can loop through, ie: 
#string, list, or tuple) and produces a dictionary with all distinct elements as the keys, 
#and the number of each element as the value



def count_unique(some_iterable):
    dictionary = {}
    for item in some_iterable:
        value = dictionary.get(item,None)
        if value == None:
            dictionary[item] = 1
        elif value != 0:
            dictionary[item] += 1
    return dictionary


count_unique([1,2,3,4,4])




# Given two lists, (without using the keyword 'in' or the method 'index') 
# return a list of all common items shared between both lists

def common_items(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1):
        while j < len(list2):
            if list1[i] == list2[j]:
                result.append(list2[j])
            j += 1
        j = 0
        i += 1
    return result

print common_items([3,4,8,8], [1,2,3,3,8])




# Given two lists, (without using the keyword 'in' or the method 'index') return 
# a list of all common items shared between both lists. 
# This time, use a dictionary as part of your solution.

def common_items2(list1, list2):
    result = []
    dictionary = {}
    i = 0
    while i < len(list1):
        dictionary[list1[i]] = 1
        i += 1
    result = []
    j = 0
    while j < len(list2):
        value = dictionary.get(list2[j],None)
        if value != None:
            result.append(list2[j])
        j += 1
    return result



common_items2([1,3,5,7], [3,8,0,1])









