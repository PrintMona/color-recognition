import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # اللون الأحمر
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    # اللون الأخضر
    lower_green = np.array([35,100,100])
    upper_green = np.array([85,255,255])

    # اللون الأزرق
    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])

    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    colors = [
        (red_mask, "RED", (0,0,255)),
        (green_mask, "GREEN", (0,255,0)),
        (blue_mask, "BLUE", (255,0,0))
    ]

    for mask, name, color in colors:

        contours, _ = cv2.findContours(mask,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:

            if cv2.contourArea(cnt) > 500:

                x,y,w,h = cv2.boundingRect(cnt)

                cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)

                cv2.putText(frame,
                            name,
                            (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            color,
                            2)

    cv2.imshow("Color Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
