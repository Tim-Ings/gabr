import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from user.forms import PostForm
from user.models import UserProfile, Notification, Trend


def ajax_load_trends(request):
    if not request.is_ajax():
        return HttpResponse('')
    try:
        current_user = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return HttpResponse('')

    trends = []
    for trend in Trend.objects.all():
        trends.append(trend.tag)

    response = {
        'trends': trends
    }

    return HttpResponse(json.dumps(json.dumps(response)))
