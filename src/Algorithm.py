from Motor import Motor


class PtzAlgorithm(Motor):
    def __init__(self, host, motor_port, frame_dimensions):
        super().__init__(host, motor_port)

        face_w, face_h = 40, 40
        self.face_x_center, self.face_y_center = face_w // 2, face_h // 2
        self.frame_w, self.frame_h = frame_dimensions
        self.frame_x_center = self.frame_w // 2
        self.frame_y_center = self.frame_h // 2
        self.steps = 1

    def decide(self, x, y, w, h):

        if y > self.frame_y_center + self.face_y_center:
            """
            |-----|
            |     |
            |     |
            """

            super().motor_move(self.tilt, self.reverse, self.steps)

        elif y < self.frame_y_center - self.face_y_center:
            """
            |     |
            |     |
            |-----|
            """
            super().motor_move(self.tilt, self.forward, self.steps)


        elif x > self.frame_x_center + self.face_x_center:
            """
            _______
            | |    |
            | |    |
            | |    |
            --------
            """
            super().motor_move(self.pan, self.reverse, self.steps)

        elif x < self.frame_x_center - self.face_y_center:
            """
           _______
           |    | |
           |    | |
           |    | |
           --------
               """
            super().motor_move(self.pan, self.forward, self.steps)
