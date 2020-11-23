import json

from django.conf import settings
from django.http import HttpResponse


def color_view(request):
    color = "blue"
    if settings.UNLEASH_CLIENT.is_enabled("blue-or-green"):
        color = "green"
    return HttpResponse(json.dumps({"color": color}))
