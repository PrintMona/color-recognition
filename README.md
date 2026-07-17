# color-recognition
# Color Recognition using OpenCV
## Project Description
This project uses **Python** and **OpenCV** to recognize colors in real time through a webcam.
The program detects three colors:
- Red
- Green
- Blue
When a color is detected, it draws a rectangle around the object and displays the color name on the screen.

## How It Works
1. Open the webcam.
2. Capture video frames.
3. Convert the image from BGR to HSV.
4. Detect the selected colors using HSV ranges.
5. Draw a bounding box around the detected object.
6. Display the color name.

## Technologies Used
- Python
- OpenCV
- NumPy
- Visual Studio Code

## Run the Project
bash
pip install -r requirements.txt
python main.py

## Output

The program detects red, green, and blue objects in real time and displays their names on the screen.
