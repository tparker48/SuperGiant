from graphics import *

class KeyboardHandler():
    window = None
    buffer = []
    phrases = []
    phrase_history = []
    history_spot = -1

    def __init__(self, graphics_window):
        self.window = graphics_window

    def read_key(self):
        key = self.window.checkKey()

        if not key:
            return
        
        if key == 'Up':
            if len(self.phrase_history) == 0:
                return

            if self.history_spot == -1:
                self.history_spot = len(self.phrase_history)-1
            else:
                self.history_spot = max(0, self.history_spot - 1)
            self.buffer = [c for c in self.phrase_history[self.history_spot]]

        if key == 'Down':
            if self.history_spot == -1:
                return
            self.history_spot = min(len(self.phrase_history)-1, self.history_spot+1)
            self.buffer = [c for c in self.phrase_history[self.history_spot]]

        if key == 'Return':
            self.history_spot = -1
            self.read_buffer()
            return
        
        if key == 'space':
            self.buffer.append(' ')
            return

        if key == 'BackSpace':
            if len(self.buffer) != 0:
                self.buffer.pop()
            return
        
        if key.isalnum() and len(key) == 1:
            self.buffer.append(key)
            return
    
    def read_buffer(self):
        self.phrases.append(self.get_buffer_string())
        self.phrase_history.append(self.get_buffer_string())
        self.buffer.clear()

    def pop_phrase(self):
        if len(self.phrases) != 0:
            return self.phrases.pop(0)
        else:
            return None
    
    def get_buffer_string(self):
        return ''.join(self.buffer)