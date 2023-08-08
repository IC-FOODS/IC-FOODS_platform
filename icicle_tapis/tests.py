from django.test import TestCase
from django.urls import reverse


# These tests are meant to be run manually.
# Populate the following vars with an unused code
# or valid JWT token to run the respective tests.
TEST_CODE = ""
TEST_TOKEN = ""


class TestTapisCallbackAPI(TestCase):
    """Tests for Tapis Callback API"""

    def test_callback(self):
        """Test the callback"""

        if len(TEST_CODE) == 0:
            return

        response = self.client.get(
            f"/api/tapis/callback/?code={TEST_CODE}&state=None",
        )

        self.assertEqual(response.status_code, 200)


class TestProtectedAPI(TestCase):
    """Tests for Tapis Callback API"""

    def test_auth(self):
        """Test the callback"""

        if len(TEST_TOKEN) == 0:
            return

        response = self.client.get(
            reverse("protected"),
            **{"HTTP_AUTHORIZATION": f"Token {TEST_TOKEN}"}
        )
        self.assertEqual(response.status_code, 200)
