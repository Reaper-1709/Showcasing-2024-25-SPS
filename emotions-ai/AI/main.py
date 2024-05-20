from fer import Video, FER
import cv2
import time

feed = cv2.VideoCapture(0)
detector = FER(mtcnn=True)

emo_map = {"neutral": "😑",
           "happy": "😀",
           "sad": "😔",
           "angry": "😡",
           "surprise": "😮",
           "disgust": "🤢",
           "fear": "😨"}

try:
    while True:
        avail, frame = feed.read() #avail --> if the webcam is available 
        if not avail:
            break
        result = detector.detect_emotions(frame)
        for face in result:

            box = face["box"]
            emotions = face["emotions"]

            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            emotion_type = max(emotions, key=emotions.get)
            emotion_score = emotions[emotion_type]
            emotion_text = f"{emotion_type}: {emotion_score:.2f}"
            cv2.putText(frame, emotion_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        print(emo_map[emotion_text.split(':')[0]], emotion_type)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    feed.release()
    cv2.destroyAllWindows()