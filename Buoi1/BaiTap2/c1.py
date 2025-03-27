def tong_chan(lst):
    tong=0
    for num in lst:
        if num%2 ==0:
            tong += num
    return tong

input_list= input("Nhập các số: ")
nums= list(map(int, input_list.split(',')))


ttong_chan = tong_chan(nums)
print("Tổng số chẵn là: ",ttong_chan)