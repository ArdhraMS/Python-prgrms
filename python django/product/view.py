from product.models import items
class products:
    def list(self,*args,**kwargs):
        all_products=items
        if "category" in kwargs:
            cat=kwargs.get("category")
            all_products=[p for p in all_products if p.get("category")==cat]
        return all_products
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        item=[i for i in items if i.get("id")==id]
        return item
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        item=[i for i in items if i.get("id")==id][0]
        items.remove(item)
        return item
    def create(self,*args,**kwargs):
        data=kwargs.get("data")
        items.append(data)
        return data
    def update(self,*args,**kwargs):
        id=kwargs.get("id")
        data=kwargs.get("data")
        instance=[i for i in items if i.get("id")==id][0]
        instance.update(data)
        return instance
p=products()
print(p.list())
print(p.list(category="jewelery")) #kwargs accept condition as dict
print(p.retrieve(id=12))
print(p.destroy(id=1))
print(p.list())
data={
    "id": 21,
    "title": "Watch",
    "price": 64000,
    "description":"perfect fit",
    "category":"electronics",
    "image":"https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_.jpg",
    "rating": {
      "rate": 4.3,
      "count": 203
    }
}
print(p.create(data=data))
print(p.list())
data1={
    "price":3000,
    "description":"perfect"
}
print(p.update(id=2,data=data1))
print(p.list())