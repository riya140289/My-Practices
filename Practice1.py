'''PROVIDED A LIST, ONLY INTEGERS HAS TO BE SORTED''' 

lst = [[(1,2,3,"abc")], 56,67, "xyz",["ab", 45, 76.0, [14,15]]]
def recursiveData(data):
    answer_lst = []
    for items in data:
        if isinstance(items, list):
            answer_lst.extend(items)
            isiter(answer_lst)
            print(isiter(answer_lst))
        else:
            answer_lst.append(items)
            print(answer_lst, "**answer_lst**")
    answer = list(filter(lambda i: isinstance(i, str), isiter(answer_lst))) #  (int, float)
    return answer

def isiter(data):
    answer_lst = []
    for items in data:
        if isinstance(items, list):
            answer_lst.extend(items)
        elif isinstance(items, tuple):
            answer_lst.extend(items)
        else:
            answer_lst.append(items)
    return answer_lst
    
print(recursiveData(lst))

