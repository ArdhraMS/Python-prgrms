from json import load
with open("countrydata.json",encoding="UTF-8") as f:
    data=load (f)
print(len(data))
# for c in data:
#     print(c.get("name"))
all_country_names=[c.get("name") for c in data] #String comprehension of above stmts.
print(all_country_names)

#To print the details of the country name.
def get_country_details(name):
    # for c in data:
    #     if c.get("name")==name:
    #         return c
    return [c for c in data if c.get("name")==name][0] #List comprehension.
# detials=get_country_details("India")
# print(detials)
print(get_country_details("India")) #The above code can also be written as.

#To print country capital.
def get_country_capital(name):
   c_data=get_country_details(name)
   if c_data: #Here if c_data means if c_data is present.
       return c_data.get("capital")
    # return[c.get("capital") for c in data if c.get("name")==name]
#The above code is  to def the function withoute get_country_details.
print(get_country_capital("India"))

#To print the population of the country name.
def get_country_population(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("population")
print(get_country_population("India"))

#To print the name of the currency of the country name.
def get_country_currency(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("currencies")[0].get("name")
print(get_country_currency("India"))


#To print the names of the countries which share the borders of the country name.
def get_country_borders(name):
    c_data=get_country_details(name)
    border_list=c_data.get("borders")
    print(border_list)
    b_names=[c.get("name") for c in data if c.get("alpha3Code") in border_list]
    return b_names
#Here if the aplha3code of data is present in boarders of country name it wil print the border country name.
print(get_country_borders("India"))


#To print the most populated country--->use max()
# max_population_country=max(data,key=lambda c:c.get("population"))
# print(max_population_country)
#The same can be defined as function.
def get_max_populated_country():
    c_data=max(data,key=lambda c:c.get("population"))
    return c_data.get("name")
print(get_max_populated_country())

#Print the language name of the country name.
def get_country_language(name):
    c_data=get_country_details(name)
    return [l.get("name") for l in c_data.get("languages")]
print(get_country_language("India"))
