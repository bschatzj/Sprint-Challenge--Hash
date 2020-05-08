def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """

    weights_dict = {}

    for index in range(length):
        # find the index that gets us to the limit
        index_two = weights_dict.get(limit - weights[index])
        
        if index_two is not None:

            print(limit)
            print(index)
            print(index_two)
            return (index, index_two)
        else:
            weights_dict[weights[index]] = index

    return None