from collections import defaultdict

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding="cp1251") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    current_page = request.GET.get('page', 1)
    # pages = request.GET['page']
    paginator = Paginator(data, 20)
    page_obj = paginator.get_page(current_page)
    current_page=page_obj.number
    next_page_url = f'?page={page_obj.next_page_number()}' if page_obj.has_next() else None
    prev_page_url = f'?page={page_obj.previous_page_number()}' if page_obj.has_previous() else None
    return render_to_response('index.html', context={
        'bus_stations': page_obj.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
