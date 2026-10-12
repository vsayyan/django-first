import json

from django.test import TestCase
class PagesTests(TestCase):

    def test_home_returns_200_and_text(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Django!")

    def test_hello_with_name(self):
        response = self.client.get("/hello/Vahe/")
        self.assertContains(response, "Hello, Vahe!")

    def test_api_status_returns_json(self):
        response = self.client.get("/api/status/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(json.loads(response.content), {"status": "ok", "framework": "django"})

    def test_unknown_url_returns_404(self):
        self.assertEqual(self.client.get("/nope/").status_code, 404)
        
    def test_post_not_allowed_on_home(self):
        self.assertEqual(self.client.post("/").status_code, 405)