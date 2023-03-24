def get_distinct_elements(input_list):
    distinct_list = []
    for element in input_list:
        if element not in distinct_list:
            distinct_list.append(element)
    return distinct_list
my_list = [1, 2, 3, 3, 4, 4, 5]
distinct_list = get_distinct_elements(my_list)
print(distinct_list)