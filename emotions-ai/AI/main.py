from fer import Video, FER
import cv2
import time
import requests
session = requests.Session()
feed = cv2.VideoCapture(0) #0 --> Default webcam
detector = FER(mtcnn=True) #if set to false, it uses haarcascade

emo_map = {"neutral": "😑", #maps an emoji to the emotions
           "happy": "😀",
           "sad": "😔",
           "angry": "😡",
           "surprise": "😮",
           "disgust": "🤢",
           "fear": "😨"}
emo_grammar = {"neutral": "neutral",
        "happy": "happy",
        "sad": "sad",
        "angry": "angry",
        "surprise": "surprised",
        "disgust": "disgusted",
        "fear": "afraid"}

try:
    while True:
        avail, frame = feed.read() #avail --> if the webcam is available 
        if not avail:
            break
        no_face = False
        result = detector.detect_emotions(frame)
        if not result:
            no_face = True

        for face in result:
            box = face["box"]
            emotions = face["emotions"]

            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            emotion_type = max(emotions, key=emotions.get)
            emotion_score = emotions[emotion_type]
            emotion_text = f"{emotion_type}: {emotion_score:.2f}"
            cv2.putText(frame, emotion_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        session.post('http://localhost:2319/set_emoji', data={'no_face': str(no_face), 'emoji': emo_map[emotion_type], 'emotion': emo_grammar[emotion_type], 'surety': f"{emotion_score:.2f}"}, timeout=0.1)
        # print(emo_map[emotion_type], emotion_type, no_face)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    feed.release()
    cv2.destroyAllWindows()
