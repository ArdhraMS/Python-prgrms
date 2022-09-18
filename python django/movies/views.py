#Print total number of movies
from json import load
with open("movies.json",encoding="UTF-8") as f:
    data=load(f)
print(len(data))

#To print the type of genres or unique geners
def unique_genres(data):
    return[ for m in data if ]


#movie_names  released in 2015

# in which year most number of movies released