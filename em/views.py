from facepy import GraphAPI

from django.shortcuts import render

graph = GraphAPI('CAACEdEose0cBALU6a5GxPFtRBsu3gk1LASHbS1dviL4a16RcfmVuTR1fVuf9eMrscODDSaZABTwZAF4ilIPGxFRc8RrwVZBX6TtZA1sdFmPBMRDFFONDnFNZAUZB1lZBwb8FRzLhlpBV0t8iYcx198RzcKTswZAjjErGBhZChQzw8sd4lv4MGGjz1cEjo2i2LcsPOUxpDwkHdEU0wdWpbHzZBo')


def home(request):
    photo = graph.get('me/photos')
    pic_one = photo['data'][0]['source']
    pic_one_title = photo['data'][0]['from']['name']
    pic_two = photo['data'][1]['source']
    pic_two_title = photo['data'][1]['from']['name']
    pic_three = photo['data'][2]['source']
    pic_three_title = photo['data'][2]['from']['name']
    pic_four = photo['data'][3]['source']
    pic_four_title = photo['data'][3]['from']['name']
    context = {'pic_one': pic_one, 'pic_one_title': pic_one_title,
               'pic_two': pic_two, 'pic_two_title': pic_two_title,
               'pic_three': pic_three, 'pic_three_title': pic_three_title,
               'pic_four': pic_four, 'pic_four_title': pic_four_title,}
    templates = 'home.html'
    return render(request, templates, context)
