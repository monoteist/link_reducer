import random
import string

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.contrib import messages
from django.shortcuts import render


from .models import Link


def create_short_link(request):
    if request.method == "POST":
        original_link = request.POST["original_link"]
        val = URLValidator()

        try:
            val(original_link)
            shortened_link = "localhost:8000/" + "".join(
                random.choices(string.ascii_letters + string.digits, k=6)
            )
            link = Link(original_link=original_link,
                        shortened_link=shortened_link)
            link.save()
            return render(
                request,
                "link_reducer/create_short_link.html",
                {"shortened_link": shortened_link},
            )
        except ValidationError:
            messages.error(request, 'Некорректная ссылка!')
    return render(request, "link_reducer/create_short_link.html")
