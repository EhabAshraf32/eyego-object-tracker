import cv2


def main():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam was opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Stop if the frame could not be read
        if not ret:
            print("Error: Could not read frame.")
            break

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