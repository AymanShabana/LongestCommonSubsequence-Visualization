import tkinter.messagebox as ms
from tkinter import *
import pygame
import ctypes

sysWidth=ctypes.windll.user32.GetSystemMetrics(0)
sysHeight=ctypes.windll.user32.GetSystemMetrics(1)
cellDim=0
str1=""
str2=""
def getLCS(b,m,n):
    Res=""
    done=False
    currentI=m-1
    currentJ=n-1
    while not done:
        if b[currentI+1][currentJ+1]==1:
            Res=str1[currentI]+Res
            currentI-=1
            currentJ-=1
        elif b[currentI+1][currentJ+1]==2:
            currentI-=1
        elif b[currentI+1][currentJ+1]==3:
            currentJ-=1
        elif b[currentI+1][currentJ+1]==4:
            currentJ-=1
        else:
            done=True
    return Res



def btnClicked():
    global str1
    global str2
    gameExit = False
    str1=string1.get()
    str2=string2.get()
    if len(str1)>len(str2):
        cellDim=int(sysHeight/(len(str1)+2))
    else:
        cellDim=int(sysHeight/(len(str2)+2))
    pygame.init()
    gameDisplay = pygame.display.set_mode((sysWidth, sysHeight),pygame.FULLSCREEN)
    pygame.display.set_caption("LCS Grid")
    cimg=pygame.transform.scale(pygame.image.load("img/box1.png"),(cellDim,cellDim))
    arrow1=pygame.transform.scale(pygame.image.load("img/diagonal.png"),(cellDim,cellDim))
    arrow2=pygame.transform.scale(pygame.image.load("img/left.png"),(cellDim,cellDim))
    arrow3=pygame.transform.scale(pygame.image.load("img/up.png"),(cellDim,cellDim))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    cells=[]

    #LCS-LENGTH
    m=len(str1)
    n=len(str2)
    b=[]
    c=[]
    for i in range(m+1):
        c.append([])
        b.append([])
        for j in range(n+1):
            c[i].append(0)
            b[i].append(0)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]=1
            elif c[i-1][j]>c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]=2
            elif c[i-1][j]<c[i][j-1]:
                c[i][j]=c[i][j-1]
                b[i][j]=3
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 4
    #LCS-LENGTH END
    res=getLCS(b,m,n)
    for i in range((len(str1)+2)):
        for j in range((len(str2)+2)):
            if i<2 or j<2:
                cells.append(cell(i,j))
            else:
                cells.append(cell(i,j,c[i-1][j-1],b[i-1][j-1]))


    clock = pygame.time.Clock()
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                gameExit = True
        gameDisplay.fill((255,255,255))
        for c in cells:
            gameDisplay.blit(cimg,((c.x*cellDim),(c.y*cellDim)))
            if not c.letter:
                text = myfont.render(str(c.val), True, (0, 0, 0), None)
            else:
                text = myfont.render(c.ltr, True, (0, 0, 0), None)
            gameDisplay.blit(text,((c.x*cellDim)+(cellDim/2),(c.y*cellDim)))
            if c.arrow==1:
                gameDisplay.blit(arrow1,((c.x*cellDim)-(cellDim/2),(c.y*cellDim)-(cellDim/2)))
            elif c.arrow==2:
                gameDisplay.blit(arrow2,((c.x*cellDim)-(cellDim/2),(c.y*cellDim)))
            elif c.arrow==3:
                gameDisplay.blit(arrow3,((c.x*cellDim)-(cellDim/4),(c.y*cellDim)-(cellDim/2)))
            elif c.arrow==4:
                gameDisplay.blit(arrow2,((c.x*cellDim)-(cellDim/2),(c.y*cellDim)))
                gameDisplay.blit(arrow3, ((c.x * cellDim)-(cellDim/4), (c.y * cellDim)-(cellDim/2)))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    ms.showinfo(title="Longest Common Subsequence", message=res)
class cell():
    def __init__(self,x,y,val=0,arrow=0):
        if (x==0 and y==0)or(x==0 and y==1)or(x==1 and y==0):
            self.letter=True
            self.ltr=""
        elif x==0:
            self.letter=True
            self.ltr=str2[y-2]
        elif y==0:
            self.letter=True
            self.ltr = str1[x - 2]
        else:
            self.letter=False

        self.val=val
        self.arrow=arrow
        self.x=x
        self.y=y

inputWindow=Tk()
inputWindow.title("Longest Common Subsequence")
lbl=Label(inputWindow, text="Enter 2 strings:")
lbl.grid(column=0, row=0)
string1 = Entry(inputWindow,width=200)
string1.grid(column=0, row=1)
string2 = Entry(inputWindow,width=200)
string2.grid(column=0, row=2)
btn = Button(inputWindow, text="Run", command=btnClicked)
btn.grid(column=0, row=3)
inputWindow.mainloop()
