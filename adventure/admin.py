from django.contrib import admin



# Register your models here.
from .models import *
admin.site.register(Room)
admin.site.register(Player)


# curl -X POST -H 'Authorization: Token 4d35e16842ccd0d179dce147cfd04657cec9342a' -H "Content-Type: application/json" -d '{"direction":"n"}' localhost:8000/api/adv/move/
# curl -X POST -H "Content-Type: application/json" -d '{"username":"team_chaotic", "password":"chaospass"}' localhost:8000/api/login/


# room_type = {
#     'cave': 'rough natural walls form this room',
#     'hall': 'hall_deco',
# }

# cave_deco = {
#     'damp': 'moisture fills the air and mold grows on the walls',
#     'hot'
# }

# hall_deco = {

# }

# room_items = {
#     'none': 50,
#     'box': 53,
# }