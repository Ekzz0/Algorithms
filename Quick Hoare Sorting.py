from random import random
from math import floor
def Quick_Hoare_Sorting(lst):
    if len(lst) > 1:
        random_index = floor(random()*len(lst))
        rNum_lst = lst[random_index]
        low =[x for x in lst if x < rNum_lst]
        eq = [x for x in lst if x == rNum_lst]
        high = [x for x in lst if x > rNum_lst]
        lst = Quick_Hoare_Sorting(low) + eq + Quick_Hoare_Sorting(high)
    return lst


lst = [-3, 2, -4, 5, 0 , -1, 10]
print(Quick_Hoare_Sorting(lst))

