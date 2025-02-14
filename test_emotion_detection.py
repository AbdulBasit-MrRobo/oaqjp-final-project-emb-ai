import unittest # Import unittest to create and unit tests
from EmotionDetection.emotion_detection import emotion_detector # Import emotion_detector for unit testing

class TestEmotionDetector(unittest.TestCase):
    def test_dominant_emotion(self):
        # Test 1 - Emotion: Joy
        res1 = emotion_detector("I am glad this happened")
        # Check if correct emotion is detected
        self.assertEqual(res1["dominant_emotion"],"joy")

        # Test 2 - Emotion: Anger
        res2 = emotion_detector("I am really mad about this")
        # Check if correct emotion detected or not
        self.assertEqual(res2["dominant_emotion"],"anger")

        # Test 3 - Emotion: Disgust
        res3 = emotion_detector("I feel disgusted just hearing about this")
        # Check if correct emotion detected or not
        self.assertEqual(res3["dominant_emotion"],"disgust")

        # Test 4 - Emotion: Sadness
        res4 = emotion_detector("I am so sad about this")
        # Check if correct emotion detected or not
        self.assertEqual(res4["dominant_emotion"],"sadness")

        # Test 5 - Emotion: Fear
        res5 = emotion_detector("I am really afraid that this will happen")
        # Check if correct emotion detected or not
        self.assertEqual(res5["dominant_emotion"],"fear")

if __name__ == "__main__":
    unittest.main()