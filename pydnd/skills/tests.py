from rest_framework.test import APITestCase, APIRequestFactory

from pydnd.skills import views


class TestSpecialAbilityList(APITestCase):

    fixtures = ['pydnd/fixtures/db_fixture.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.SpecialAbilityList.as_view()
        self.uri = 'special_abilities'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_cannot_delete(self):
        request = self.factory.delete(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    def test_cannot_put(self):
        request = self.factory.put(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    # TODO Cannot post


class TestActionsList(APITestCase):

    fixtures = ['pydnd/fixtures/db_fixture.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.SpecialAbilityList.as_view()
        self.uri = 'special_abilities'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_cannot_delete(self):
        request = self.factory.delete(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    def test_cannot_put(self):
        request = self.factory.put(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

    # TODO Cannot post
