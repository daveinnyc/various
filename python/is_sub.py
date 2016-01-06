def is_sub(str1, str2):
    '''
    >>> is_sub('abc', 'abcd')
    True
    >>> is_sub('abcd', 'abc')
    False
    >>> is_sub('abc', 'ababcd')
    True
    >>> is_sub('abc', 'dfabcd')
    True
    >>> is_sub('abc', 'dfabc')
    True
    >>> is_sub('', 'abcd')
    True
    >>> is_sub('', '')
    True
    '''
    sub = str1
    super = str2
    
    if '' == sub:  #empty sring is a substring of all strings
        return True
    if len(str1) <= len(str2): #substring can't be longer than super
        for i in range(len(super)):
            j = 0
                            
            while super[i] == sub[j]:
                if (len(sub) - 1) == j:
                    return True
                i += 1
                j += 1
        
    return False
    
    
if "__main__" == __name__:
    import doctest
    doctest.testmod()