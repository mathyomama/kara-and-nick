from django.db import models

# Create your models here.
class PartyMember(models.Model):
        name = models.CharField(max_length=50)
        image = models.ImageField()
        RESPONSIBILITIES = (
                        ('MAID_OF_HONOR', 'Maid of Honor'),
                        ('MATRON_OF_HONOR', 'Matron of Honor'),
                        ('BEST_MAN', 'Best Man'),
                        ('BRIDESMAID', 'Bridesmaid'),
                        ('JR_BRIDESMAID', 'Jr. Bridesmaid'),
                        ('GROOMSMAN', 'Groomsman'),
                        ('JR_GROOMSMAN', 'Jr. Groomsman'),
                        ('RING_BEARER', 'Ring Bearer'),
                        ('COIN_BEARER', 'Coin Bearer'),
                        ('FLOWER_GIRL', 'Flower girl'),
                        (None, 'Responsibility'),
                        )
        responsibility = models.CharField(max_length=20, choices=RESPONSIBILITIES)
        story = models.TextField()
        relation_to_engaged = models.CharField(max_length=100)

        def __unicode__(self):
                return self.name
