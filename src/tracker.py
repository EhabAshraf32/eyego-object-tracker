import cv2


def main():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam was opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Read the first frame
    ret, frame = cap.read()

    # Stop if the first frame could not be read
    if not ret:
        print("Error: Could not read the first frame.")
        cap.release()
        return

    # Let the user select the object using a bounding box
    bbox = cv2.selectROI("Eyego Object Tracker", frame, False)

    # Display the selected bounding box
    x, y, w, h = bbox
    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.imshow("Eyego Object Tracker", frame)

    # Wait for a key press
    cv2.waitKey(0)

    # Release the webcam
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()