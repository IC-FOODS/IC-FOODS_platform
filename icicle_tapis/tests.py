from django.test import TestCase


class TestTapisAPI(TestCase):
    """Tests for Travelport APIs"""

    def test_tapis(self):
        """Test the basic login flow"""

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
