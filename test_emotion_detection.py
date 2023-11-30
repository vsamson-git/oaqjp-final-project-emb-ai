import unittest
from EmotionDetection.emotion_detection import emotion_detector as ed

class TestEmotion(unittest.TestCase):
    def test_emotions(self):
        self.assertEqual(ed('I am glad this happened')['dominant_emotion'], 'joy')
        self.assertEqual(ed('I am really mad about this')['dominant_emotion'], 'anger')
        self.assertEqual(ed('I feel disgusted just hearing about this')['dominant_emotion'], 'disgust')
        self.assertEqual(ed('I am so sad about this')['dominant_emotion'], 'sadness')
        self.assertEqual(ed('I am really afraid that this will happen')['dominant_emotion'], 'fear')

unittest.main()