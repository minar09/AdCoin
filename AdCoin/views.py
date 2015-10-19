
# -*- coding: utf-8 -*-

# Create your views here.
from _ast import BitAnd
import datetime
import inspect
import itertools
from mimetypes import MimeTypes
import operator
import os
import re
import time
from django.contrib.admin.templatetags.admin_list import items_for_result
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.storage.base import Message
from django.core.context_processors import csrf
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db import connection
from django.db.models.sql.query import Query
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template


def HomePage(req):
    templ = get_template('HomePage.html')
    variables = Context({})
    output = templ.render(variables)
    return HttpResponse(output)
