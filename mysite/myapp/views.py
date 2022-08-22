from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Dict
from django.urls import reverse

def index(request): 
  l=[]
  l1=[]
  i=0
  for k,v in Dict.ans.items():
    if k[0]<7:
      if i==18:
          l.append(l1)
          l1=[]
          i=0
      l1.append((k[0],k[1],v[0],v[1]))
      i+=1
  l.append(l1)
  l2=[]
  l1=[]
  for i in range(7,9):
    for j in range(0,18):
      l1.append((i,j,Dict.ans[(i,j)][0],Dict.ans[(i,j)][1]))
    l2.append(l1)
    l1=[]
  l.sort(key= lambda x: (x[0],x[1]))
  context = {'renderdict': Dict.ans,
              'list' : l,
              'list2': l2,
              'rangei': range(4),
              'rangej': range(3)
  }
  return render(request, 'index.html', context)

def update(request, id1, id2):
  template = loader.get_template('update.html')
  
  context = {'renderdict': Dict.ans[(id1,id2)][0],
              'id1': id1,
              'id2': id2,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id, id1, id2):
  change = request.POST['updated']
  Dict.ans[(id1,id2)][0] = change
  if Dict.dict[(id1,id2)] == change:
    Dict.ans[(id1,id2)][1] = '2'
  else:
    Dict.ans[(id1,id2)][1] = '1'

  return HttpResponseRedirect(reverse('index'))
