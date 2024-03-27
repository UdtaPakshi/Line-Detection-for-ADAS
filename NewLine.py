import numpy as np
import cv2


# Funct to detect lines in a frame
def detect_lines(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred, 50, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame


# Main function
def main():
    cap = cv2.VideoCapture("road_car_view.mp4")

    while True:
        # Read a frame
        ret, frame = cap.read()

        if not ret:
            break

        result_frame = detect_lines(frame)

        # Display result
        cv2.imshow('Line Detection', result_frame)

        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
