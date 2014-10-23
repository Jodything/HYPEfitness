import os
from facepy import GraphAPI

from django.shortcuts import render

FB_AUTH = os.environ.get('FB_AUTH')
graph = GraphAPI(FB_AUTH)
# url = 'https://graph.facebook.com/oauth/access_token?client_id=1714402388785165&client_secret=cbcd3b94455a534eacb85750afcd4e83&grant_type=fb_exchange_token&fb_exchange_token=CAAYXPWliuA0BABBBnZBSxScEBwcezHFIRpcm5xRc5Rj4QNhzIVedzrfXP0hrFz8kztZBd88OHJ2FFocmgHP0XzCjQM3lLq2r7FDxXOSo3Cnfj1lJmXDK78vtaYdNpb8CPGhgzy1KHpjiRdDAiBfHZBfUBUv7mNjNCdpASz5RcujkLrcdb6PcQaV1tFJYEgZD'


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
    pic_five = photo['data'][4]['source']
    pic_five_title = photo['data'][4]['from']['name']
    pic_six = photo['data'][5]['source']
    pic_six_title = photo['data'][5]['from']['name']
    pic_seven = photo['data'][6]['source']
    pic_seven_title = photo['data'][6]['from']['name']
    pic_eight = photo['data'][7]['source']
    pic_eight_title = photo['data'][7]['from']['name']
    context = {'pic_one': pic_one, 'pic_one_title': pic_one_title,
               'pic_two': pic_two, 'pic_two_title': pic_two_title,
               'pic_three': pic_three, 'pic_three_title': pic_three_title,
               'pic_four': pic_four, 'pic_four_title': pic_four_title,
               'pic_five': pic_five, 'pic_five_title': pic_five_title,
               'pic_six': pic_six, 'pic_six_title': pic_six_title,
               'pic_seven': pic_seven, 'pic_seven_title': pic_seven_title,
               'pic_eight': pic_eight, 'pic_eight_title': pic_eight_title, }
    templates = 'home.html'
    return render(request, templates, context)
