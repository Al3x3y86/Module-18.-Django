from django.shortcuts import render


def main_page(request):
    return render(request, 'fourth_task/platform.html')


def shop_page(request):
    games = ['Atomic Heart',
             'Cyberpunk 2077',
             'PayDay 2']
    return render(request, 'fourth_task/games.html', {'games': games})


def cart_page(request):
    return render(request, 'fourth_task/cart.html')
