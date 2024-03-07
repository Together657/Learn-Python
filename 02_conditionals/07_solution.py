order_size = "extra shot"
# 	The size of the orders to place. Must be one of:
# 	- "small": places a small market order (0.01 BTC    )

extra_shot = True


if extra_shot:
    coffee = order_size + " coffee with shot"
else:
    coffee = order_size + " coffee"
print(" order ", coffee)