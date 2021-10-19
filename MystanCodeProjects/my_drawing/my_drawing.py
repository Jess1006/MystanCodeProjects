"""
File: my_drawing.py
Name: Jess
----------------------
This file uses campy model to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    little prince drawing
    """
    window = GWindow(860, 580, title='Little Prince')
    background(window)
    stem(window)
    leaf(window)
    flower(window)
    cover(window)
    prince(window)
    fox(window)
    ground(window)
    famous_saying(window)


def prince(window):
    body = GArc(110, 600, 0, 180)
    body.filled = True
    body.color = 'white'
    body.fill_color = 'yellowgreen'
    window.add(body, x=608.3, y=430)

    head = GOval(80, 80)
    head.filled = True
    head.color = 'white'
    head.fill_color = 'gold'
    window.add(head, x=623, y=370)

    scarf1 = GOval(60, 20, x=632, y=435)
    scarf1.filled = True
    scarf1.color = 'gold'
    scarf1.fill_color = 'orange'
    window.add(scarf1)

    scarf2 = GPolygon()
    scarf2.add_vertex((634, 440))
    scarf2.add_vertex((640, 445))
    scarf2.add_vertex((660, 446))
    scarf2.add_vertex((690, 442))
    scarf2.add_vertex((710, 440))
    scarf2.add_vertex((725, 439))
    scarf2.add_vertex((745, 439))
    scarf2.add_vertex((755, 440))
    scarf2.add_vertex((757, 442))
    scarf2.add_vertex((760, 442))
    scarf2.add_vertex((765, 442))
    scarf2.add_vertex((775, 441.5))
    scarf2.add_vertex((780, 441.5))
    scarf2.add_vertex((782.5, 443))
    scarf2.add_vertex((785, 443.5))
    scarf2.add_vertex((786, 444))
    scarf2.add_vertex((787, 445))
    scarf2.add_vertex((788, 446))
    scarf2.add_vertex((789, 447))
    scarf2.add_vertex((789.5, 448.5))
    scarf2.add_vertex((790, 450))
    scarf2.add_vertex((791.5, 451.5))
    scarf2.add_vertex((793, 453))
    scarf2.add_vertex((795, 454))
    scarf2.add_vertex((797, 454))
    scarf2.add_vertex((799, 455))
    scarf2.add_vertex((801, 455))
    scarf2.add_vertex((801, 456.6))
    scarf2.add_vertex((802, 458))
    scarf2.add_vertex((803, 460))
    scarf2.add_vertex((804, 461.5))
    scarf2.add_vertex((805, 463))
    scarf2.add_vertex((806, 465))
    scarf2.add_vertex((807, 466))
    scarf2.add_vertex((809, 467))
    scarf2.add_vertex((810, 467.7))
    scarf2.add_vertex((811.5, 469))  # far
    scarf2.add_vertex((773, 472))
    scarf2.add_vertex((795, 491))
    scarf2.add_vertex((688, 466))
    scarf2.add_vertex((628, 466))
    scarf2.filled = True
    scarf2.color = 'white'
    scarf2.fill_color = 'darkorange'
    window.add(scarf2)

    hair1 = GPolygon()
    hair1.add_vertex((630, 390))
    hair1.add_vertex((672, 364))
    hair1.add_vertex((670, 389))
    hair1.add_vertex((645, 377))
    hair1.add_vertex((683, 367))
    hair1.add_vertex((675, 389))
    hair1.add_vertex((677, 379))
    hair1.add_vertex((705, 381))
    hair1.add_vertex((700, 410))
    hair1.filled = True
    hair1.color = 'gold'
    hair1.fill_color = 'gold'
    window.add(hair1)


def fox(window):
    l_ear = GPolygon()
    l_ear.add_vertex((520, 410))  # vertex 1
    l_ear.add_vertex((510, 433))
    l_ear.add_vertex((530, 433))
    l_ear.filled = True
    l_ear.color = 'white'
    l_ear.fill_color = 'orangered'
    window.add(l_ear)

    r_ear = GPolygon()
    r_ear.add_vertex((552, 410))  # vertex 1
    r_ear.add_vertex((542, 433))
    r_ear.add_vertex((562, 433))
    r_ear.filled = True
    r_ear.color = 'white'
    r_ear.fill_color = 'orangered'
    window.add(r_ear)

    body = GArc(90, 400, 0, 180)
    body.filled = True
    body.color = 'white'
    body.fill_color = 'orangered'
    window.add(body, x=491, y=460)

    head = GPolygon()
    head.add_vertex((510, 433))
    head.add_vertex((562, 433))
    head.add_vertex((572, 450))
    head.add_vertex((562, 470))
    head.add_vertex((510, 470))
    head.add_vertex((500, 450))
    head.filled = True
    head.color = 'white'
    head.fill_color = 'orangered'
    window.add(head)

    tail = GArc(95, 80, 0, 180, x=536, y=537)
    tail.filled = True
    tail.color = 'white'
    tail.fill_color = 'orangered'
    window.add(tail)


