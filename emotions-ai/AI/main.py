import serial
import requests
import time
import cv2
from fer import FER
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

session = requests.Session()
feed = cv2.VideoCapture(0)  # 0 --> Default webcam
detector = FER(mtcnn=True)  # if set to false, it uses haarcascade
port = 'COM3'
ser = serial.Serial(port=port, baudrate=9600)

emo_arduino = {
    "angry": 0,
    "disgust": 1,
    "fear": 2,
    "happy": 3,
    "sad": 4,
    "surprise": 5,
    "neutral": 6,
}
emo_map = {"neutral": "😑",  # maps an emoji to the emotions
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
timeout = 0.1
try:
    while True:
        avail, frame = feed.read()  # avail --> if the webcam is available
        if not avail:
            break
        no_face = False
        result = detector.detect_emotions(frame)
        if not result:
            no_face = True
            emotion_type = 'neutral'
            emotion_score = 100
            emotion_text= 'blah'

        for face in result:
            box = face["box"]
            emotions = face["emotions"]

            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            emotion_type = max(emotions, key=emotions.get)
            emotion_score = emotions[emotion_type]
            emotion_text = f"{emotion_type}: {emotion_score:.2f}"
            cv2.putText(frame, emotion_text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # breakpoint()
        # print(emotion_type)
        try:
            session.post('http://localhost:2319/set_emoji', data={'no_face': str(
                no_face), 'emoji': emo_map[emotion_type], 'emotion': emo_grammar[emotion_type], 'surety': f"{int(emotion_score*100)}"}, timeout=timeout)
        except requests.Timeout as te:
            print(f"timeout with timeout = {timeout}s; increasing by 0.5s")
            timeout += 0.5
            continue
        # print(emo_map[emotion_type], emotion_type, no_face)
        if not no_face:
            ser.write(f'{emo_arduino[emotion_type]}:'.encode())
        elif no_face:
            ser.write('2319:'.encode())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.25)
except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    feed.release()
    cv2.destroyAllWindows()
