from django.views.generic import ListView, DetailView
from .models import Snack

class SnacksListView(ListView):
    template_name="snack_list.html"
    model = Snack
    context_object_name = "list_snacks"


class SnacksDetailView(DetailView):
    template_name=("snack_detail.html")
    model = Snack