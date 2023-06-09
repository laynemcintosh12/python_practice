def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newLst = []
    for item in lst:
        if item is True:
            newLst.append(item)
    return newLst