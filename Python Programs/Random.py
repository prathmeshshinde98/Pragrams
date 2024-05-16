
if __name__ == "__main__":
    arr = input().split()
    # print(arr)
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    total_height = 0
    number_students = len(arr)
    average_height = 0
    for i in range(0, len(arr)):
        total_height = total_height + arr[i]

    print(f"Total height = {total_height}")
    print(f"Number of students = {number_students}")
    print(f"Average height = {total_height/number_students}")