from django.test import TestCase
from django.urls import reverse

class TestTapisAPI(TestCase):
    """Tests for Tapis APIs"""

    def test_tapis(self):
        """Test the basic login flow"""
        return
        user_data = {
            "username": "siebo",
            "password": "XXXXX",
        }

        response = self.client.post(
            "/api/tapis/login/",
            data={
                "username": user_data["username"],
                "password": user_data["password"],
            },
        )
        import pdb; pdb.set_trace()


class TestTapisUserInfoAPI(TestCase):
    """Tests for Tapis UserInfo API"""

    def test_user_info(self):
        """Test the basic login flow"""

        response = self.client.post(
            reverse("user-info"),
        )
        print(response.content)

        response = self.client.post(
            reverse("user-info"),
        )
        print(response.content)


class TestTapisCallbackAPI(TestCase):
    """Tests for Tapis Callback API"""

    def test_callback(self):
        """Test the callback"""

        response = self.client.post(
            reverse("callback"),
        )
