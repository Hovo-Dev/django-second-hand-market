import factory
from accounts.models import Publisher

class PublisherFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    address = factory.Faker('address')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_active = True

    class Meta:
        model = Publisher