def ground(window):
    mud1 = GArc(200, 150, 0, 180)
    mud1.filled = True
    mud1.color = 'sienna'
    mud1.fill_color = 'sienna'
    window.add(mud1, x=-30, y=550)

    mud2 = GArc(200, 150, 0, 180)
    mud2.filled = True
    mud2.color = 'saddlebrown'
    mud2.fill_color = 'saddlebrown'
    window.add(mud2, x=60, y=550)

    mud3 = GArc(200, 150, 0, 180)
    mud3.filled = True
    mud3.color = 'sienna'
    mud3.fill_color = 'sienna'
    window.add(mud3, x=150, y=550)

    mud4 = GArc(200, 150, 0, 180)
    mud4.filled = True
    mud4.color = 'sienna'
    mud4.fill_color = 'sienna'
    window.add(mud4, x=200, y=550)

    mud5 = GArc(200, 150, 0, 180)
    mud5.filled = True
    mud5.color = 'sienna'
    mud5.fill_color = 'sienna'
    window.add(mud5, x=270, y=550)

    mud6 = GArc(200, 150, 0, 180)
    mud6.filled = True
    mud6.color = 'saddlebrown'
    mud6.fill_color = 'saddlebrown'
    window.add(mud6, x=380, y=550)

    mud7 = GArc(200, 150, 0, 180)
    mud7.filled = True
    mud7.color = 'sienna'
    mud7.fill_color = 'sienna'
    window.add(mud7, x=450, y=550)

    mud8 = GArc(200, 150, 0, 180)
    mud8.filled = True
    mud8.color = 'saddlebrown'
    mud8.fill_color = 'saddlebrown'
    window.add(mud8, x=520, y=550)

    mud9 = GArc(200, 150, 0, 180)
    mud9.filled = True
    mud9.color = 'saddlebrown'
    mud9.fill_color = 'saddlebrown'
    window.add(mud9, x=570, y=550)

    mud10 = GArc(200, 150, 0, 180)
    mud10.filled = True
    mud10.color = 'sienna'
    mud10.fill_color = 'sienna'
    window.add(mud10, x=680, y=550)


def background(window):
    b_g = GRect(860, 580)
    b_g.filled = True
    b_g.fill_color = 'oldlace'
    b_g.color = 'oldlace'
    window.add(b_g)


def stem(window):
    stem1 = GPolygon()
    stem1.add_vertex((180, 570))
    stem1.add_vertex((190, 590))
    stem1.add_vertex((200, 490))
    stem1.add_vertex((190, 470))
    stem1.filled = True
    stem1.color = 'forestgreen'
    stem1.fill_color = 'forestgreen'
    window.add(stem1)

    stem2 = GPolygon()
    stem2.add_vertex((200, 490))
    stem2.add_vertex((190, 475))
    stem2.add_vertex((195, 400))
    stem2.add_vertex((198, 388))
    stem2.filled = True
    stem2.fill_color = 'limegreen'
    stem2.color = 'limegreen'
    window.add(stem2)

    stem3 = GPolygon()
    stem3.add_vertex((193, 570))
    stem3.add_vertex((190, 500))
    stem3.add_vertex((203, 400))
    stem3.add_vertex((208, 388))
    stem3.filled = True
    stem3.fill_color = 'olive'
    stem3.color = 'olive'
    window.add(stem3)

    stem4 = GPolygon()
    stem4.add_vertex((195, 390))
    stem4.add_vertex((200, 430))
    stem4.add_vertex((210, 300))
    stem4.add_vertex((200, 288))
    stem4.filled = True
    stem4.fill_color = 'olivedrab'
    stem4.color = 'olivedrab'
    window.add(stem4)

    stem5 = GPolygon()
    stem5.add_vertex((203, 180))
    stem5.add_vertex((207, 160))
    stem5.add_vertex((210, 310))
    stem5.add_vertex((202, 298))
    stem5.filled = True
    stem5.fill_color = 'seagreen'
    stem5.color = 'seagreen'
    window.add(stem5)

    stem6 = GPolygon()
    stem6.add_vertex((158, 250))
    stem6.add_vertex((160, 245))
    stem6.add_vertex((210, 318))
    stem6.add_vertex((200, 308))
    stem6.filled = True
    stem6.fill_color = 'darkkhaki'
    stem6.color = 'darkkhaki'
    window.add(stem6)

    stem7 = GPolygon()
    stem7.add_vertex((202, 250))
    stem7.add_vertex((208, 245))
    stem7.add_vertex((240, 200))
    stem7.add_vertex((230, 220))
    stem7.filled = True
    stem7.fill_color = 'olivedrab'
    stem7.color = 'olivedrab'
    window.add(stem7)

    stem8 = GPolygon()
    stem8.add_vertex((208, 185))
    stem8.add_vertex((135, 173))
    stem8.add_vertex((150, 160))
    stem8.add_vertex((180, 166))
    stem8.add_vertex((195, 160))
    stem8.add_vertex((200, 165))
    stem8.add_vertex((245, 160))
    stem8.filled = True
    stem8.fill_color = 'darkolivegreen'
    stem8.color = 'darkolivegreen'
    window.add(stem8)

    stem9 = GPolygon()
    stem9.add_vertex((199, 340))
    stem9.add_vertex((196, 200))
    stem9.add_vertex((208, 250))
    stem9.add_vertex((209, 310))
    stem9.add_vertex((208, 320))
    stem9.filled = True
    stem9.fill_color = 'sage'
    stem9.color = 'sage'
    window.add(stem9)

    stem10 = GPolygon()
    stem10.add_vertex((207, 330))
    stem10.add_vertex((200, 280))
    stem10.add_vertex((197, 250))
    stem10.add_vertex((209, 310))
    stem10.add_vertex((208, 320))
    stem10.filled = True
    stem10.fill_color = 'olive'
    stem10.color = 'olive'
    window.add(stem10)


