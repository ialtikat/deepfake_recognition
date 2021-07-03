from functools import cache
from mesonet_classifiers import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os, shutil

def detector():
    MesoNet_classifier = Meso4()
    MesoNet_classifier.load("weights/Meso4_DF")

    image_data_generator = ImageDataGenerator(rescale=1.0 / 255)
    data_generator = image_data_generator.flow_from_directory( "", classes=["Saveimg"] )
    num_to_label = {1: "real", 0: "fake"}
    X, y = data_generator.next()
    probabilistic_predictions = MesoNet_classifier.predict(X)
    predictions = [num_to_label[round(x[0])] for x in probabilistic_predictions]
    uzunlluk=len(predictions)
    fake=predictions.count("fake")
    
    #Dosya içerisine kaydedilen fotoğrafları silmek için
    #Start
    folder = 'Saveimg'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except:
            pass
    #End
    #Resimlerin analiz sonucunda olasılık hesabı.
    if uzunlluk*0.30 < fake:
        return "FAKE"
    else:
        return "REAL"

if __name__=='__main__':
    detector()
