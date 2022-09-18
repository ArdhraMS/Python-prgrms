# Print no of mobiles.
from mobileapp.models import mobiles
print(len(mobiles))
# Print 5g mobile names.
print([mob.get("name") for mob in mobiles if mob.get("band")=="5g"])
# Costly mobile.
costly_mobile=max(mobiles,key=lambda m:m.get("price"))
print(costly_mobile.get("name"))
# Cheapest mobile.
cheapest_mobile=min(mobiles,key=lambda m:m.get("price"))
print(cheapest_mobile.get("name"))
# Print AMOLED display mobile names.
print([mob.get("name") for mob in mobiles if mob.get("display")=="AMOLED"])
# ### Sort mobiles based on price.
# ### mobiles.sort(key=lambda m:m.get("price"),reverse=True)
# ###print(mobiles)
# # Print samsung 5g mobiles.
# print([mob.get("name") for mob in mobiles if mob.get("name")=="samsung" and mob.get("band")=='5g'])
# # Print coslty Samsung mobile.
# coslty_samsung=max(mobiles,key=lambda n:m.get("price"))
