#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"source: {self.source}, dest: {self.destination}"


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #need to insert tickets into hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        print('ticket', ticket)
    print('len', length)

    destination = 'NONE'
    #iterate through the length
    for x in range(length):
        #now need to retrieve each route
        route[x] = hash_table_retrieve(hashtable, destination)
        destination = route[x]

    return route
