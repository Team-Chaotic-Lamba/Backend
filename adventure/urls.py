from django.conf.urls import url
from . import api
# from adventure.map_generator import *

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('rooms', api.all_rooms),
    url('generate', api.make_map)
]
# generate = Generator()
# generate.create_map()