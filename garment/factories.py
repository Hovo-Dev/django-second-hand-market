import factory
from garment.models import Garment
from accounts.factories import PublisherFactory

class GarmentFactory(factory.django.DjangoModelFactory):
    publisher = factory.SubFactory(PublisherFactory)
    description = factory.Faker('paragraph', nb_sentences=3)
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    size = factory.Iterator([choice[0] for choice in Garment.SIZE_CHOICES])
    type = factory.Iterator([choice[0] for choice in Garment.TYPE_CHOICES])

    class Meta:
        model = Garment
