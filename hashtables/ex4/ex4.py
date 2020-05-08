def has_negatives(a):

    """
    YOUR CODE HERE
    """
    # pro tip dont print (a) lmao
    
    num_dict = {}
    result = []

    for num in a:
        # see if there is another instance of the number in our array positive or negative
        if num_dict.get(abs(num)):
            if (num_dict.get(abs(num)) + num) == 0:
                result.append(abs(num))
        else:
            num_dict[abs(num)] = num 

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
