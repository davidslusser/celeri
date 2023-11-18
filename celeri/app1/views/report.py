""" report like pages for app models and data """

# from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import AnnualTrendView, AnnualStatView, AnnualProgressView

# from handyhelpers.views.report import get_colors

# import models
# from app1.models import ()


class App1Dashboard(View):
    """app1 dashboard"""

    template_name = "app1/custom/dashboard.html"

    def get(self, request):
        """render dashboard for app1 specific data"""
        context = {"title": "App1 Dashboard"}
        return render(request, self.template_name, context=context)


class App1AnnualProgressView(AnnualProgressView):
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


class App1AnnualStatView(AnnualStatView):
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


class App1AnnualTrendView(AnnualTrendView):
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
