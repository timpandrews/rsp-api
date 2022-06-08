from django.http import HttpResponse
import datetime


def home(request):
    now = datetime.datetime.now()
    html = "<html><body>"
    html += "<h1>RSP-API</h1>"
    html += "It is now %s." % now
    html += "<br><br><div><a href='/api/docs/'>API Docs</a><div>"
    html += "<br><div><a href='/admin/'>Admin</a><div>"
    html += "</body></html>"
    return HttpResponse(html)
