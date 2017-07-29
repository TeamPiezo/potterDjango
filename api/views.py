# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Sloats
from datetime import date, datetime, time
import json as simplejson

# Create your views here.


def book_a_slot(request):
    username = 'default'
    d = request.GET.get('date', datetime.now().strftime('%Y-%m-%d'))
    d = datetime.strptime(d, '%Y-%m-%d')
    t = request.GET.get('starttime')
    t = datetime.strptime(t, '%H:%M')
    slot_time = datetime.combine(date(d.year, d.month, d.day), time(t.hour))
    booked_by_user = request.GET.get('bookedbyuser', 'default')
    # we added this so that we can have pet note type with '&' in between them
    # we replace the '&' with '_' from front-end so that it can be send
    # here we are converting it back to the previous(same) name
    try:
        bookslot = Sloats(username= username, start_time = slot_time,
             booked_by_user = booked_by_user)
        bookslot.save()
        return HttpResponse(simplejson.dumps({"status": "success"}))
    except Exception as e:
        print(e)
    return HttpResponse(simplejson.dumps({"status": "duplicate"}))

def find_a_slot(request):
    slotdate = request.GET.get('date')
    # we added this so that we can have pet note type with '&' in between them
    # we replace the '&' with '_' from front-end so that it can be send
    # here we are converting it back to the previous(same) name
    all_sloats = list(range(8,24))
    start_date = datetime.strptime(slotdate, "%Y-%m-%d")
    date_min = datetime.combine(date.today(), time.min)
    date_max = datetime.combine(date.today(), time.max)
    # booked_sloats = Sloats.objects.filter(
    #     start_time__year=str(start_date.year),
    #     start_time__month=str(start_date.month),
    #     start_time__day=str(start_date.day)
    # ).only('start_time')
    booked_sloats = Sloats.objects.filter(start_time__range=(date_min, date_max)).only('start_time')
    booked_sloats = [i.start_time.hour for i in list(booked_sloats)]
    free_sloats = list(set(all_sloats) - set(booked_sloats))
    return HttpResponse(simplejson.dumps({"status": "success", "freesloats": free_sloats}))