import cv2
import numpy as np
import random


# init part
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)


def detect_faces(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
    return frame


def detect_eyes(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)  # detect eyes
    width = np.size(img, 1)  # get face frame width
    height = np.size(img, 0)  # get face frame height
    left_eye = None
    right_eye = None
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
        else:
            right_eye = img[y:y + h, x:x + w]
    return left_eye, right_eye


def cut_eyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)

    return img


def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    #print(keypoints)
    return keypoints


def nothing(x):
    pass

def check_eye_collision(eye, location):
    #if one of the eyes hits the correct text, return true
    ret = False
    #print(eye[0][0][0], eye[0][0][0])
    if cv2.pointPolygonTest(location, (eye[0][0][0], eye[0][0][0]), False) != -1:
        ret = True
    return ret


def main():
    # holds the color name and the color code in tuple
    dict_of_color = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0), 'yellow': (0, 255, 255), 'black': (0, 0, 0), 'white': (255, 255, 255)}
    rand = random.choice(list(dict_of_color.keys()))
    color = dict_of_color[rand]
    possible_colors = [color]
    while possible_colors[0] == color:
        possible_colors = [random.choice(list(dict_of_color.keys()))]
    possible_colors.append(rand)
    random.shuffle(possible_colors)
    game_won = False
        

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Guessing Game')
    cv2.createTrackbar('threshold', 'Guessing Game', 0, 255, nothing)
    while not game_won:
        _, frame = cap.read()
        face_frame = detect_faces(frame, face_cascade)
        cv2.putText(frame, 'Press q to QUIT', (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, dict_of_color['red'], 2)
        if face_frame is not None and not game_won:
            eyes = detect_eyes(face_frame, eye_cascade)
            for eye in eyes:
                if eye is not None:
                    threshold = r = cv2.getTrackbarPos('threshold', 'Guessing Game')
                    eye = cut_eyebrows(eye)
                    keypoints = blob_process(eye, threshold, detector)
                    eye = cv2.drawKeypoints(eye, keypoints, eye, dict_of_color['red'], cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    
                    # color guessing game, text is shown on the screen and the user has to guess the color of the text
                    cv2.putText(frame, 'Guess the color of the text', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, dict_of_color['red'], 2)
                    
                    cv2.putText(frame, rand, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    pts_1 = np.array([[170,275],[170,245],[270,245],[270,275],[170,275]], np.int32)
                    pts_1 = pts_1.reshape((-1,1,2))
                    thickness = 3
                    cv2.polylines(frame, [pts_1], False, dict_of_color[possible_colors[0]], thickness)
                    cv2.putText(frame, possible_colors[0], (175,270),  cv2.FONT_HERSHEY_SIMPLEX, 1, dict_of_color[possible_colors[0]], 2)

                    pts_2 = np.array([[380,275],[380,245],[480,245],[480,275],[380,275]], np.int32)
                    pts_2 = pts_2.reshape((-1,1,2))
                    cv2.polylines(frame, [pts_2], False, dict_of_color[possible_colors[1]], thickness)
                    cv2.putText(frame, possible_colors[1], (385,270),  cv2.FONT_HERSHEY_SIMPLEX, 1, dict_of_color[possible_colors[1]], 2)
                    game_won = check_eye_collision(eye, pts_1) or check_eye_collision(eye, pts_2)

        elif game_won:
            cv2.putText(frame, 'You won!', (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, dict_of_color['green'], 2)
        else:
            cv2.putText(frame, 'No face detected', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, dict_of_color['red'], 2)

        cv2.imshow('Guessing Game', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    if game_won:
        print("You guessed the color of the text: " + rand)
    else:
        print("You didn't guess the color of the text")
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

