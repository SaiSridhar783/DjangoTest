from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Have a Nice Day."

        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=1)

        return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
