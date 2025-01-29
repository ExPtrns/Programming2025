def get_unique(l1, l2):
    join_list = l1 + l2
    result = []
    for i in join_list:
        if i in l1 and i in l2:
            continue
        else:
            result.append(i)
    return result