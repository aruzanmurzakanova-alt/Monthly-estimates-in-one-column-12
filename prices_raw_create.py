import pandas as pd

data = {
    "product": [
        "Apple", "Banana", "Orange", "Milk", "Bread",
        "Cheese", "Butter", "Eggs", "Chicken", "Beef",
        "Fish", "Rice", "Pasta", "Tomato", "Potato",
        "Onion", "Carrot", "Cucumber", "Juice", "Water",
        "Coffee", "Tea", "Sugar", "Salt", "Flour",
        "Yogurt", "Ice Cream", "Chocolate", "Cookies", "Chips"
    ],
    "price": [
        "100", "200,5", "300 000", "450.75", "abc",
        "1 200", "850,3", None, "2300", "5 000",
        "700.99", "120", "340,7", "89", "150",
        "60,5", "75 000", "110", "200.0", "50",
        "999,99", "450", "300", "25", "700,0",
        "120,25", "1 500", "800", "350,5", "400"
    ]
}

df = pd.DataFrame(data)

df.to_csv("prices_raw.csv", index=False, encoding="utf-8")

print("✅ Файл prices_raw.csv с большим количеством товаров создан!")