a = str(input("Input a sentence: "))


def rev(a):
    newl = a.split(" ")
    newrev = ""
    for i in range(len(newl)):
        newrev+=newl[len(newl)-i-1] + " "
    return newrev


print(rev(a))
