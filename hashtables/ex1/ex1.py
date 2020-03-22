#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # first we need to insert the
    for i in range(length):
        #hash_table_insert takes the ht, the keys and the values
        hash_table_insert(ht, weights[i], i)
    #now that our hashtable has nodes we can retrieve to compare
    for i in range(length):
        #retrieve is using the 'ht' and keys
        # 21 - 6 = 15
        next_i = hash_table_retrieve(ht, limit - weights[i])
        #if 15 exists
        if next_i:
            # if 15 is greater than 6
            if next_i > i:
                # return 15,6
                return [next_i, i]
            else:
                # return 6, 15
                return [i, next_i]
    #if there are less then two values
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
