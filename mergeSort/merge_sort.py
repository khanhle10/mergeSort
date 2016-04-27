from heapq import merge

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def read_file():
    buffer_size = 4*1024
    max_list = []
    max_buffer = ""
    max_buffer_size = 2*buffer_size
    count = 0
    global_count = 0
    with open("age.txt") as file:
        while True:
            data = file.read(buffer_size)
            if data == '':
                break
            max_buffer = ','.join([data,max_buffer])
            count += 1
            if count == 2:
                list_int = convert_to_int(max_buffer)
                while 0 in list_int:
                    list_int.remove(0)
                write_to_file(list_int, global_count)
                count = 0
                print(global_count)
                global_count += 1

def write_to_file(list, count):
    str_list = ','.join(str(x) for x in list)
    file = "file"
    end_file = "txt"
    with open(file + str(count) + end_file, "w") as o_file:
        o_file.write(str_list)
        o_file.write(',')
        o_file.close()
def convert_to_int(data):
    return quickSort([int(x) for x in data.split(',') if x != '' or x == 0])
read_file()
