from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'sushi': {
        'тунец, г': 0.5,
        'лосось, г': 0.5,
        'креветка, г': 0.5,
        'сом, г': 0.5,
        'рис, г': 0.5,
    },
    # можете добавить свои рецепты ;)
}
servings_1 = [1, 2, 3, 4, 5]

def index(request, recipe):
    # Создаем копию рецепта, чтобы не изменять глобальные данные
    recipe_copy = {ingredient: amount for ingredient, amount in DATA[recipe].items()}
    servings = int(request.GET.get('servings', 1))
    for ingredient, amount in recipe_copy.items():
        recipe_copy[ingredient] = amount * servings



    context = {
        'recipe': recipe_copy,
        'servings': servings_1
    }
    return render(request, 'calculator/index.html', context)


def start(request):

    return render(request, 'calculator/start.html', {'DATA': DATA})
