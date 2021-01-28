# WaterMark-Image-Comparison
Language:\
Python\
Part 2 of a group project that web scrapped Instagram and downloaded photos with a hashtag or a user handle. The photos then are compared with each other and inform the user if their photos have been copied by other accounts or not.\
Goal: Create a Program that can identify a watermark on an Image using an algorithm.\
By using an image template, the algorithm will search the pixels on the image looking for the closest related location to the template.\
The goal was to compare the selected location found by the algorithm and compare it to the template to determine if it is the same or not.\
This caused my problems with resizing of the photo and is still being worked on.\
This version does compare both photos to each other and will inform the user if it is a copied image or not.\
A timer limits the time showing the algorithms found locations for each photo and will open and close each window accordingly.\
A new Image will be made combining the differences of each photo into one and save it to the main folder.\
