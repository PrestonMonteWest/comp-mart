from django.db import models
from django.conf import settings
from fernet_fields import EncryptedTextField

class AddressBase(models.Model):
    class Meta:
        abstract = True

    STATES = (
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AR', 'Arkansas'),
        ('AS', 'American Samoa'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'District of Columbia'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('GU', 'Guam'),
        ('HI', 'Hawaii'),
        ('IA', 'Iowa'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MO', 'Missouri'),
        ('MP', 'Northern Mariana Islands'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NA', 'National'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NE', 'Nebraska'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VA', 'Virginia'),
        ('VI', 'Virgin Islands'),
        ('VT', 'Vermont'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming'),
    )

    street = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, choices=STATES)
    zip_code = models.CharField('ZIP code', max_length=5)

class Address(AddressBase):
    class Meta:
        ordering = ('street', 'city', 'state')
        unique_together = (('user', 'street', 'city', 'state'),)
        verbose_name_plural = 'Addresses'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name='addresses'
    )

    def __str__(self):
        return '{}, {}, {} {}'.format(
            self.street,
            self.city,
            self.state,
            self.zip_code
        )

class CreditCard(models.Model):
    class Meta:
        unique_together = (('user', 'card_number'),)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name='cards'
    )
    card_number = EncryptedTextField()
    card_type = models.CharField(max_length=20)
    holder_name = models.CharField(max_length=50)
    expiration_date = models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.card_type, self.holder_name)
