import os
import json
import requests
from bs4 import BeautifulSoup
from send_mail import gmail_send_message

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def main():
    os.system("cls")
    with open("products.json", "r") as f:
        products = json.load(f)

    for product in products:
        r = requests.get(product["link"])
        full_price = float(product["price"])

        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.find("title").text
        price = float(soup.find("span", id=product["id"])["data-price-amount"])

        if price < full_price:
            discount = full_price - price
            discount = "{:.2f}".format(discount)
            sale_price = "{:.2f}".format(price)
            message = f"{title} er nå på tilbud for kr {sale_price} (kr {discount} avslag) hos {product['store']}"
            print(message)

if __name__ == "__main__":
    main()