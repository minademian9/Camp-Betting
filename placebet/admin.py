from django.contrib import admin



# Register your models here.

from .models import Bet, Player, BetAnswer

admin.site.register(Bet)
admin.site.register(Player)
admin.site.register(BetAnswer)