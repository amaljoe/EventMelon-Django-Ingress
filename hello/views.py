from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from gensim.summarization import keywords

cred = credentials.Certificate("key.json")
default_app = firebase_admin.initialize_app(cred)
print(default_app.project_id)
firebase_admin.firestore.client(app=default_app)

db = firestore.client()

events_ref = db.collection(u'events')
docs = events_ref.stream()

for doc in docs:
    text = doc.to_dict()["description"]
    words = keywords(text).split(', ')
    print(f'{doc.to_dict()["name"]} => {words}')


# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')
    # return render(request, "chumma.html")



# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.all()

#     return render(request, "db.html", {"greetings": greetings})


