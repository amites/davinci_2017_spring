def mix_fruit(arr):
    normal = ['banana', 'orange', 'apple', 'lemon', 'grapes', ]
    price_normal = 5
    special = ['avocado', 'strawberry', 'mango', ]
    price_special = 7
    price_extra_special = 9

    total_price = 0

    for fruit in arr:
        fruit = fruit.lower()
        if fruit in normal:
            total_price += price_normal
        elif fruit in special:
            total_price += price_special
        else:
            total_price += price_extra_special

    total_price = total_price / len(arr)
    return int(round(total_price))
