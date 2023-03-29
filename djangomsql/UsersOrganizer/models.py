from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=75)
    discord_id = models.CharField(max_length=75)
    riot_id = models.CharField(max_length=75)
    battle_net_id = models.CharField(max_length=75)
    steam_id = models.CharField(max_length=75)
    epic_games_id = models.CharField(max_length=75)

    def __str__(self):
        return(f"{self.username}")