def find_max(numbers: list) -> int:
    """Find the largest(maximum) number in a list of numbers"""
    pass

def find_min(numbers: list) -> int:
    """Find the smallest(minimum) number in a list of numbers"""
    pass

def find_average(numbers: list) -> int:
    """Find the average of a list of numbers int the list 'numbers' and return 
    it as a float to one decimal point"""
    pass

def find_even_pairs(numbers: list) -> int:
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(0,1), (1, 2)]
    """
    pass

def find_number_of_even_numbers(numbers: list) -> int:
    """Find the total number of even numbers in the list 'numbers' and return 
    the number as an integer"""
    pass

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Max:", find_max(numbers))
    print("Min:", find_min(numbers))
    print("Average:", find_average(numbers))
    print("Even pairs:", find_even_pairs(numbers))
    print("Count of even numbers:", find_number_of_even_numbers(numbers))