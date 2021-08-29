import factory
from django.utils import timezone

class FieldWorkerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'workers.FieldWorker'
        django_get_or_create = ('first_name', 'last_name')

    id = factory.Faker('uuid4')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    function = 'Other'
    created_at = timezone.now()