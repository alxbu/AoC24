from functions import load_input, split_rows, generate_initial_left_right, count_distinct_elements_in_list, write_result

def main():
    similarities = []
    
    in_data = load_input().split("\n")
    
    left_list, right_list = [], []

    for row in in_data:
        row = split_rows(row)
        left, right = generate_initial_left_right(row)
        left_list.append(left)
        right_list.append(right)
        
    count_dict_right = count_distinct_elements_in_list(right_list)
    count_dict_left = count_distinct_elements_in_list(left_list)
        
    similarities = [count_dict_left[elem] * elem * count_dict_right.get(elem, 0) for elem in count_dict_left]

    result = sum(similarities)
    
    write_result(result, 2)

if __name__ == '__main__':
    main()