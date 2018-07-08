from django.views.generic.base import TemplateView


class ChatterBotAppView(TemplateView):
    template_name = "iChat.html"


def chatt(request):
    text = request.get()
    print(text)