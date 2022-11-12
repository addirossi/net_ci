from django.test import TestCase, Client


class TestSomeCase(TestCase):
    def test_my_view(self):
        client = Client()
        response = client.get('/test/')
        self.assertEqual(response.content.decode(), "Проверка работоспособности!")
