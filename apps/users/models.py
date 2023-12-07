from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    total_points = models.IntegerField(default=0)
    rounds_played = models.IntegerField(default=0)
    average_points = models.FloatField(default=0)

    def get_last(self, limit=1):
        return self.slot_set.order_by('-date_created')[:limit]

    def refresh_data(self):
        rounds = self.slot_set.all()
        self.rounds_played = rounds.count()
        self.total_points = rounds.aggregate(models.Sum('points'))['points__sum']
        self.average_points = self.total_points / self.rounds_played
        self.save()
        
    
