class AllInfo:
    CITY_NAME = (
        ('Baden-Württemberg', 'Baden-Württemberg'),
        ('Bayern', 'Bayern'),
        ('Berlin', 'Berlin'),
        ('Brandenburg', 'Brandenburg'),
        ('Bremen', 'Bremen'),
        ('Hamburg', 'Hamburg'),
        ('Hessen', 'Hessen'),
        ('Niedersachsen', 'Niedersachsen'),
        ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'),
        ('Nordrhein-Westfalen', 'Nordrhein-Westfalen'),
        ('Rheinland-Pfalz', 'Rheinland-Pfalz'),
        ('Saarland', 'Saarland'),
        ('Sachsen', 'Sachsen'),
        ('Sachsen-Anhalt', 'Sachsen-Anhalt'),
        ('Schleswig-Holstein', 'Schleswig-Holstein'),
        ('Thüringen', 'Thüringen')
    )

    FOOD_TYPE = (
        ('Fruits and Vegetables', 'Fruits and Vegetables'),
        ('Dry goods and Seasonings', 'Dry goods and seasonings'),
        ('Rice Flour and Noodles', 'Rice Flour and Noodles'),
        ('Condiments and Sauces', 'Condiments and Sauces'),
        ('Normal and Alcoholic Beverages', 'Normal and Alcoholic Beverages'),
        ('Snack', 'Snack'),
        ('Frozen Products', 'Frozen Products'),
        ('Other', 'Other')
    )

    WAITING = 'Waiting'
    SHIPPING = 'Shipping'
    DELIVER = 'Delivered'

    DELIVER_TYPE = (
        (WAITING, 'Waiting for delivery'),
        (SHIPPING, 'In the process of shipping'),
        (DELIVER, 'Delivered')
    )

    PAYMENT_TYPE = (
        ('PayPal', 'PayPal'),
        ('BankTransfer', 'BankTransfer'),
    )
