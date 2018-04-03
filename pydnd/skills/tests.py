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


class TestSpecialAbilityGet(APITestCase):

    fixtures = ['pydnd/fixtures/db_fixture.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.SpecialAbilityGet.as_view()
        self.uri = 'special_abilities/'

    def test_get_by_name(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='Amphibious')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)

    def test_get_by_name_case_insensitive(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='amphibioUs')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)

    def test_get_by_id(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='2')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)

    def test_non_ability_name(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='NOT_ABILITY')
        self.assertEqual(response.status_code, 404,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))

    def test_non_ability_id(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='99999')
        self.assertEqual(response.status_code, 404,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))


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


class TestActionsGet(APITestCase):

    fixtures = ['pydnd/fixtures/db_fixture.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.ActionGet.as_view()
        self.uri = 'actions/'

    def test_get_by_name(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='Multiattack')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)

    def test_get_by_name_case_insensitive(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='multiatTack')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)

    def test_get_by_id(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='2')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)

    def test_non_action_name(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='NOT_ACTION')
        self.assertEqual(response.status_code, 404,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))

    def test_non_action_id(self):
        request = self.factory.get(self.uri)
        response = self.view(request, name_or_id='99999')
        self.assertEqual(response.status_code, 404,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))
