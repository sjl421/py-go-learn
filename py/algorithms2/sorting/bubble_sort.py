
def sort(seq):
    '''
    Takes a list of integers and sorts them in ascending order.
    This sorted list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    '''
    L = len(seq)
    for i in range(L):
        for n in range(1, L-i):
            if seq[n] < seq[n-1]:
                seq[n-1], seq[n] = seq[n], seq[n-1]
    return seq
