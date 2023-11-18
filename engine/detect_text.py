import easyocr
import cv2

def detect_text(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Initialize EasyOCR
    reader = easyocr.Reader(['en'],gpu=True)

    # Detect text in the image
    boxes = reader.detect(image)

    # Extract text from the detected boxes
    detected_text = []
    for box in boxes:
        detected_text.append(box[0])

    return detected_text[0]