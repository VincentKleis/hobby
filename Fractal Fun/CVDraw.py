import cv2 as cv
import numpy as np
from time import sleep

class mouse_tools():
    img = np.full((500, 500, 3), 255, np.uint8)
    prev = np.full((500, 500, 3), 255, np.uint8)
    drawing = False
    ix, iy = -1, -1
    jx = 0
    mode = "Triangle"

    def draw_triangel(self, canvas:list , centerpoint:tuple, sidelenght:int, thickness:int, color):

        height = round(sidelenght*((3**(1/2)/2)))
        top = (centerpoint[0], round(centerpoint[1]-height/2))
        left = (round(centerpoint[0]-sidelenght/2), round(centerpoint[1]+height/2))
        right = (round(centerpoint[0]+sidelenght/2), round(centerpoint[1]+height/2))

        image = cv.line(canvas, top, left, color, thickness)
        image = cv.line(image, top, right, color, thickness)
        image = cv.line(image, left, right, color, thickness)

        return image

    def stack_based_fill(self, canvas:list, point:tuple, color:list):
            """takes a canvas color and point and changes every pixel of the same color in that regeon to the chosen color

            Args:
                color (list): list of rgb values
                point (tuple): tuple containing x and y coordinates for the startingpoint of a fill
            """
            pixels_front = []
            pixel_color = canvas[point[1]][point[0]].copy()
            pixels_front.append(point)
            new_front = []

            while len(pixels_front) > 0:
                for pixel in pixels_front:
                    neighbours = [(pixel[0]+1, pixel[1]), (pixel[0], pixel[1]+1), (pixel[0]-1, pixel[1]), (pixel[0], pixel[1]-1)]

                    for x in neighbours:
                        if f"{canvas[x[1]][x[0]]}" == f"{pixel_color}":
                            new_front.append(x)
                            self.img[x[1]][x[0]] = color

                pixels_front = []
                cv.imshow("Drawline", self.img)

                for pixel in new_front:
                    pixels_front.append(pixel)

                new_front = []

    def Mouse_event(self, event, x, y, flags, params):

        if event == cv.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y
        
        elif event == cv.EVENT_MOUSEMOVE:
            if self.drawing == True:
                if self.mode == "Triangle":
                    self.draw_triangel(self.prev, (self.ix, self.iy), self.jx-self.ix, 3, [255, 255, 255])
                    self.draw_triangel(self.prev, (self.ix, self.iy), x-self.ix, 3, [0, 0, 0])
                    self.jx = x

        elif event == cv.EVENT_LBUTTONUP:
            self.drawing = False
            if self.mode == "Triangle":
                self.draw_triangel(self.img, (self.ix, self.iy), x-self.ix, 3, [0, 0, 0])
                self.prev = self.img.copy()



# main loop
canvas = mouse_tools()
cv.namedWindow("image")
cv.setMouseCallback("image", canvas.Mouse_event)

while True:
    cv.imshow("image", canvas.prev)
    if cv.waitKey(1) & 0xFF == ord("q") or cv.getWindowProperty("image", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()