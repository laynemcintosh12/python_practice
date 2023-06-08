def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count = {}
    for i in str(num1):
        count[i] = count.get(i, 0) + 1
    count_two = {}
    for x in str(num2):
        count_two[x] = count.get(x, 0) + 1
    return count == count_two
    