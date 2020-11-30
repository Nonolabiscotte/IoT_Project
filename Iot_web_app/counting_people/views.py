# general import
from django.shortcuts import render, HttpResponse
from .models import Room
from .models import DataFromRoom
from django.template import loader

#graphics import
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import pandas as pd
# Create your views here.

def get_data_from_a_room(code_id): # retourne les 24 derniers objets queryset ordonnés par leur date de publication
    data_room = DataFromRoom.objects.filter(code_id=code_id).order_by('date_published')[:24]
    number_of_people = []
    date_of_the_measurement = []
    for data in data_room:
        number_of_people.append(data.people_in_room)
        date_of_the_measurement.append(data.date_published.hour)
    df = pd.DataFrame({'number_of_people': number_of_people, 'Date': date_of_the_measurement})
    return df

def iterate_selected_dateframe(df):
    return selected_columns

def index(request):
    created_room = Room.objects.all().order_by('code')
    template = loader.get_template('counting_people/index.html')
    context = {
        'created_room':created_room,
    }
    return HttpResponse(template.render(context, request))

def room_list(request, code_id):
    code_id = Room.objects.get(code = code_id).id # renvoie la pk du tableau Room de la room numéro code_id
    data_room = DataFromRoom.objects.filter(code_id=code_id) # séléctionne toutes les lignes ayant le pk = à code_id
    df = get_data_from_a_room(code_id)
    room = Room.objects.get(id = code_id) # requête pour afficher les infos de la room sélectionnée
    template = loader.get_template('counting_people/room_data.html') #template
    context = {
        'data_room':data_room,
        'room':room,
        'df':df
    } # dico pour transferer les data
    return HttpResponse(template.render(context, request))

def graphic_generator(request):
    f = plt.figure()
    x = np.arange(10)
    h = [0,1,2,3,4,5,6,4,2,1]
    plt.title('Test')
    plt.xlim(0,10)
    plt.ylim(0,8)
    plt.xlabel('x label')
    plt.ylabel('y label')
    bar1 = plt.bar(x,h,width=1.0,bottom=0,color='Blue',alpha=0.65,label='legend')
    plt.legend()

    canevas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image/png')
    canevas.print_png(response)
    plt.close(f)
    return response
