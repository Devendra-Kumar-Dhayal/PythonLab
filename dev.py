 

def add(a,b):
    return a+b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def sub(a,b):
    return a-b


def simp_intre(p,r,t):
    return (p*r*t/100)
def comp_intre(p,r,n,t):
    A= p(1+r/n)**(n*t)
    return A
def Various_operations():
    lst = [1,2,3,4,5,67,8,9,0,0]
    print("Original list : ", lst )
    print("sliced list from 1st to 3rd element : ", lst[1:4])
    print("sliced list from 2nd to last element : ", lst[2:])
    print("reversed list")
    for i in range(0,len(lst)):
        print("", lst[-i-1])
def operations_on_set():
    print("operations on set ")
    st = {1,2,234,5,7,88,90,87,6,56,56,3453,54534,55}
    st2 = {1,2,45,6,5,6546,34,34,,5432, 2,3,4,6,4,23,4,3}
    union = st|st2
    intersec = st&st2
    diff = st - st2
    symdif = s1^s2
    print("set 1 = ", st)
    print("set 2 = ", st2)
    print("union = ", union)
    print("intersection = ", intersec)
    print("difference = ", diff)
    print("symmetric difference = ", symdif)
def operations_on_dict():
    dic1 = {"dev":"iot","abhi":"cse","raman":"is","naman":"12th"}
    print("original dictionary : ", dic1)
    print("dictionary keys : " dic1.keys())
    print("dictionary values : " dic1.values())
def operations_on_tuple():
    tup = (1,2,3,4,5,67,8)
    print("Tuple : ", tup )
    print("slices tuple from 1 to 3 element : ", tup[1:4])
    print("multiplication of tuple : ", tup*3)
    try :
        tup[7] = 8
        print("value added")
    except :
        print("system throws an error")


def mgu3p():
    import matplotlib.pyplot as plt
    data = {'C':20, 'C++':15, 'Java':30,'Python':35}
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(courses, values, width = 0.4)
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    plt.show()
