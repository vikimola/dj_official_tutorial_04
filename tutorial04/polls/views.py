from unicodedata import category

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Category, Choice

# Create your views here.

tml_path = "polls/template/polls/"


def cookie(request):
    print(request.COOKIES)
    resp = HttpResponse("C is for cookie and thats all..")
    resp.set_cookie("zap", 36)  # no expiration date-> until browser is closed
    resp.set_cookie("sai", 42, max_age=1000)  # exp date: 1000 seconds
    return resp


def polls(request):
    categories = Category.objects.all()
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    # if num_visits > 5:
    #     del (request.session['num_visits'])
    # for category in categories:
    #     print(category)
    #     print(category.id)
    return render(request, tml_path + "polls.html", {"categories": categories, "num_visits": num_visits})


def choices(request, category_id):
    print("UFKTFKTYIDKJY")
    print(category_id)

    # choiceses = Choice.objects.filter(category_name=category_id)
    category = Category.objects.get(id=category_id)
    print(category)
    return render(request, tml_path + "choices.html", {"category": category})


def vote(request, category_id):
    # if request.method == "POST":
    #     choice_id = request.POST.get("choice")
    #     print("YUGKBUYG")
    #     print(choice_id)
    #     choice = Choice.objects.get(id=int(choice_id))
    #     print("GFCVJCOVBYUGKBUYG")
    #     print(choice)
    #     choice.vote_num += 1
    #     choice.save()
    # else:
    #     category = Category.objects.get(id=category_id)
    #     return render(request, tml_path + "choices.html", {"category": category})
    #
    # # return render(request, tml_path + "results.html")
    # return HttpResponseRedirect(reverse("results", args=[category_id, ]))  # redirect to another url

    category = get_object_or_404(Category, id=category_id)
    try:
        choice_id = request.POST.get("choice")
        choice = Choice.objects.get(id=int(choice_id))
    except TypeError:
        message = "You gotta select an option to vote"
        return render(request, tml_path + "choices.html", {"category": category, "message": message})
    else:

        choice.vote_num += 1
        choice.save()
    return HttpResponseRedirect(reverse("results", args=[category_id, ]))  # redirect to another url


def results(request, category_id):
    category = Category.objects.get(id=category_id)
    # print(category)
    # choices = category.choice_set.all()
    # for c in choices:
    #     print(c.choice_text)
    return render(request, tml_path + "results.html", {"category": category})


class CategoryListView(ListView):
    model = Category
    template_name = tml_path + "polls.html"
    context_object_name = "categories"


class ChoicesView(DetailView):
    model = Category
    template_name = tml_path + "choices.html"
    context_object_name = "category"
    print("GUYYYYYYYB")
    print(category)


class ResultsView(DetailView):
    model = Category
    template_name = tml_path + "results.html"
    context_object_name = "category"
