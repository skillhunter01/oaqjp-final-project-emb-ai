import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger')

        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear')

        print("Test Results:")
        test_cases = [
            ("I am glad this happened", result1),
            ("I am really mad about this", result2),
            ("I feel disgusted just hearing about this", result3),
            ("I am so sad about this", result4),
            ("I am really afraid that this will happen", result5)
        ]

        for text, result in test_cases:
            print(f"\nText: {text}")
            print(f"Dominant Emotion: {result['dominant_emotion']}")
            print(f"Scores: anger: {result['anger']:.2f}, disgust: {result['disgust']:.2f}, "
                  f"fear: {result['fear']:.2f}, joy: {result['joy']:.2f}, sadness: {result['sadness']:.2f}")

if __name__ == "__main__":
    unittest.main()