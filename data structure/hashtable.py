hash_table = list([0 for _ in range(10)])

def hash_func(key):
    # 나머지 연산
    return key % 5

def store_data(data, value):
    key = ord(data[0])
    hash_val = hash_func(key)
    hash_table[hash_val] = value


def get_data(data):
    key = ord(data[0])
    hash_val = hash_func(key)
    return hash_table[hash_val]


data1 = 'gahyun'
data2 = 'nahyun'
data3 = 'jungmi'


store_data(data1, '010-4258-8535')
store_data(data2, '010-5252-8535')
store_data(data3, '010-5528-8535')

print(hash_table)
print(get_data(data1))