from django.views.generic import ListView, DetailView
from .models import Snack

class SnacksListView(ListView):
    template_name="snack_list.html"
    model = Snack
    context_object_name = "list_snacks"


class SnacksDetailView(DetailView):
    template_name=("snack_detail.html")
    model = Snack



# Views for Snacks App
# Where to create these views?
# Dig around and see if there’s a sensible spot.
# HINT There is one correct place for your app’s views.
# create SnackListView (Done)
# extend ListView (Done)
# give a template of snack_list.html (Done)
# associate Snack model (Done)
# update url patterns for project (Done)
# empty path should include snacks.urls (Done)
# update snacks app urls (Done)
# empty sub-path should be handled by SnackListView (Done)
# Don’t forget to use as_view() (Done)
# add detail view
# link snack_detail.html template (Done)
# associate Snack model (Done)
# update app urlpatterns to handle detail view (Done)
# account for primary key in url (Done)
# path would look like localhost:8000/1/ to get to snack with id of 1 (Done)