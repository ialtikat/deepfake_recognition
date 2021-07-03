import cv2
import mediapipe as mp


class FaceDetector():
    def __init__(self, minDetectionCon = 0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw= mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img,count, draw= True):
        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results= self.faceDetection.process(imgRGB)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate (self.results.detections):
                bboxC= detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox=int(bboxC.xmin * iw-40), int(bboxC.ymin * ih-40), int(bboxC.width * iw+50), int(bboxC.height * ih+60)
                bboxs.append([id, bbox, detection.score])
                self.imgDraw(img, bbox, count) #Çerçeve
                # cv2.putText(img, f'{int(detection.score[0]*100)}%',(bbox[0] ,bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3 ) #Yüzdelik Skor


        return img,  bboxs

    #Yüzü kare içine aldığımız kısım 
    def imgDraw(self, img, bbox, count, l = 30, t = 5, rt = 1):
        try:
            x, y, w, h = bbox
            x1, y1 = x+ w, y + h
            count=count
            cv2.rectangle(img, bbox, (0, 0, 255), rt)
            
            cv2.imwrite("Saveimg/Face."+str(count)+".jpg",img[y: y+h, x: x + w])
            

            cv2.line(img, (x, y), (x + l, y), (0, 0, 255), t)
            cv2.line(img, (x, y), (x, y + l), (0, 0, 255), t)

            cv2.line(img, (x1, y), (x1 - l, y), (0, 0, 255), t)
            cv2.line(img, (x1, y), (x1, y + l), (0, 0, 255), t)

            cv2.line(img, (x, y1), (x + l, y1), (0, 0, 255), t)
            cv2.line(img, (x, y1), (x, y1 - l), (0, 0, 255), t)

            cv2.line(img, (x1, y1), (x1 - l, y1), (0, 0, 255), t)
            cv2.line(img, (x1, y1), (x1, y1 - l), (0, 0, 255), t)

            return img
        except:
            pass

def main(cap):
    cap = cap
    detector = FaceDetector()
    count =0 #Resimlerin kaydedilirken isimlendirmek için.
    while True:
        success, img =cap.read()
        count+=1
        img, bboxs = detector.findFaces(img, count)
        cv2.imshow("Image", img)
        if cv2.waitKey(5) & 0xFF == ord ('q'):
            break
        
if __name__ == '__main__': 
    main()
    
