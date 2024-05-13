import requests
from bs4 import BeautifulSoup
import csv

# URL of the Amazon product category
url = "https://www.amazon.com/gp/bestsellers/amazon-devices/ref=zg_bs_nav_0"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the product elements on the page
product_elements = soup.find_all("div", {"data-component-type": "s-search-result"})

# Create a list to store the product data
product_data = []

# Extract the product information from each product element
for product in product_elements:
    try:
        name = product.find("span", class_="a-size-medium").text.strip()
        price = product.find("span", class_="a-offscreen").text.strip()
        rating = product.find("span", class_="a-icon-alt").text.strip()
        rating = rating.split(" ")[0]  # Extract the numerical rating

        # Add the product data to the list
        product_data.append([name, price, rating])
    except AttributeError:
        continue  # Skip products without the required information

# Open a CSV file for writing
with open("amazon_products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Name", "Price", "Rating"])

    # Write the product data to the CSV file
    writer.writerows(product_data)

print("Product data has been saved to amazon_products.csv")
