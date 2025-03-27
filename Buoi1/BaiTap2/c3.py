def tao_tuple(lst):
    return tuple(lst)

input_list = input("Nhập các số: ")
nums = list(map(int, input_list.split(',')))

my_tuple = tao_tuple(nums)
print("List: ", nums)
print("Tuple từ list: ", my_tuple)
