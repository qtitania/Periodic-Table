from django.db import models
import pandas as pd
class Dict(models.Model):
  #l=[['H', 1, 'Hydrogen'], ['He', 2, 'Helium'], ['Li', 3, 'Lithium'], ['Be', 4, 'Beryllium'], ['B', 5, 'Boron'], ['C', 6, 'Carbon'], ['N', 7, 'Nitrogen'], ['O', 8, 'Oxygen'], ['F', 9, 'Fluorine'], ['Ne', 10, 'Neon'], ['Na', 11, 'Sodium'], ['Mg', 12, 'Magnesium'], ['Al', 13, 'Aluminum,'], ['Si', 14, 'Silicon'], ['P', 15, 'Phosphorus'], ['S', 16, 'Sulfur'], ['Cl', 17, 'Chlorine'], ['Ar', 18, 'Argon'], ['K', 19, 'Potassium'], ['Ca', 20, 'Calcium'], ['Sc', 21, 'Scandium'], ['Ti', 22, 'Titanium'], ['V', 23, 'Vanadium'], ['Cr', 24, 'Chromium'], ['Mn', 25, 'Manganese'], ['Fe', 26, 'Iron'], ['Co', 27, 'Cobalt'], ['Ni', 28, 'Nickel'], ['Cu', 29, 'Copper'], ['Zn', 30, 'Zinc'], ['Ga', 31, 'Gallium'], ['Ge', 32, 'Germanium'], ['As', 33, 'Arsenic'], ['Se', 34, 'Selenium'], ['Br', 35, 'Bromine'], ['Kr', 36, 'Krypton'], ['Rb', 37, 'Rubidium'], ['Sr', 38, 'Strontium'], ['Y', 39, 'Yttrium'], ['Zr', 40, 'Zirconium'], ['Nb', 41, 'Niobium'], ['Mo', 42, 'Molybdenum'], ['Tc', 43, 'Technetium'], ['Ru', 44, 'Ruthenium'], ['Rh', 45, 'Rhodium'], ['Pd', 46, 'Palladium'], ['Ag', 47, 'Silver'], ['Cd', 48, 'Cadmium'], ['In', 49, 'Indium'], ['Sn', 50, 'Tin'], ['Sb', 51, 'Antimony'], ['Te', 52, 'Tellurium'], ['I', 53, 'Iodine'], ['Xe', 54, 'Xenon'], ['Cs', 55, 'Cesium'], ['Ba', 56, 'Barium'], ['La', 57, 'Lanthanum'], ['Ce', 58, 'Cerium'], ['Pr', 59, 'Praseodymium'], ['Nd', 60, 'Neodymium'], ['Pm', 61, 'Promethium'], ['Sm', 62, 'Samarium'], ['Eu', 63, 'Europium'], ['Gd', 64, 'Gadolinium'], ['Tb', 65, 'Terbium'], ['Dy', 66, 'Dysprosium'], ['Ho', 67, 'Holmium'], ['Er', 68, 'Erbium'], ['Tm', 69, 'Thulium'], ['Yb', 70, 'Ytterbium'], ['Lu', 71, 'Lutetium'], ['Hf', 72, 'Hafnium'], ['Ta', 73, 'Tantalum'], ['W', 74, 'Tungsten'], ['Re', 75, 'Rhenium'], ['Os', 76, 'Osmium'], ['Ir', 77, 'Iridium'], ['Pt', 78, 'Platinum'], ['Au', 79, 'Gold'], ['Hg', 80, 'Mercury'], ['Tl', 81, 'Thallium'], ['Pb', 82, 'Lead'], ['Bi', 83, 'Bismuth'], ['Po', 84, 'Polonium'], ['At', 85, 'Astatine'], ['Rn', 86, 'Radon'], ['Fr', 87, 'Francium'], ['Ra', 88, 'Radium'], ['Ac', 89, 'Actinium'], ['Th', 90, 'Thorium'], ['Pa', 91, 'Protactinium'], ['U', 92, 'Uranium'], ['Np', 93, 'Neptunium'], ['Pu', 94, 'Plutonium'], ['Am', 95, 'Americium'], ['Cm', 96, 'Curium'], ['Bk', 97, 'Berkelium'], ['Cf', 98, 'Californium'], ['Es', 99, 'Einsteinium'], ['Fm', 100, 'Fermium'], ['Md', 101, 'Mendelevium'], ['No', 102, 'Nobelium'], ['Lr', 103, 'Lawrencium'], ['Rf', 104, 'Rutherfordium'], ['Db', 105, 'Dubnium'], ['Sg', 106, 'Seaborgium'], ['Bh', 107, 'Bohrium'], ['Hs', 108, 'Hassium'], ['Mt', 109, 'Meitnerium'], ['Ds', 110, 'Darmstadtium'], ['Rg', 111, 'Roentgenium'], ['Cn', 112, 'Copernicium'], ['Nh', 113, 'Nihonium'], ['Fl', 114, 'Flerovium'], ['Mc', 115, 'Moscovium'], ['Lv', 116, 'Livermorium'], ['Ts', 117, 'Tennessine'], ['Og', 118, 'Oganesson']]
  l=[[0 for i in range(3)]for j in range(118)]
  df = pd.read_csv('myapp/data.csv')
  ll=[]
  c=0
  for i in df:
    if c==3:
      break
    ll.append(df[i].values.tolist())
    c+=1
  
  for i in range(len(ll[1])):
    ll[1][i]=ll[1][i].strip()
    ll[2][i]=ll[2][i].strip()
  for i in range(len(ll[1])):
    l[i][0]=ll[1][i]
    l[i][1]=ll[0][i]
    l[i][2]=ll[2][i]

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
  c=1
  for i in range(9):
    for j in range(18):
      if dict[(i,j)]=="":
        dict[(i,j)]=["",0,""]
      
        


