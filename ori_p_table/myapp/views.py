from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Dict
from django.urls import reverse

def index(request): 
  l=[]
  l1=[]
  i=0
  for k,v in Dict.dict.items():
    if k[0]<7:
      if i==18:
          l.append(l1)
          l1=[]
          i=0
      l1.append((k[0],k[1],v[0],v[1],v[2]))
      i+=1
  l.append(l1)
  l2=[]
  l1=[]
  for i in range(7,9):
    for j in range(0,18):
      l1.append((i,j,Dict.dict[(i,j)][0],Dict.dict[(i,j)][1],Dict.dict[(i,j)][2]))
    l2.append(l1)
    l1=[]
  l.sort(key= lambda x: (x[0],x[1]))
  context = {'list' : l,
             'list2': l2,
  }
  return render(request, 'index.html', context)


