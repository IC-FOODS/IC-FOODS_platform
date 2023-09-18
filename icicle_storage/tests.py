import json

from django.test import TestCase
from django.urls import reverse

from icicle_storage.models import JSONObject

# These tests are meant to be run manually.
# Populate the following vars with an unused code
# or valid JWT token to run the respective tests.
TEST_CODE = ""
TEST_TOKEN = ""


class TestJSONObjectListAPI(TestCase):
    """Tests for JSONObjectListAPI"""

    def setUp(self):
        """Run this before each test"""

        JSONObject.objects.create(
            title="private",
            owner="siebo",
            json_data={"key1": "val1", "key2": "val2"},
            public=False,
        )
        JSONObject.objects.create(
            title="publico",
            owner="siebo",
            json_data={"key1": "val1", "key2": "val2"},
            public=True,
        )

    def test_object_list(self):
        """Test the object creation"""

        if len(TEST_TOKEN) == 0:
            return

        response = self.client.get(
            reverse("json-objects"),
            **{"HTTP_AUTHORIZATION": f"Token {TEST_TOKEN}"}
        )
        self.assertEqual(response.status_code, 200)
        # We should only see one result, for the public dataset
        self.assertEqual(len(response.json()), 1)

class TestJSONObjectCreateAPI(TestCase):
    """Tests for JSONObjectCreateAPI"""

    def test_object_create(self):
        """Test the object creation"""

        if len(TEST_TOKEN) == 0:
            return

        data = {
            "title": "publico",
            "json_data": {"key1": "val1", "key2": "val2"},
            "public": True,
        }

        response = self.client.post(
            reverse("json-object-create"),
            data=json.dumps(data),
            content_type="application/json",
            **{"HTTP_AUTHORIZATION": f"Token {TEST_TOKEN}"}
        )
        self.assertEqual(response.status_code, 201)


class TestJSONObjectViewAPI(TestCase):
    """Tests for JSONObjectViewAPI"""

    def setUp(self):
        """Run this before each test"""

        self.json_obj = JSONObject.objects.create(
            title="publico",
            owner="siebo",
            json_data={"key1": "val1", "key2": "val2"},
            public=True,
        )

    def test_object_view(self):
        """Test the object creation"""
        self.assertEqual(JSONObject.objects.count(), 1)

        response = self.client.get(
            reverse("json-object", kwargs={'uuid':self.json_obj.uuid}),
            **{"HTTP_AUTHORIZATION": f"Token {TEST_TOKEN}"}
        )
        self.assertEqual(
            response.json()['uuid'],
            str(self.json_obj.uuid)
        )


class TestJSONObjectDeleteAPI(TestCase):
    """Tests for JSONObjectViewAPI"""

    def setUp(self):
        """Run this before each test"""

        self.json_obj = JSONObject.objects.create(
            title="publico",
            owner="siebo",
            json_data={"key1": "val1", "key2": "val2"},
            public=True,
        )

    def test_object_delete(self):
        """Test the object creation"""

        self.assertEqual(JSONObject.objects.count(), 1)

        response = self.client.delete(
            reverse("json-object-delete", kwargs={'uuid':self.json_obj.uuid}),
            **{"HTTP_AUTHORIZATION": f"Token {TEST_TOKEN}"}
        )

        self.assertEqual(JSONObject.objects.count(), 0)
