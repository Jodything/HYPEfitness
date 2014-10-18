from facepy import GraphAPI

from django.shortcuts import render

graph = GraphAPI('CAACEdEose0cBADb75TQUmAedmGjHVSZBBl58ZCxrjDjG4eldVlLVD3M3ZAm8lsp1h1DKGJGc2ZAkZC16G5P4ZCFv6dFiibb810e5E5gKJ1dvQIVgviv9vNibGv3aGKZBbFuCefxjqh1wtHZAi2ZAtZAltIiMYv0r2dmpy4rcLMHzZBhSRU08N1wgx6iQWlJyAsfppOzZCi9fmTA4rUV92awKwDIp')

def fb_photo_one(self):
    context = {}
    templates = 'gallery.html'
    photo = graph.get('me/photos')
    pic_one = photo['data'][0]['picture']
    return render(pic_one, context, templates)

def fb_photo_two(self):
    photo = graph.get('me/photos')
    pic_two = photo['data'][1]['picture']
    return render(pic_two)
    