def top_revenue_product(products: dict, sales: dict) -> str:
    return max(products, key=lambda p: products[p] * sales[p])


# Test
products = {
    "Olma":  1500,
    "Banan": 2000,
    "Uzum":  3500,
}
sales = {
    "Olma":  120,
    "Banan": 85,
    "Uzum":  60,
}

result = top_revenue_product(products, sales)
print(f"Eng ko'p tushum keltirgan mahsulot: {result}")

# Barcha tushum qiymatlari
for p in products:
    tushum = products[p] * sales[p]
    print(f"  {p}: {products[p]} × {sales[p]} = {tushum:,} so'm")