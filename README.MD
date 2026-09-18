# Real-Time Object Tracker

A real-time object tracking system that allows the user to select an object in the first webcam frame and track it as it moves.

## Requirements

- Python 3.x
- OpenCV

## Installation

```bash
pip install -r requirements.txt

```

## Usage

Run the application with:

```bash

python src/tracker.py

Or if you want to open the src folder...

cd src then 
python tracker.py

```

The application opens the default webcam and displays the live video feed.

Press q to exit.

## Implementation

The application currently uses OpenCV to:

- Capture the first frame from the webcam.

- Allow the user to select the target object using a bounding box.

- Store the selected object's bounding box coordinates.