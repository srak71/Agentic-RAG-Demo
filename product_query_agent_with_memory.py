from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver


PRODUCTS = {
    "wireless headphones": {"price": 79.99,  "description": "Over-ear Bluetooth, 30-hr battery, active noise cancellation."},
    "smart watch":         {"price": 199.99, "description": "Tracks heart rate and sleep. 5-day battery, water-resistant."},
    "mechanical keyboard": {"price": 129.00, "description": "Tenkeyless, Cherry MX Brown switches, per-key RGB."},
    "laptop stand":        {"price": 34.99,  "description": "Adjustable aluminium, fits 11-17 inch laptops, folds flat."},
}

REVIEWS = {
    "wireless headphones": {"reviews": 1262, "rating": 4.6},
    "smart watch":         {"reviews": 340,  "rating": 3.9},
    "mechanical keyboard": {"reviews": 67,   "rating": 4.8},
    "laptop stand":        {"reviews": 781,  "rating": 4.5},
}

@tool
def get_product(name: str) -> str:
    """Look up a product by name and return its price, rating, stock, and description."""
    p = PRODUCTS.get(name.lower())
    if not p:
        return f"Product not found. Available: {', '.join(PRODUCTS)}"
    return str(p)
    
@tool
def get_review(name: str) -> str:
    """Look up a product review by a product name. Return the product name, number of reviews and rating"""
    r = REVIEWS.get(name.lower())
    if not r:
        return f"Review not available for this product"
    return str(r)    



# Agent 1 - No memory
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

agent = create_agent(
    llm,
    tools=[get_product, get_review],
    system_prompt="You are a helpful product assistant for an online tech store.",
)

def ask(question: str):
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(result["messages"][-1].content)


ask("what is the price of wireless headphones.")
# Output: "The price of the wireless headphones is $79.99."
ask("what are the reviews on this product")
# Output: "I need to know the name of the product you're looking for to provide you 
# with the reviews. Could you please provide the product name? I'll be happy to help."


# Agent 1A - With memory
memory = MemorySaver()

agent_with_memory = create_agent(
    llm,
    tools=[get_product, get_review],
    system_prompt="You are a helpful product assistant for an online tech store.",
    checkpointer=memory,
)


def ask_with_memory(question: str, thread_id: str = "default"):
    config: RunnableConfig = {"configurable": {"thread_id": thread_id}}
    result = agent_with_memory.invoke(
        {"messages": [HumanMessage(content=question)]},
        config=config,
    )
    print(result["messages"][-1].content)
    return


ask_with_memory("what is the price of wireless headphones.")
# Output: "The price of the wireless headphones is $79.99."
ask_with_memory("what are the reviews on this product")
# Now remembers "wireless headphones" from the previous turn and returns its reviews directly.
# Output: "The wireless headphones have 1262 reviews with an average rating of 4.6."
