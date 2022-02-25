Cars = [5, 8, 6, 9, 5, 4, 8, 7, 9, 4, 5, 2]

def mean(a): 
    sum = 0
    for i in range(0, len(Cars)):
        sum = sum + Cars[i]
    mean = sum / len(Cars)
    return mean

def median(a):
    Cars.sort()
    value = len(Cars) / 2
    if value % 2 == 0:
        value_1 = int(value) - 1
        value_2 = int(value)  
        print("The median is", (a[value_1] + a[value_2]) / 2)
    else: 
        round(value)
        value_number = round(value)
        value_number = int(value_number)
        median = a[value_number] 
    return median

def mode(a):
    mode = 0
    for i in a:
        element_count = a.count(i)
        if element_count >= mode:
            mode = element_count
        else:
            return mode


def Range(a):
    a.sort()
    maximum = a[-1]
    minimum = a[0]
    range = maximum - minimum
    return range


print("The mean of the data is", mean(Cars))
print("The median of the data is", median(Cars))
print("The mode of the data is", mode(Cars))
print("The range of the data is", Range(Cars))