import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


##Fake pop script
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()

topics = ['Search','Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        fake_topic = add_topic()

        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the webpage entry
        webpg = Webpage.objects.get_or_create(topic=fake_topic, url=fake_url, name=fake_name)[0]

        #create a fake access AccessRecord
        acc_record = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script... Please wait")
    populate(20)
    print("Populating complete!")
