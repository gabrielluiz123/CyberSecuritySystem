from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import validate_email


class Index(View):
    model = 'Registro'
    template_name = 'sidebar_left.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)
