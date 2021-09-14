from django.http import HttpResponse


class pagehandler(object):
    def __init__(self, htmlfilepath):
        self.htmlfilepath = htmlfilepath

    def home(self, request):
        htmlpage = open(self.htmlfilepath, "r", encoding="utf-8")
        html = htmlpage.read()
        htmlpage.close()
        return HttpResponse(html)
