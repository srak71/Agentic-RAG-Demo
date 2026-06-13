from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent



# DEMO DATABASE - PRODUCTS
PRODUCTS = {
    "wireless headphones": {"price": 79.99,  "rating": 4.6, "description": "Over-ear Bluetooth, 30-hr battery, active noise cancellation."},
    "smart watch":         {"price": 199.99, "rating": 4.3, "description": "Tracks heart rate and sleep. 5-day battery, water-resistant."},
    "mechanical keyboard": {"price": 129.00, "rating": 4.8, "description": "Tenkeyless, Cherry MX Brown switches, per-key RGB."},
    "laptop stand":        {"price": 34.99,  "rating": 4.5, "description": "Adjustable aluminium, fits 11-17 inch laptops, folds flat."},
}

@tool
def get_product(name: str) -> str:
    """Look up a product by name and return its price, rating, stock, and description."""
    p = PRODUCTS.get(name.lower())
    if not p:
        return f"Product not found. Available: {', '.join(PRODUCTS)}"
    return str(p)



# AGENT 1 - PRODUCT AGENT
#
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

agent = create_agent(
    llm,
    tools=[get_product],
    system_prompt="You are a helpful product assistant for an online tech store.",
)

def ask(question: str):
    """Send a user question to the product agent and display the response. No return value."""
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(result["messages"][-1].content)

# test ask()
ask("What can you tell me about the wireless headphones?")
# this call to ask() does following
#
# 1. extracts product name "wireless headphones" from the question
# 2. calls get_product("wireless headphones") to retrieve product details
# 3. returns the product details to the user in a human readable answer
# 
# Output: "The wireless headphones are priced at $79.99, have a rating of 4.6, and come with features 
# such as over-ear Bluetooth, 30-hour battery life, and active noise cancellation."




# DEMO DATABASE - REVIEWS
REVIEWS = {
    "wireless headphones": {"reviews": 1262, "rating": 4.6},
    "smart watch":         {"reviews": 340,  "rating": 3.9},
    "mechanical keyboard": {"reviews": 67,   "rating": 4.8},
    "laptop stand":        {"reviews": 781,  "rating": 4.5},
}

@tool
def get_review(name: str) -> str:
    """Look up a product review by a product name. Return the product name, number of reviews and rating"""
    r = REVIEWS.get(name.lower())
    if not r:
        return f"Review not available for this product"
    return str(r)




# AGENT 2 - PRODUCT + REVIEW AGENT
#
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

agent2 = create_agent(
    llm,
    tools=[get_product, get_review],
    system_prompt="You are a helpful product assistant for an online tech store.",
)

def ask2(question: str):
    result = agent2.invoke({"messages": [{"role": "user", "content": question}]})
    print(result["messages"][-1].content)
    
# test ask2()
ask2("how do people like smart watch?")
# this call to ask2() does following
# 
# 1. extracts product name "smart watch" from the question
# 2. calls get_review("smart watch") to retrieve review details
# 3. returns the review details to the user in a human readable answer
# 4. calls get_product("smart watch") to retrieve product details
# 
# Output: "People generally like smart watches. The smart watch has a rating of 4.3 out of 5 and 
# has 340 reviews with an average rating of 3.9. It is priced at $199.99 and has features such as 
# tracking heart rate and sleep, a 5-day battery, and is water-resistant.