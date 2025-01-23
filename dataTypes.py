# Dictionary/Maps - SIMILAR TO JAVASCRIPT DICTIONARY

# TUPLE - once value is fixed, we can't change it.

pi_tuple = (1,2,3,4,5);
# pi_tuple = list(pi_tuple) + (3,4) # Won't work as we can't combine list with the tuple
# print(f'{pi_tuple}')

pi_tuple = pi_tuple + (3,4); # THIS WILL WORK
# print(f'{pi_tuple}')

new_list = list(pi_tuple)
# print(f'{new_list}')

new_list = tuple(pi_tuple)
# print(f'{new_list}')
pi_tuple = (1,2,3,33,3,33,3,3,3,4,5); # no change
# print(f'LIST = {new_list}')

pi_tuple = 9; # no change
# print(f'LIST = {new_list}')



# LISTS - dynamic

newList = ['a', 'b', 'c', 'd'];

# print(f'newList is {newList}')
# print(f'newList is {newList[-1]}')


newList2 = ['e', 'f', 'g', 'h'];

combinedList = [newList, newList2]; # Remember to put the brackets to make it a List. AND ',' in between not '+'. Otherwise, it will just concat the two lists and make them one.

# print(f'{combinedList}');

# print(f'{min(combinedList)}');
# print(f'{max(combinedList)}');

# print(f'{combinedList[1][0]}');
del combinedList[0];
# print(f'{combinedList}');
# print(f'{len(combinedList[0])}');

combinedList.append('123');
# print(f'{combinedList}');

combinedList[0].insert(2, '99999');

# print(f'{combinedList}');

combinedList[0].remove('99999');

# print(f'{combinedList}');

combinedList[0].sort();
# print(f'{combinedList}');

combinedList.reverse();
# print(f'{combinedList}');
