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

    COUNTRIES = (
        ('Russia', 'Russia'),
        ('Germany', 'Germany'),
        ('United Kingdom', 'United Kingdom'),
        ('France', 'France'),
        ('Italy', 'Italy'),
        ('Spain', 'Spain'),
        ('Ukraine', 'Ukraine'),
        ('Poland', 'Poland'),
        ('Romania', 'Romania'),
        ('Netherlands', 'Netherlands'),
        ('Belgium', 'Belgium'),
        ('Czech Republic (Czechia)', 'Czech Republic (Czechia)'),
        ('Greece', 'Greece'),
        ('Portugal', 'Portugal'),
        ('Sweden', 'Sweden'),
        ('Hungary', 'Hungary'),
        ('Belarus', 'Belarus'),
        ('Austria', 'Austria'),
        ('Serbia', 'Serbia'),
        ('Switzerland', 'Switzerland'),
        ('Bulgaria', 'Bulgaria'),
        ('Denmark', 'Denmark'),
        ('Finland', 'Finland'),
        ('Slovakia', 'Slovakia'),
        ('Norway', 'Norway'),
        ('Ireland', 'Ireland'),
        ('Croatia', 'Croatia'),
        ('Moldova', 'Moldova'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Albania', 'Albania'),
        ('Lithuania', 'Lithuania'),
        ('North Macedonia', 'North Macedonia'),
        ('Slovenia', 'Slovenia'),
        ('Latvia', 'Latvia'),
        ('Estonia', 'Estonia'),
        ('Montenegro', 'Montenegro'),
        ('Luxembourg', 'Luxembourg'),
        ('Malta', 'Malta'),
        ('Iceland', 'Iceland'),
        ('Andorra', 'Andorra'),
        ('Monaco', 'Monaco'),
        ('Liechtenstein', 'Liechtenstein'),
        ('San Marino', 'San Marino'),
        ('Holy See', 'Holy See')
    )

    INFORMATION = (
        ('phone', 'phone'),
        ('email', 'email'),
        ('address', 'address'),
        ('logo', 'logo')
    )
