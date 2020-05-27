import cv2


class ObjDetection:
    """
    detect object in frame and return positions
    """

    def __init__(self, cascade_path):
        print("\nObject detection has been initialized.")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def show_frame(self, frame):
        cv2.imshow("Context", frame)
        cv2.waitKey(1)

    def detect(self, frame, display_window=True):
        face = self.face_cascade.detectMultiScale(frame, 1.1, 4)
        if len(face) == 1:
            for (x, y, w, h) in face:
                if display_window:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.imshow("Context", frame)
                    cv2.waitKey(1)
                return x, y, w, h

        if display_window:
            cv2.imshow("Context", frame)
            cv2.waitKey(1)
        return None
