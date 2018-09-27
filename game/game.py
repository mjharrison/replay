import mss
import time
import win32gui


TITLE = 'Rivals of Aether'
DEFAULT_WIDTH = 976
DEFAULT_HEIGHT = 579


class Rect:
    def __init__(self, rect):
        if len(rect) != 4:
            raise ValueError
        self.__rect = rect
        self.x0 = rect[0]
        self.y0 = rect[1]
        self.x1 = rect[2]
        self.y1 = rect[3]
        self.width = self.x1 - self.x0
        self.height = self.y1 - self.y0
        self.size = (self.width, self.height)


class WindowHandler:
    def __init__(self):
        self.__id = win32gui.FindWindow(None, TITLE)

    def get_rect(self):
        return Rect(win32gui.GetWindowRect(self.__id))

    def move_to_corner(self):
        rect = self.get_rect()
        win32gui.MoveWindow(self.__id, 
            0, 0,
            rect.width, rect.height,
            True)

    def resize_to_default(self):
        rect = self.get_rect()
        win32gui.MoveWindow(
            self.__id,
            rect.x0, rect.y0,
            DEFAULT_WIDTH, DEFAULT_HEIGHT,
            True
        )


class FrameCollector():
    def __init__(self, window_handle):
        self.__sct = mss.mss()
        self.__target = window_handle.get_rect()

    def get_frame(self):
        return self.__sct.grab({
            'left': self.__target.x0,
            'top': self.__target.y0,
            'width': self.__target.width,
            'height': self.__target.height
        })
    
    def get_frame_loop(self, duration, fps=60):
        delta_threshold = 1/fps
        time_start = time.time()
        time_previous = time_start
        while True:
            time_now = time.time()
            delta = time_now - time_previous
            if delta >= delta_threshold:
                time_previous = time_now
                yield self.get_frame()
            if time_now - time_start >= duration:
                break