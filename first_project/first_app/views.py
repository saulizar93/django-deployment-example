from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, AccessRecord, Webpage
# Create your views here.
def index(request):

    webpages_list = AccessRecord.objects.all()
    date_dict = {'access_records': webpages_list}
    return render(request,'first_app/index.html', date_dict)
