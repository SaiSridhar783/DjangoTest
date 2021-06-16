from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("all-reviews", views.ReviewListView.as_view()),
    path("all-reviews/favourite", views.AddFavouriteView.as_view()),
    path("all-reviews/<int:pk>",
         views.SingleReviewView.as_view(), name="single-review")
]
