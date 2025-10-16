def find_max(numbers: list) -> int:
    """Find the largest(maximum) number in a list of numbers"""
    return max(numbers)

def find_min(numbers: list) -> int:
    """Find the smallest(minimum) number in a list of numbers"""
    return min(numbers)

def find_average(numbers: list) -> int:
    """Find the average of a list of numbers int the list 'numbers' and return 
    it as a float to one decimal point"""
    return sum(numbers)/len(numbers)

def find_even_pairs(numbers: list) -> int:
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(0,1), (1, 2)]
    """
    even_pairs = []

    for i in range(len(numbers)- 1):
        if i % 2 == 0:
            (numbers[i] + numbers[i+1])
            even_pairs.append (i, i + 1)
    return find_number_of_even_numbers([6, 2, 3, 5, 9, 4, 1, 11])


def find_number_of_even_numbers(numbers: list) -> int:
    """Find the total number of even numbers in the list 'numbers' and return 
    the number as an integer"""
    even_numbers = 0
    for i in numbers:
        if i % 2 == 0:
            even_numbers += 1
    return even_numbers

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Max:", find_max(numbers))
    print("Min:", find_min(numbers))
    print("Average:", find_average(numbers))
    print("Even pairs:", find_even_pairs(numbers))
    print("Count of even numbers:", find_number_of_even_numbers(numbers))