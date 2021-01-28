import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

PictureMatches = 10
pictureNumber = 0
while pictureNumber < PictureMatches:

    def close_event():
        plt.close()
    fig = plt.figure()
    timer = fig.canvas.new_timer(interval=3000)
    timer.add_callback(close_event)
    timer.start()


    File1Image = glob.glob("DownloadedImages/*jpg")[pictureNumber]
    print("The picture: ")
    print(File1Image)
    File2Image = glob.glob("OriginalImages/*jpg")[pictureNumber]
    pictureNumber+=1
    img = cv2.imread(File1Image, 0)
    img2 = img.copy()
    img3 = cv2.imread(File2Image, 0)
    template = cv2.imread('Template.jpg', 0)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img, template, method)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

        plt.subplot(122), plt.imshow(template, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        timer.start()
        plt.show()

        width = 164
        height = 161
        dim = (width, height)
        resizeTemp = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite("result1.jpg", resizeTemp)
        resizeRes = cv2.resize(img3, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite("result2.jpg", resizeRes)

        difference = cv2.subtract(resizeTemp, resizeRes)
        result = not np.any(difference)

        if result is True:
            print("The images are the same")
        else:

            print("not the same")
            cv2.imwrite("IncorrectMatchResultPhoto" + str(pictureNumber) + ".jpg", difference)






