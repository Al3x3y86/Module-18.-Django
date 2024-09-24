from django.shortcuts import render


def main_page(request):
    return render(request, 'third_task/platform.html')


def shop_page(request):
    games = {
        'Atomic Heart': 'Купить',
        'Cyberpunk 2077': 'Купить',
        'PayDay 2': 'Купить',
    }
    return render(request, 'third_task/games.html', {'games': games})


def cart_page(request):
    return render(request, 'third_task/cart.html')
