# from collections import namedtuple
#
# Feature = namedtuple('sss', ['age', 'gender', 'name'])
# row = Feature(age=22, gender='male', name='Alex')
# print(row.age)
#
# from collections import Counter
#
# ages = [22, 22, 25, 25, 30, 24, 26, 24, 35, 45, 52, 22, 22, 22, 25, 16, 11, 15, 40, 30]
# value_counts = Counter(ages)
# print(value_counts.most_common())
#
from collections import defaultdict
#
# my_default_dict = defaultdict(int)
# for letter in 'the red fox ran as fast as it could':
# 	my_default_dict[letter] += 1
# print(my_default_dict)

# Passing a function to return default value
def print_default():
    return 1

def_dict=defaultdict(print_default)
print(def_dict['chocolate'])

# Вывод:
# value absent