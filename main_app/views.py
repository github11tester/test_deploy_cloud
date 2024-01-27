from django.shortcuts import render
from django.views import View


class BasePageView(View):
    def get(self, request):
        return render(request, 'main_app/base.html')
