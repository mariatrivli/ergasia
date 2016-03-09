import math
import random
from PILL import Image, ImageDraw
for i in range(1,1025):
    pass
    for j in range(1,1025):
        pass
        epipedo[i][j]
for i in range(1,21):
    pass
    im = Image.new("RGB", (512, 512), "white")
    x=random.choice(1,1025)
    y=random.choice(1,1025)
    r=random.choice(10,51)
    draw = ImageDraw.Draw(im)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,0), outline ='red')
    for j in range(1,4):#apothikeuw ta stoixeia tou kathe kuklou(kentro kai aktina)
        pass
        if j==1:
            pass
            kukloi[i][1]=x
        if j==2:
            pass
            kukloi[i][2]=y
        if j==3:
            pass
            kukloi[i][3]=r
for i in range(1,21):
    pass
    for k in range(i,20):#sugkrinw kathe kuklo me tous upoloipous xwris na epanalambanontai oi idioi elegxoi
        pass
        a=math.pow(kukloi[k+1][2]-kukloi[i][2], 2)
        b=math.pow(kukloi[k+1][1]-kukloi[i][1], 2)
        d=math.sqrt(a+b)
        if math.fabs(kukloi[i][3]-kykloi[k+1][3])<d and d<kukloi[i][3]+kykloi[k+1][3]:
            pass
            temkuk=0#oi temonomenoi kukloi
            temkuk=temkuk+1
print "temnontai",temkuk, "kukloi"# emfanizei tous temonomenous kuklous
im.show()#kai tin eikona
