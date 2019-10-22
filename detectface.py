import cv2

#entering the location of video
path = "WhatsApp Video 2019-09-08 at 20.25.50.mp4"
vid = cv2.VideoCapture(path)

# adding dataset
data = cv2.CascadeClassifier("data.xml")
#reading video
while True:
    ret,video = vid.read()
    #fx = videowidth and fy= videoheight
    video = cv2.resize(video, None, fx=0.5,fy=0.5)
    if ret:
        gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        faces = data.detectMultiScale(video,1.2)
        # x, y, w, h are x co-ordiante y co-ordiante width and height of detected object
        for x, y, w, h in faces:
            cv2.rectangle(video, (x, y), (x + w, y + h), (255, 0, 255), 5)
        if cv2.waitKey(1) == 27:
            break
        elif cv2.waitKey(1) == ord("q"):
            break


        cv2.imshow("output",video)
    else:
        print("Some Error")
cv2.destroyAllWindows()
vid.release()




