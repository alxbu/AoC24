import re

INPUT = "input.txt"
RESULT = "result.txt"

def load_input():
    """
    Load input data from file

    Returns:
        str: input data
    """
    with open(INPUT, 'r') as f:
        return f.read().strip()
    
def replace_multiple_spaces(data):
    """
    Replace multiple spaces with one space

    Args:
        data (str): input data

    Returns:
        str: data with multiple spaces replaced with one space
    """
    return re.sub(r'\s+', ' ', data)
    
def split_rows(data):
    """
    Split data into rows

    Args:
        data (str): input data

    Returns:
        list: data split into rows using single space as separator
    """
    return replace_multiple_spaces(data).split()

def generate_initial_left_right(data):
    """
    Generate initial left and right values

    Args:
        data (list): data split into rows using single space as separator

    Returns:
        tuple: initial left and right values
    """
    try:
        return int(data[0]), int(data[1])
    except (IndexError, ValueError) as e:
        raise ValueError("Invalid data format for generating left and right values") from e

def calculate_off_value(left, right):
    """
    Calculate off value

    Args:
        left (int): left value
        right (int): right value

    Returns:
        int: off value
    """
    return abs(left - right)

def write_result(result):
    """
    Write result to file

    Args:
        result (int): result to write
    """

    with open(RESULT, 'w') as f:
        f.write(str(result))
    print(result)