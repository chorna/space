from space.workers.models import FieldWorker
from django.urls import reverse

from nose.tools import eq_
from nose.plugins.debug import pdb
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory

from .factories import FieldWorkerFactory

# Create your tests here.

fake = Faker()


class TestFieldWorkerCreateTestCase(APITestCase):
    """
    Tests /field worker create operations.
    """

    def setUp(self):
        self.url = reverse('fieldworker-list')
        self.field_worker_data = factory.build(dict, FACTORY_CLASS=FieldWorkerFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.field_worker_data)
        eq_(response.status_code, status.HTTP_201_CREATED)


class TestFieldWorkerListTestCase(APITestCase):
    """
    Tests /field worker list operations.
    """

    def setUp(self):
        self.url = reverse('fieldworker-list')
        self.field_worker_data = factory.build(dict, FACTORY_CLASS=FieldWorkerFactory)

    def test_get_request_field_workers(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_pagination_field_workers(self):
        for x in range(15):
            FieldWorkerFactory()
        response = self.client.get(self.url+'?page=2')
        eq_(response.status_code, status.HTTP_200_OK)


class TestFieldWorkerUpdateTestCase(APITestCase):
    """
    Tests /field worker patch operations.
    """

    def setUp(self):
        self.field_worker = FieldWorkerFactory()
        self.url = reverse(
            'fieldworker-detail',
            kwargs={'pk': self.field_worker.id}
            )

    def test_update_request_field_workers(self):
        data = {
            'first_name': 'aaa',
            'last_name': 'bbb',
        }
        response = self.client.put(self.url, data)
        eq_(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_partial_request_field_workers(self):
        data = {
            'first_name': 'aaa',
        }
        response = self.client.patch(self.url, data)
        eq_(response.status_code, status.HTTP_200_OK)


class TestFieldWorkerDeleteTestCase(APITestCase):
    """
    Tests /field worker delete operations.
    """

    def setUp(self):
        self.field_worker = FieldWorkerFactory()
        self.url = reverse(
            'fieldworker-detail',
            kwargs={'pk': self.field_worker.id}
            )

    def test_delete_request_field_workers(self):
        response = self.client.delete(self.url)
        eq_(response.status_code, status.HTTP_204_NO_CONTENT)