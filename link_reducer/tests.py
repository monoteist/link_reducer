from django.test import TestCase, Client
from django.urls import reverse

from .models import Link


class LinkReducerTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_short_link(self):
        # Test with a valid URL
        response = self.client.post(
            reverse("link_reducer:create_short_link"),
            {"original_link": "https://www.instagram.com/i.monoteist/"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Link.objects.count(), 1)

        # Test with an invalid URL
        response = self.client.post(
            reverse("link_reducer:create_short_link"),
            {"original_link": "not a valid url"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Link.objects.count(), 1)
        self.assertContains(response, "Некорректная ссылка!")

    def test_redirect_short_link(self):
        # Create a link in the database
        link = Link.objects.create(
            original_link="https://www.instagram.com/i.monoteist/",
            shortened_link="abc123",
        )

        # Test with a valid shortened link
        response = self.client.get(
            reverse("link_reducer:redirect_short_link", args=[link.shortened_link])
        )
        self.assertRedirects(
            response, link.original_link, status_code=302, fetch_redirect_response=False
        )

        # Test with an invalid shortened link
        response = self.client.get(
            reverse("link_reducer:redirect_short_link", args=["invalid"])
        )
        self.assertEqual(response.status_code, 404)

    def test_statistics_status_code(self):
        self.response = self.client.get(reverse("link_reducer:statistics"))
        self.assertEqual(self.response.status_code, 200)

    def test_statistics_redirect_count(self):
        link = Link.objects.create(
            original_link="https://www.example1.com/", shortened_link="abcde"
        )
        self.client.get(
            reverse("link_reducer:redirect_short_link", args=[link.shortened_link])
        )
        self.client.get(
            reverse("link_reducer:redirect_short_link", args=[link.shortened_link])
        )
