from django.db import models
import random


class Slot(models.Model):
    created_by = models.ForeignKey("users.Profile", on_delete=models.CASCADE,blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slot_one = models.IntegerField(blank=True)
    slot_two = models.IntegerField(blank=True)
    slot_three = models.IntegerField(blank=True)
    points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.date_created:
            self.date_created = models.DateTimeField(auto_now_add=True)
            self.slot_one = random.randint(1, 9)
            self.slot_two = random.randint(1, 9)
            self.slot_three = random.randint(1, 9)
            self.get_points()
        super(Slot, self).save(*args, **kwargs)

    def get_slots(self):
        return [self.slot_one, self.slot_two, self.slot_three]

    def get_points(self):
        self.points = 0
        memo = {}
        for slot in self.get_slots():
            if slot in memo:
                memo[slot] += 1
            else:
                memo[slot] = 1
        
        for _, value in memo.items():
            if value == 3:
                self.points = 10
                break

            elif value == 2:
                self.points = 1
                break
        self.save()
        return self.points



    