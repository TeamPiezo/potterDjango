# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Sloat, Sloats, MeetingNotes, Tasks
# Register your models here.
admin.site.register(Sloat)
admin.site.register(Sloats)
admin.site.register(MeetingNotes)
admin.site.register(Tasks)