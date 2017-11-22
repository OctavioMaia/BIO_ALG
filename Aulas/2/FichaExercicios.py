def A1(list, x):
    count = 0
    for i in range(len (list)):
        if list[i] >= x :
            count+=1

    return count

list = [2,3,4,5,6,2,2]

print(A1(list,5))

def B3(Seq):
    if Seq == Seq.reverse():
        return True
    else:
        return False

a = ["B","C","B"]
print(B3(a))