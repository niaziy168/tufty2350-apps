import time

started = False
blinker = 1
screen.font = font.ignore

poy = 0
pty = 110

pohp = 120
pthp = 120
bbpo = False
bbpt = False

pobx = []
poby = []
ptbx = []
ptby = []
tpob = 0
tptb = 0
ftmr = 0

while True:
  if started == True:

    if badge.held(BUTTON_C):
      if poy < 109:
        poy += 1
    elif badge.held(BUTTON_A):
      if poy > 0:
        poy -= 1

    if badge.held(BUTTON_DOWN):
      if pty < 109:
        pty += 1
    elif badge.held(BUTTON_UP):
      if pty > 0:
        pty -= 1

    screen.pen = color.rgb(0, 76, 255)
    pone = shape.rectangle(5, poy, 11, 11)
    screen.shape(pone)
    ftmr += 1

    pohpbar = shape.line(1, 0, 1, pohp, 1)
    screen.shape(pohpbar)

    if ftmr > 30:
      poby.append(poy + 9)
      pobx.append(15)
      ptby.append(pty + 9)
      ptbx.append(143)
      tptb += 1
      tpob += 1
      ftmr = 0

    if tpob > 4:
      tpob -= 1
      del pobx[0]
      del poby[0]
      
    if tptb > 4: 
      tptb -= 1
      del ptbx[0]
      del ptby[0]

    bbpo = False

    if tpob > 0:
      if pobx[0] > 160:
        if poby[0] > pty:
          if poby[0] < pty + 10:
            bbpo = True
            tpob -= 1
            del pobx[0]
            del poby[0]
        if bbpo == False:
          tpob -= 1
          del pobx[0]
          del poby[0]
          pthp -= 2

    for i in range(tpob):
      pobx[i] = pobx[i]+2
      screen.put(pobx[i], poby[i])
      

    screen.pen = color.rgb(255, 0, 0)
    ptwo = shape.rectangle(144, pty, 11, 11)
    screen.shape(ptwo)

    pthpbar = shape.line(160, 0, 160, pthp, 1)
    screen.shape(pthpbar)

    bbpt = False

    if tptb > 0:
      if ptbx[0] < 0:
        if ptby[0] > poy:
          if ptby[0] < poy + 10:
            bbpt = True
            tptb -= 1
            del ptbx[0]
            del ptby[0]
        if bbpt == False:
          tptb -= 1
          del ptbx[0]
          del ptby[0]
          pohp -= 2

    for j in range(tptb):
      ptbx[j] = ptbx[j]-2
      screen.put(ptbx[j], ptby[j])

    if pthp < 0:
      screen.font = font.ignore
      screen.clear()
      screen.pen = color.rgb(0, 17, 255)
      screen.text("P1 WINS!", 10,10)
      screen.edgeglow()
      badge.update()
      pthp = 120
      pohp = 120
      time.sleep(2.5)
    elif pohp < 0:
      screen.clear()
      screen.font = font.ignore
      screen.pen = color.rgb(0,17,255)
      screen.text("P2 WINS!", 10,10)
      screen.edgeglow()
      badge.update()
      pthp = 120
      pohp = 120
      time.sleep(2.5)

    default_clear = color.rgb(0, 0, 0)
    badge.update()
  else:
    screen.font = font.ignore
    screen.text("BLAST WARS", 10,10)
    screen.font = font.nope
    if blinker == 1:
      screen.text("press b", 10, 50)
      blinker = 0
    else:
      blinker = 1
    screen.edgeglow()
    badge.update()
    time.sleep(0.1)

    if badge.pressed(BUTTON_B):
      started = True
