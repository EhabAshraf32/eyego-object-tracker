**# Real-Time Object Tracker**

A real-time object tracking system that allows the user to select an object in the first webcam frame and track it as it moves.

**## Requirements**

* Python 3.x
* OpenCV

**## Project Structure**

```text
eyego-object-tracker/
├── src/
│   └── tracker.py
├── requirements.txt
├── README.md
└── .gitignore
```

**## Installation**

```bash
pip install -r requirements.txt
```

**## Usage**

Run the application from the project root:

```bash
python src/tracker.py
```

The application opens the default webcam.

Select the object you want to track by drawing a bounding box around it in the first frame.

The selected object will then be tracked in real time, with the updated bounding box displayed on the live video feed.

Press `q` to exit the application, or use `Ctrl+C` in the terminal to stop the process.

**## Implementation**

The system uses OpenCV to:

* Capture frames from the webcam.
* Allow the user to select the target object using a bounding box.
* Initialize a **CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability)** tracker using the selected object.
* Track the selected object across subsequent frames.
* Display the updated bounding box and tracking status on the live video feed.

**CSRT** was chosen because it provides good tracking accuracy and robustness for real-time object tracking while being suitable for webcam-based applications.
