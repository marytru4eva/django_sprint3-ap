from django.shortcuts import render


def csrf_failure(request, reason=''):
    """Обработка ошибки 403 CSRF"""
    return render(request, 'pages/403csrf.html', status=403)


def page_not_found(request, exception):
    """Обработка ошибки 404"""
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    """Обработка ошибки 500"""
    return render(request, 'pages/500.html', status=500)


def about(request):
    """Страница 'О проекте'"""
    return render(request, 'pages/about.html')


def rules(request):
    """Страница 'Правила'"""
    return render(request, 'pages/rules.html')
