item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
print(f"Vybraný předmět je {item['title']} a stojí {item['price']} Kč.")
if "weight" in item:
    print("Hmotnost přemětu je" ,item["weight"], "kg") 
else:
    print("Hmotnost není zadána")
item["price"] = 929
item["weight"] = 0.4
key = "price"
item[key] = 929
print(item)