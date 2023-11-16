from django.test import TestCase
import json

class UserViewTest(TestCase):
    def test_get_user_response(self):
        """Get status code 200"""
        response = self.client.get('http://127.0.0.1:8080/user/test1@gmail.com/')
        self.assertEqual(response.status_code, 200)


    def test_create_user(self):
        """Get status code 200"""
        data = {
            'email': 'test1@gmail.com',
            'firstName': 'testfirstname',
            'lastName': 'testlastname'
        }
        dataJSON = json.dumps(data)
        response = self.client.post('http://127.0.0.1:8080/user/', dataJSON)
        self.assertEqual(response.status_code, 200)

class AccountViewTest(TestCase):
    pass

class RecordViewTest(TestCase):
    pass