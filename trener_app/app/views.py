from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Seria
from .models import Cwiczenie


# Create your views here.


class TreningView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        uzytkownik = request.user
        serie = Seria.objects.filter(podopieczny = uzytkownik)


        context = {
            "serie": serie,
            "user": uzytkownik
        }
        return render(request, "plan_treningowy.html", context)