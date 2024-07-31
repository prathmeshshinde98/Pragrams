
def two_sum(nums : list[int], target: int) -> list[int]:
    hash_stack = {}
    value_found_flag = 0
    for num in range(len(nums)):
        search_number = target - nums[num]
        if search_number in hash_stack:
            value_found_flag = 1
            return [hash_stack[search_number], num]
        hash_stack[nums[num]] = num
    if value_found_flag == 0:
        return [0,0]


if __name__ == "__main__":
    string_input = input('Enter Array (Put a space after each number) - ')
    target_number = int(input('Enter Target Sum Number '))
    string_input = string_input.strip()
    formatted_string = string_input.split(' ')
    input_array = []

    for i in formatted_string:
        input_array.append(int(i))
    return_list = two_sum(input_array, target_number)
    if return_list == [0,0]:
        print('No numbers in array which add up to target value')
    else:
        print(return_list)