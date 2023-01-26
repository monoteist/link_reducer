import random
import string

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


from .models import Link


def create_short_link(request):
    if request.method == "POST":
        original_link = request.POST["original_link"]
        val = URLValidator()

        try:
            val(original_link)
            shortened_link = "".join(
                random.choices(string.ascii_letters + string.digits, k=6)
            )
            Link.objects.get_or_create(
                original_link=original_link, shortened_link=shortened_link
            )
            return render(
                request,
                "link_reducer/create_short_link.html",
                {"shortened_link": shortened_link},
            )
        except ValidationError:
            messages.error(request, "Некорректная ссылка!")
    return render(request, "link_reducer/create_short_link.html")


def redirect_short_link(request, shortened_link):
    link = get_object_or_404(Link, shortened_link=shortened_link)
    link.redirect_count += 1
    link.save()
    return redirect(link.original_link)


def statistics(request):
    links = Link.objects.all()
    return render(request, "link_reducer/statistics.html", {"links": links})
