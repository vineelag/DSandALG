def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.
    :param seq: A list of integers
    :rtype: A list of sorted integers
    """

    gaps = [x for x in range(len(seq) // 2, 0, -1)]

    for gap in gaps:
        for i in range(gap, len(seq)):
            temp = seq[i]
            j = i
            while j >= gap and seq[j - gap] > temp:
                seq[j] = seq[j - gap]
                j -= gap
            seq[j] = temp

    return seq
