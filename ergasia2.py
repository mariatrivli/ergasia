import random

def paixnidi(a,triliza):#sunartisi gia tin topothetisi pioniou
    pass
    print a
    x=input("poio pioni thes;")
    tetagmeni=input("se poiα tetmimeni thes to pioni sou;")
    tetmimeni=input("se poia tetagmeni thes to pioni sou;")
    while triliza[tetagmeni][tetmimeni]==3 and x==3:
        pass
        print "epelekse allo pioni!"
        x=input("poio thes;")
    triliza[tetagmeni][tetmimeni]=x
    a.remove (x)

for i in range(1,4):
   pass
   for j in range(1,4):
      pass
      triliza=[i][j]
paiktis1=[1,1,2,2,3,3]
paiktis2=list(paiktis1)
#paizei prwta o paiktis1
while len(paiktis1)!=0 and len(paiktis2)!=0:#mexri na teleiwsoun ta pionia
    pass
    paixnidi(paiktis1,triliza)
    paixnidi(paiktis2,triliza)
print "eksantlithikan ta pionia"
