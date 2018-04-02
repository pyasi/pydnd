from rest_framework.test import APITestCase, APIRequestFactory

from pydnd.monsters import views


class TestMonsterList(APITestCase):

    fixtures = ['pydnd/fixtures/db_fixture.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MonsterList.as_view()
        self.uri = 'monsters'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_delete(self):
        request = self.factory.delete(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 202,
                         'Expected Response Code 202, received {0} instead.'
                         .format(response.status_code))

    # def test_post(self):
    #     request = self.factory.post(self.uri, )


class TestMonsterGetter(APITestCase):

    fixtures = ['pydnd/fixtures/db_fixture.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MonsterGet.as_view()
        self.uri = 'monsters/'

    def test_get_by_name(self):
        request = self.factory.get(self.uri)
        response = self.view(request, 'Aboleth')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)
        self.assertTrue(response.data['special_abilities'])
        self.assertTrue(response.data['actions'])

    def test_get_by_name_case_insensitive(self):
        request = self.factory.get(self.uri)
        response = self.view(request, 'aboleTh')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)
        self.assertTrue(response.data['special_abilities'])
        self.assertTrue(response.data['actions'])

    def test_get_by_id(self):
        request = self.factory.get(self.uri)
        response = self.view(request, '2')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)
        self.assertTrue(response.data['special_abilities'])
        self.assertTrue(response.data['actions'])

    def test_non_monster_name(self):
        request = self.factory.get(self.uri)
        response = self.view(request, 'NOT_MONSTER')
        self.assertEqual(response.status_code, 204,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))
        self.assertFalse(response.data)

    def test_non_monster_id(self):
        request = self.factory.get(self.uri)
        response = self.view(request, '99999')
        self.assertEqual(response.status_code, 204,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))
        self.assertFalse(response.data)

class TestMonsterGetActions(APITestCase):

    fixtures = ['pydnd/fixtures/db_fixture.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MonsterActionsList.as_view()
        self.uri = 'monsters/{}/actions'

    def test_get_by_name(self):
        request = self.factory.get(self.uri.format('1'))
        response = self.view(request, '1')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue(response.data)

    # def test_get_by_name(self):
    #     request = self.factory.get(self.uri)
    #     response = self.view(request, '2')
    #     self.assertEqual(response.status_code, 200,
    #                      'Expected Response Code 200, received {0} instead.'
    #                      .format(response.status_code))
    #
    # def test_non_monster_name(self):
    #     request = self.factory.get(self.uri)
    #     response = self.view(request, 'NOT_MONSTER')
    #     self.assertEqual(response.status_code, 204,
    #                      'Expected Response Code 204, received {0} instead.'
    #                      .format(response.status_code))
    #
    # def test_non_monster_id(self):
    #     request = self.factory.get(self.uri)
    #     response = self.view(request, '99999')
    #     self.assertEqual(response.status_code, 204,
    #                      'Expected Response Code 204, received {0} instead.'
    #                      .format(response.status_code))