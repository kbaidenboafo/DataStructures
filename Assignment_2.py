cars = {'toyota prado': 120000, 'nissan': 120000, 'bmw': 273828, 'honda': 43900, 'Hyundai': 57000, 'mitubushi': 67000,
        'tesla': 45000, 'pontiac': 65000, 'benz': 54000, 'opel': 65000, 'alpha romero': 590003, 'matiz': 50000, 'acura': 590000,
        'ford': 770000, 'kia': 55000, 'chevolet': 69000, 'subaru': 96000, 'audi': 650000, 'culvert': 78400,'gmc': 68000,
        'porsche': 54000, 'jaguar': 580000, 'bentley': 580000, 'renault': 58600, 'suzuki': 90000, 'lexus': 34000,
        'land rover': 550000, 'range rover': 100000, 'dodge': 580000, 'ram': 99999}

prompt = input('Which car do you wish to purchase? ')
if prompt in cars:
        print('Yes, we have ' + prompt.upper() + ' available.')
        price = cars[prompt]
        print(prompt.upper() + ' goes for $' + str(price))


else:
        print("Sorry, we don't have" + prompt + ' available. These are the cars we have:')
        a = cars.keys()
        print(a)















