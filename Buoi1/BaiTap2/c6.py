def xoa_pt(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a':1, 'b':2, 'c':3}
key_to_delete= 'b'
kq= xoa_pt(my_dict, key_to_delete)

if kq:
    print("Phần tử đã xóa trong Dict: ", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dict")
    