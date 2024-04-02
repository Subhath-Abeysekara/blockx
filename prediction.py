import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def predict_user_score(datapoint):
    numpy_data = np.array(datapoint)
    print(numpy_data)
    load_model = joblib.load('user_score_predict_model_final.h5')
    predictions = load_model.predict(numpy_data.reshape(1, -1))
    return predictions[0]

def detect_post_content(img_array):
    label = {'Very Bad':4, 'Bad':3, 'Neutral':2, 'Good':1, 'Very Good':0}
    load_model = joblib.load('post_level_predict_model_final.h5')
    predictions = load_model.predict(img_array)
    post_prediction = [key for key, value in label.items() if value == predictions]
    print(post_prediction)
    return post_prediction

# datapoint = [5999,258,770,14,2,5347,1,0,1,24,236,0,3319,1,5,201]
# datapoint = [14,0,266.0,3005,2378,6304,3336,0]
# print(predict_user_score(datapoint))
# text = "In the vast expanse of the cosmos, where stars twinkle like distant dreams and galaxies swirl in majestic spirals, lies the awe-inspiring mystery of the universe. It's a tapestry woven with threads of gravity, matter, and energy, where celestial bodies dance to the silent rhythm of cosmic forces. From the fiery birth of stars in stellar nurseries to the serene grandeur of black holes lurking in the cosmic shadows, the universe presents an endless array of wonders waiting to be explored."
# fake_news_detect(text)