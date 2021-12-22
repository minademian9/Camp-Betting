from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save 


# Create your models here.


class Bet(models.Model):
    bet_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    owner = models.CharField(max_length=200)
    closed = models.BooleanField(default=False)
    solution = models.CharField(max_length=200, default = None,null=True, blank=True)

    def __str__(self):
        return self.bet_text


class BetAnswer(models.Model):
    player_name = models.CharField(max_length=200)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    value= models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.choice
    
    def getdetails(self):
        return {"player_name": self.player_name,
        "player_choice": self.choice , 
        "bet_id" :self.bet.id
        , "bet_text":self.bet.bet_text 
        , 'bet_solution' : self.bet.solution,
        'bet_value': self.value,
        'bet_owner':self.bet.owner}

    def player_answer(self):
        return self.choice


class Player(models.Model):
    name = models.CharField(max_length=200)
    wallet = models.IntegerField(default=100)

    def __str__(self):
        return self.name
    
    def getWallet(self):
        return self.wallet

#     class NeoPlayer(models.Model):
#     name = models.OneToOneField(User, on_delete=models.CASCADE)
#     wallet = models.IntegerField(default=100)

#     def __str__(self):
#         return str(self.wallet)
    
#     @receiver(post_save, sender=User) 
#     def create_user_profile(sender, instance, created, **kwargs):
#       if created:
#         NeoPlayer.objects.create(name=instance)

#     @receiver(post_save, sender=User) 
#     def save_user_profile(sender, instance, **kwargs):
#       instance.neoplayer.save()

