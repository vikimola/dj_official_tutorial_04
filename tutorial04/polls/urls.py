from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.polls, name="polls"),
#     path("<int:category_id>", views.choices, name="choices"),
#     path("<int:category_id>/vote", views.vote, name="vote"),
#     path("<int:category_id>/results", views.results, name="results"),
#     path("cookie", views.cookie, name="cookie"),
# ]

urlpatterns = [
    path("", views.CategoryListView.as_view(), name="polls"),
    path("<int:pk>", views.ChoicesView.as_view(), name="choices"),
    path("<int:category_id>/vote", views.vote, name="vote"),
    path("<int:pk>/results", views.ResultsView.as_view(), name="results")
]
