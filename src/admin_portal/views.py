from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class AdminPortalView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    permission_required = 'prod_card.delete_books'
    login_url = 'admin_portal:admin_portal'
    template_name = 'admin_portal/portal_detail.html'
