def dao_nguoc_ds(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số: ")
nums = list(map(int, input_list.split(',')))

list_dngc = dao_nguoc_ds(nums)
print("Sau khi đảo ngược: ", list_dngc)
