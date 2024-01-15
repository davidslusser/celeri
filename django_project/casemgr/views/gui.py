from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views import HandyHelperIndexView

# import models
# from casemgr.models import ()

# import forms
# from casemgr.forms import ()


class Index(HandyHelperIndexView):
    """render the casemgr index page"""

    title = """Casemgr"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/casemgr/dashboard",
            "icon": "fas fa-tachometer-alt",
            "title": "Dashboard",
            "description": "Dashboard for Casemgr ",
        },
        {
            "url": "/casemgr/rest",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List RESTful APIs for Casemgr",
        },
    ]
    protected_item_list = []
    protected_group_name = "admin"


# class ListMyModels(HandyHelperListPlusCreateAndFilterView):
#     """list available MyModel entries"""
#     queryset = MyModel.objects.all()
#     title = "MyModel"
#     table = "myapp/table/mymodels.htm"


# class DetailMyModel(DetailView):
#     model = MyModel
#     template_name = 'myapp/detail/mymodel.html'


class Test(View):
    template_name = "casemgr/custom/test3.html"

    def get(self, request):
        """render dashboard for casemgr specific data"""
        context = {"title": "Casemgr Dashboard"}
        return render(request, self.template_name, context=context)
