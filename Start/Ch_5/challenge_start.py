# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# process each order
for order in test_orders:
    print("-----------")
    totalPrice = 0.0
    for a in order:
        match a:
            case "shirt"|"pants"|"jacket"|"dress" as garment,size, starch, same_day:
                totalPrice += 12.95
                if starch:
                    totalPrice += 2.0
                if same_day:
                    totalPrice += 10.0
                print(f"Dry Clean:({size}) {garment}",
                      "' Starched' if starch else ''",
                      "' same-day' if same_day else ''")
            case str() as description, weight:
                totalPrice += 4.95*weight
                if weight > 15:
                    totalPrice -= 4.95*weight*0.1
                print(f"Wash/Fold: {description}, weight: {weight}")
            case "comforter"|"cover" as btype, dryclean, size:
                print(f"Blanket: ({size}) {btype}",
                      " ' Dry clean' if dryclean else ''")
                totalPrice += 25.0
    print(f"Order total: {totalPrice:.2f}")
    print("-----------")