def leaf(window):
    leaf1 = GArc(100, 70, 180, 120)
    leaf1.filled = True
    leaf1.fill_color = 'forestgreen'
    leaf1.color = 'forestgreen'
    window.add(leaf1, x=130, y=250)
    leaf2 = GArc(120, 70, 295, 140)
    leaf2.filled = True
    leaf2.fill_color = 'forestgreen'
    leaf2.color = 'forestgreen'
    window.add(leaf2, x=115, y=190)
    leaf3 = GArc(180, 90, 160, 140)
    leaf3.filled = True
    leaf3.fill_color = 'olive'
    leaf3.color = 'olive'
    window.add(leaf3, x=65, y=200)
    leaf4 = GArc(180, 90, 250, 160)
    leaf4.filled = True
    leaf4.fill_color = 'olivedrab'
    leaf4.color = 'olivedrab'
    window.add(leaf4, x=200, y=125)


def flower(window):
    petal0 = GPolygon()
    petal0.add_vertex((205, 185))  # vertex
    petal0.add_vertex((50, 115))
    petal0.add_vertex((80, 70))
    petal0.add_vertex((110, 65))
    petal0.add_vertex((150, 35))
    petal0.add_vertex((190, 40))
    petal0.add_vertex((230, 30))
    petal0.add_vertex((270, 60))
    petal0.add_vertex((310, 55))
    petal0.add_vertex((340, 80))
    petal0.filled = True
    petal0.fill_color = 'firebrick'
    petal0.color = 'firebrick'
    window.add(petal0)

    petal1 = GPolygon()
    petal1.add_vertex((205, 185))
    petal1.add_vertex((50, 90))
    petal1.add_vertex((100, 85))
    petal1.add_vertex((110, 66))
    petal1.filled = True
    petal1.fill_color = 'maroon'
    petal1.color = 'maroon'
    window.add(petal1)

    petal2 = GPolygon()
    petal2.add_vertex((205, 185))
    petal2.add_vertex((290, 50))
    petal2.add_vertex((330, 60))
    petal2.filled = True
    petal2.fill_color = 'darkred'
    petal2.color = 'darkred'
    window.add(petal2)

    petal3 = GPolygon()
    petal3.add_vertex((205, 185))
    petal3.add_vertex((105, 100))
    petal3.add_vertex((150, 60))
    petal3.filled = True
    petal3.fill_color = 'indianred'
    petal3.color = 'indianred'
    window.add(petal3)

    petal4 = GPolygon()
    petal4.add_vertex((205, 185))
    petal4.add_vertex((140, 90))
    petal4.add_vertex((160, 50))
    petal4.add_vertex((190, 65))
    petal4.filled = True
    petal4.fill_color = 'ivory'
    petal4.color = 'ivory'
    window.add(petal4)

    petal5 = GPolygon()
    petal5.add_vertex((205, 185))
    petal5.add_vertex((170, 90))
    petal5.add_vertex((180, 30))
    petal5.add_vertex((230, 45))
    petal5.filled = True
    petal5.fill_color = 'brown'
    petal5.color = 'brown'
    window.add(petal5)

    petal6 = GPolygon()
    petal6.add_vertex((205, 185))
    petal6.add_vertex((205, 90))
    petal6.add_vertex((210, 50))
    petal6.add_vertex((230, 35))
    petal6.filled = True
    petal6.fill_color = 'burlywood'
    petal6.color = 'burlywood'
    window.add(petal6)

    petal7 = GPolygon()
    petal7.add_vertex((205, 185))
    petal7.add_vertex((218, 70))
    petal7.add_vertex((250, 35))
    petal7.filled = True
    petal7.fill_color = 'sienna'
    petal7.color = 'sienna'
    window.add(petal7)

    petal8 = GPolygon()
    petal8.add_vertex((205, 185))
    petal8.add_vertex((230, 80))
    petal8.add_vertex((245, 60))
    petal8.add_vertex((270, 50))
    petal8.filled = True
    petal8.fill_color = 'maroon'
    petal8.color = 'maroon'
    window.add(petal8)

    petal9 = GPolygon()
    petal9.add_vertex((205, 185))
    petal9.add_vertex((270, 50))
    petal9.add_vertex((273, 60))
    petal9.add_vertex((278, 90))
    petal9.filled = True
    petal9.fill_color = 'floralwhite'
    petal9.color = 'floralwhite'
    window.add(petal9)

    petal10 = GPolygon()
    petal10.add_vertex((205, 185))
    petal10.add_vertex((95, 50))
    petal10.add_vertex((135, 60))
    petal10.add_vertex((160, 90))
    petal10.filled = True
    petal10.fill_color = 'tan'
    petal10.color = 'tan'
    window.add(petal10)

    petal11 = GPolygon()
    petal11.add_vertex((205, 185))
    petal11.add_vertex((188, 70))
    petal11.add_vertex((195, 40))
    petal11.add_vertex((210, 60))
    petal11.filled = True
    petal11.fill_color = 'saddlebrown'
    petal11.color = 'saddlebrown'
    window.add(petal11)

    petal12 = GPolygon()
    petal12.add_vertex((205, 185))  # vertex
    petal12.add_vertex((50, 115))
    petal12.add_vertex((80, 150))
    petal12.add_vertex((110, 145))
    petal12.add_vertex((150, 115))
    petal12.add_vertex((190, 120))
    petal12.add_vertex((230, 110))
    petal12.add_vertex((270, 140))
    petal12.add_vertex((310, 135))
    petal12.add_vertex((340, 80))
    petal12.filled = True
    petal12.fill_color = 'firebrick'
    petal12.color = 'firebrick'
    window.add(petal12)

    petal13 = GPolygon()
    petal13.add_vertex((205, 185))  # vertex
    petal13.add_vertex((50, 115))
    petal13.add_vertex((80, 150))
    petal13.add_vertex((110, 166))
    petal13.add_vertex((150, 175))
    petal13.add_vertex((190, 135))
    petal13.add_vertex((230, 166))
    petal13.add_vertex((270, 150))
    petal13.add_vertex((310, 135))
    petal13.add_vertex((340, 80))
    petal13.filled = True
    petal13.fill_color = 'maroon'
    petal13.color = 'maroon'
    window.add(petal13)


def cover(window):
    covering_1 = GLine(35, 570, 35, 120)
    covering_1.color = 'dimgrey'
    window.add(covering_1)

    covering_2 = GLine(365, 570, 365, 120)
    covering_2.color = 'dimgrey'
    window.add(covering_2)

    covering_3 = GArc(330, 450, 0, 180)
    covering_3.color = 'dimgrey'
    window.add(covering_3, x=35, y=11)


def famous_saying(window):
    sentence1 = GLabel('It is the time that you have')
    sentence1.font = 'Times-20-bold-italic'
    sentence1.color = 'dimgrey'
    window.add(sentence1, x=440, y=200)

    sentence2 = GLabel('wasted for your rose that')
    sentence2.font = 'Times-20-bold-italic'
    sentence2.color = 'dimgrey'
    window.add(sentence2, x=440, y=230)

    sentence3 = GLabel('makes your rose so important.')
    sentence3.font = 'Times-20-bold-italic'
    sentence3.color = 'dimgrey'
    window.add(sentence3, x=440, y=260)

    sentence4 = GLabel('-Little Prince')
    sentence4.font = 'Times-20-bold-italic'
    sentence4.color = 'dimgray'
    window.add(sentence4, x=625, y=310)


if __name__ == '__main__':
    main()
