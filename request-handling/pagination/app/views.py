from collections import defaultdict

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
import os
def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    columns = defaultdict(list)  # each value in each column is appended to a list
    with open( os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data-398-2018-08-30.csv'), newline='',encoding="cp1251") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k

    print(columns['District'][0])
    print(columns['Name'][0])
    print(columns['Street'][0])
    current_page = 1
    pages = request.GET['page']
    next_page_url = 'write your url'
    return render_to_response('index.html', context={
        'bus_stations': [{'Name': columns['Name'][0], 'Street': 'улица', 'District': 'район'}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

