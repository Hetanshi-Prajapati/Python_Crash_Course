"""sandwich_orders=['a','b','c','d','e','f','g','h']
finish_orders=[]
for sandwich_order in sandwich_orders:
    print(f"I mad your {sandwich_order}")
    finish_orders.append(current_order)
    
    print(f"Current order: {sandwich_order.title()}")
    current_order=sandwich_orders.pop()
    
    # print(f"Current order: {sandwich_order.title()}")
    
    
for finish_order in finish_orders:
    print(finish_order)
"""
sandwich_orders = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
finished_sandwiches = []

# Loop through the sandwich orders and process each one
for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

# After all sandwiches are made, list the finished sandwiches
print("\nAll sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich.title()} sandwich")
