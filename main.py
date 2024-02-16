from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    l1 = Line(Point(50, 50), Point(400, 400))
    l2 = Line(Point(400, 10), Point(10, 200))
    win.draw_line(l1, "black")
    win.draw_line(l2, "green")
    win.wait_for_close()

main()