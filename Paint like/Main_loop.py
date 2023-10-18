import cv2 as cv
import Draw as draw
import numpy as np
import tkinter as tk
from PIL import Image
root = tk.Tk()
root.withdraw()

img_canv = np.full((500, 500, 3), 255, np.uint8)
prev_canv = img_canv.copy()
drawing = False

# start coordinats for mouse
ix, iy = -1, -1
mode = "Triangle"
screen_size = (root.winfo_screenheight(), root.winfo_screenmmwidth())
window = np.full((screen_size[0], screen_size[1], 3), 255)

x_offset = 50
y_offset = 50
x_limit = screen_size[1]
y_limit = screen_size[0]

def Mouse_event(event, x, y, flags, params):
        global drawing, img_canv, prev_canv, ix, iy, mode
        tools = draw.mouse_tools()

        # recods x and y at mous down click
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        
        # as mouse is moved draws a triangle where it is moved and 
        elif event == cv.EVENT_MOUSEMOVE:
            window = 
            icons = draw.icons()
            icons.icon_draw((x, y), False, window)

            if drawing == True:
                if mode == "Triangle":
                    # re draw based on permanent image to create the ilusion of see trough ness
                    prev_canv = img_canv.copy()
                    tools.draw_triangel(prev_canv, (ix, iy), (x-ix)*2, 3, [0, 0, 0])

            # this list comprehension does the same as the code within the below docstring
            # that being drawing the canvas in the window
            window = [window[y][x] if x < x_offset and y < y_offset else prev_canv[y-y_offset][x-x_offset] for x in range(len(window)) for y in range(len(window))]
            window = Image.fromarray(window)

            """
            hold = []
            for x in range(len(window)):
                for y in range(len(window)):
                    if x < x_offset and y < y_offset:
                        hold.append(window[y][x])
                    else:
                        hold.append(prev_canv[y-y_offset][x-x_offset])
            window = hold
            """

        # when mouse is let go draw the triangle to the permanent image
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            if mode == "Triangle":
                tools.draw_triangel(img_canv, (ix, iy), (x-ix)*2, 3, [0, 0, 0])


# main loop
cv.namedWindow("image")
cv.setMouseCallback("image", Mouse_event)

while True:
    cv.imshow("image", window)
    cv.waitKey(1)
    if cv.getWindowProperty("image", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()