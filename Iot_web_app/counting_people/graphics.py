from models import Room, DataFromRoom
import matplotlib.pyplot as plt
import pandas as pd

def get_data_from_a_room(code_id): # retourne les 24 derniers objets queryset ordonnés par leur date de publication
    data_room = DataFromRoom.objects.filter(code_id=code_id).order_by('date_published')[:24]
    number_of_people = []
    date_of_the_measurement = []
    for data in data_room:
        number_of_people.append(data.people_in_room)
        date_of_the_measurement.append(data.date_published.hour)
    df = pd.DataFrame({'number_of_people': number_of_people, 'Date': date_of_the_measurement})
    return df

"""
Notes:
iteration of a dataframe with pandas
for x in df.itertuples():
    print(x.column_name)
"""
