#encoding:utf-8
def qukic_sort(data):
    if len(data)>= 2:
        base_data = data[0]
        left , right = [] ,[]
        data.remove(base_data)
        for i in data:
            if i > base_data:
                right.append(i)
            else:
                left.append(i)
        return qukic_sort(left) + [base_data] + qukic_sort(right)
    else:
        return data
arry = [ 45,78,125,15,48,32,79,123,5,7,11]
print qukic_sort(arry)