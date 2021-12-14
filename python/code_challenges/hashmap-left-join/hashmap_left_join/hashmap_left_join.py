def left_join(hashmap1, hashmap2):
    result = []
    for key, value in hashmap1.items():
        if key in hashmap2:            #The same as using .contains from our hashtable
            result += [[key, hashmap1[key], hashmap2[key]]]
        else:
            result += [[key, value, 'NULL']]
    return result
