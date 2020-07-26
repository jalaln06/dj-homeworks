from collections import Counter
import random
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()
int_count = 0


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    landchoice = request.GET.get('from-landing', 'original')
    if landchoice == "original":
        counter_click.update("O")
    elif landchoice == "test":
        counter_click.update("T")
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    landchoice = request.GET.get('ab-test-arg', 'original')

    if landchoice == "original":
        counter_show.update("O")
        return render_to_response('landing.html')
    else:
        counter_show.update("T")
        return render_to_response('landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    original_conversion = counter_show['O']/counter_click['O']
    test_conversion = counter_show['T'] / counter_click['T']

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
