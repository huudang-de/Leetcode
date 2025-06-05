my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)
for i in range(n - 1): # i = 0 đến i = n -2 tức là từ 0 đến 6
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    # min_values = my_array.pop(min_index) /n my_array.insert(i, min_values) :sắp xếp lựa chọn
    my_array[j], my_array[min_index] = my_array[min_index], my_array[j] # dịch chuyển sắp xếp lựa chọn tối ưu hơn 
print("Sorted array:", my_array)
