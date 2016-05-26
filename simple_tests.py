from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_multiply_ok(self):
        url = "/x/4/5/"
        expected = "4 x 5 = 20"

        response = self.client.get(url)

        # self.assertEqual(resp.status_code, 200)
        self.assertContains(response, expected)

    def test_page_not_exist(self):
        url = 'age/something/really/weird/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
