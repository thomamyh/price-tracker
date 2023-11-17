# Price Tracker

A program that informs me when products I am interested in is on sale. Instad of me browsing to the website to look up the product, I can just run the program from the command line. At the moment, it only works on Europris, but the plan is to extend to other stores and products as needed.

## Usage

- Clone the repo
- Install the required packages
```
pip install -r requirements.txt
```
- Create a file called `products.json`
```
[
  {
  "store": Name of the store
  "link": Link to the product
  "price": Current price
  "id": product-id
  }
]
```
- Take a look at `example-products.json`
- The product-id can be found by looking up the product on the website, viewing the source and searching for "product-price-". This will only give one match.