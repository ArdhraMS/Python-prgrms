from json import load #In case of error write enconding .
with open("products.json",encoding="UTF-8") as f: #To read the datas in products.json.
    data=load(f)
print(len(data))