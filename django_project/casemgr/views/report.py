""" report like pages for app models and data """

# from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import (AnnualProgressView, AnnualStatView,
                                       AnnualTrendView)

# from handyhelpers.views.report import get_colors

# import models
# from casemgr.models import ()


class CasemgrDashboard(View):
    """casemgr dashboard"""

    template_name = "casemgr/custom/dashboard.html"

    def get(self, request):
        """render dashboard for casemgr specific data"""
        context = {"title": "Casemgr Dashboard"}
        return render(request, self.template_name, context=context)


class CasemgrAnnualProgressView(AnnualProgressView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]


class CasemgrAnnualStatView(AnnualStatView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]


class CasemgrAnnualTrendView(AnnualTrendView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]
