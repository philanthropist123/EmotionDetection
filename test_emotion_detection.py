import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_statement_joy(self):
        text = "I am glad this happened"
        result_dict = emotion_detector(text)
        self.assertEqual(result_dict['dominant_emotion'], 'joy')

    def test_statement_anger(self):
        text = "I am really mad about this"
        result_dict = emotion_detector(text)
        self.assertEqual(result_dict['dominant_emotion'], 'anger')

    def test_statement_disgust(self):
        text = "I feel disgusted just hearing about this"
        result_dict = emotion_detector(text)
        self.assertEqual(result_dict['dominant_emotion'], 'disgust')

    def test_statement_sadness(self):
        text = "I am so sad about this"
        result_dict = emotion_detector(text)
        self.assertEqual(result_dict['dominant_emotion'], 'sadness')

    def test_statement_fear(self):
        text = "I am really afraid that this will happen"
        result_dict = emotion_detector(text)
        self.assertEqual(result_dict['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()