# exc2 shopping cart

print("Vitejte v obchode\nDstupne polozky jsou: [1] HDD 8TB | [2] Mikrotik RBSXT-G5HPacD | [3] Ubiquiti Unifi Switch 8 Aggregation Switch PoE ++++++ Pro Max\nMuzete si vybrat 1 zbozi v ruznem mnoztvi")

item = int(input("Zadejte cislo zbozi: "))
price = 0
item_name = ""


if item == 1:
    price = 2000
    item_name = "HDD 8TB"
elif item == 2:
    price = 500
    item_name = "Mikrotik RBSXT-G5HPacD"
elif item == 3:
    price = 120000
    item_name = "Ubiquiti Unifi Switch 8 Aggregation Switch PoE ++++++ Pro Max"


qty = int(input("Kolik kusu: "))

final_price = price * qty

print(f"=== Uctenka ===\nZvolene zbozi: {item_name}\nCena za 1ks: {price}\nPocet ks: {qty}\nCelkova cena k zaplaceni: {final_price}\n\nPrejdete k dalsimu vydejnimu oknu a predlozte tuto uctenku\nDekujeme ze s nami nakupujete")