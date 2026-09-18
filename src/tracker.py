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

    # Let the user select the object to track
    bbox = cv2.selectROI("Eyego Object Tracker", frame, False)

    # Create the CSRT tracker
    tracker = cv2.TrackerCSRT_create()

    # Initialize the tracker with the selected object
    tracker.init(frame, bbox)

    while True:
        # Read the next frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Update the tracker with the new frame
        success, bbox = tracker.update(frame)

        if success:
            # Convert the bounding box values to integers
            x, y, w, h = [int(value) for value in bbox]

            # Draw the updated bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Display tracking status
            cv2.putText(
                frame,
                "Tracking",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        else:
            # Display a message if tracking fails
            cv2.putText(
                frame,
                "Tracking lost",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        # Display the current frame
        cv2.imshow("Eyego Object Tracker", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the webcam
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()