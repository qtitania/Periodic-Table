from django.db import models
import pandas as pd
class Dict(models.Model):
  #l=['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

  df = pd.read_csv('myapp/data.csv')
  c=0
  ll=[]
  for i in df:
    if c==3:
      break
    ll.append(df[i].values.tolist())
    c+=1
  
  for i in range(len(ll[1])):
    ll[1][i]=ll[1][i].strip()
  l=ll[1]
    
  dict = {}
  dict[(0,0)]=l[0]
  for i in range(1,17):
    dict[(0,i)]=""
  dict[(0,17)]=l[1]
  j=2
  for i in range(0,18):
    if i<12 and i>1:
      dict[(1,i)]=""
    else:
      dict[(1,i)]=l[j]
      j+=1
  for i in range(0,18):
    if i<12 and i>1:
      dict[(2,i)]=""
    else:
      dict[(2,i)]=l[j]
      j+=1
  for k in range(3,5):
    for i in range(0,18):
        dict[(k,i)]=l[j]
        j+=1
  k=5
  dict[(k,0)]=l[j]
  j+=1
  dict[(k,1)],dict[(k,2)]=l[j],""
  j=71
  for i in range(3,18):
    dict[(k,i)]=l[j]
    j+=1
  k=6
  dict[(k,0)]=l[j]
  j+=1
  dict[(k,1)],dict[(k,2)]=l[j],""
  j=103
  for i in range(3,18):
    dict[(k,i)]=l[j]
    j+=1
  k=7
  dict[(k,0)],dict[(k,1)]="",""
  j=56
  for i in range(2,17):
    dict[(k,i)]=l[j]
    j+=1
  dict[(k,17)]=""
  k=8
  dict[(k,0)],dict[(k,1)]="",""
  j=88
  for i in range(2,17):
    dict[(k,i)]=l[j]
    j+=1
  dict[(k,17)]=""

  ans = {}
  for i in range(9):
    for j in range(18):
      if dict[(i,j)]=="":
        ans[(i,j)]=["",'0']
      else:
        ans[(i,j)]=["Enter",'0']


