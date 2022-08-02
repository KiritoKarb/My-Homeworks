from pprint import pprint
with open('file.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        try:
            quantity = int(line)
            ingredients = []
            for item in range(quantity):
                ingredient = {}
                data = file.readline().strip().split(' | ')
                ingredient['ingredient_name'] = data[0]
                ingredient['quantity'] = int(data[1])
                ingredient['measure'] = data[2]
                ingredients.append(ingredient)
                cook_book[dish_name] = ingredients
            file.readline()
        except ValueError:
            dish_name = line.strip()


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']*person_count
            else:
                ingredients[ingredient['ingredient_name']] = {'measure': ingredient['measure'],'quantity': ingredient['quantity']*person_count}
    return pprint(ingredients)

pprint(cook_book)
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 7)