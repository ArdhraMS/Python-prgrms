#print all framework name, so we have to import framework to views.
from framework.models import frameworks as fws
for fw in fws:
    print(fw.get("name"))
#The same can be written in one sentence using string comprehension.
print([fw.get("name") for fw in fws])
print([fw.get("language") for fw in fws])

#To print name of language whose rating is greater than 4.
for fw in fws:
    if fw.get("rating")>4:
        print(fw.get("name"))
#The same can be written in same sentence.
print([fw.get("name") for fw in fws if fw.get("rating")>4])

#Print the framework of python.
print([fw.get("name") for fw in fws if fw.get("language")=="python"])

#Print framework with backend
print([fw.get("name") for fw in fws if fw.get("belongsto")=="backend"])

#Print the top rated framwork.
top_rated=max(fws,key=lambda m:m.get("rating"))
print(top_rated.get("name"))