from functions import load_input, split_rows, generate_initial_left_right, calculate_off_value, write_result

def main():
    in_data = load_input().split("\n")
    
    left_list, right_list = [], []

    for row in in_data:
        row = split_rows(row)
        left, right = generate_initial_left_right(row)
        left_list.append(left)
        right_list.append(right)
        
    left_list.sort()
    right_list.sort()
        
    off_values = [calculate_off_value(x, y) for x, y in zip(left_list, right_list)]

    result = sum(off_values)
    
    write_result(result)

if __name__ == '__main__':
    main()