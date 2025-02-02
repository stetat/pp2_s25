# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]





def rcheck(stup):
    return stup["imdb"] > 5.5


def filt(slist):
    sub = []
    for i in range(len(slist)):
        if slist[i]["imdb"] > 5.5:
            sub.append(slist[i]["name"])
    
    return sub


def category(slist, cate):
    sub = []
    for i in range(len(slist)):
        if slist[i]["category"] == cate:
            sub.append(slist[i]["name"])
    return sub


def avg_score(slist):
    avg = 0
    amount = 0

    for i in range(len(slist)):
        avg+=1
        amount+=slist[i]["imdb"]
    
    return round(amount/avg, 3)


def avg_ctg_score(slist, name):
    avg = 0
    amount = 0

    for i in range(len(slist)):
        if slist[i]["category"] == name:
            avg+=1
            amount+=slist[i]["imdb"]
    
    return round(amount/avg, 3)




choice = int(input("Which movie do you want to check? (1-15): "))

f_check = filt(movies)

name = str(input("which categories' movies do you want to see?: "))
c_check = category(movies, name)

name_1 = str(input("which categories' average IMDB do you want to see?: "))


print(rcheck(movies[choice-1]))


print("")


for x in f_check:
    print(x)
print("")


for x in c_check:
    print(x)
print("")


print(avg_score(movies))
print("")

print(avg_ctg_score(movies, name_1))
        