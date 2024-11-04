# Sample eco-friendly product recommendations
sustainable_products = {
    "Toothbrush": "Bamboo Toothbrush",
    "Straws": "Stainless Steel Straws",
    "Bags": "Reusable Cotton Bag",
    "Bottles": "Glass Water Bottle",
    "Shampoo": "Refillable Shampoo Bottle"
}

# Function to suggest sustainable alternatives
def suggest_sustainable_product(product):
    return sustainable_products.get(product, "No eco-friendly option found for this product.")

# User input
product = "Toothbrush"  # Example product

# Suggest eco-friendly alternative
suggestion = suggest_sustainable_product(product)
print(f"Eco-friendly alternative for {product}: {suggestion}")
