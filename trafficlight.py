# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: Traffic Light
# Version: 1.0: Base version by author
import tkinter as tk

phases = ((True, False, False),
          (True, True, False),
          (False, False, True),
          (False, True, False))


class TrafficLight:
    # Initialize the Traffic Light parameters
    def __init__(self, _window):
        self._window = _window
        self.canvas = None
        self.next_button = None
        self.quit_button = None
        self.font_style = ('Arial Bold', 15)
        self.quit_font_style = ('Arial', 10)
        self.pos = 0
        self.initialize_signal()

    # Initialize the Traffic Light Board
    def initialize_signal(self):
        self.canvas = tk.Canvas(window, width=220, height=640, bg='black')
        self.next_button = tk.Button(window, text="S T A R T", font=self.font_style, padx=4, pady=2,
                                     borderwidth=3, width=8, height=1, bg='white', command=self.button_click)
        self.quit_button = tk.Button(window, text="Q U I T", font=self.quit_font_style, command=window.destroy)
        self.next_button.grid(row=1, column=0)
        self.quit_button.grid(row=2, column=0)
        self.canvas.grid(row=0)

    # Perform the Traffic Light Phases
    def button_click(self):
        self.pos = self.pos % len(phases)
        self.next_button.config(text=' N E X T ')
        self.canvas.create_oval(20, 30, 200, 210, outline='#7a7873', width=10, fill='red' if phases[self.pos][0]
                                else 'black')
        self.canvas.create_oval(20, 230, 200, 410, outline='#7a7873', width=10, fill='yellow' if phases[self.pos][1]
                                else 'black')
        self.canvas.create_oval(20, 430, 200, 610, outline='#7a7873', width=10, fill='green' if phases[self.pos][2]
                                else 'black')
        self.pos += 1


if __name__ == '__main__':
    window = tk.Tk()
    window.title('S I G N A L')
    window.config(background='black')
    window.config(borderwidth=10)
    window.iconbitmap(window, default="traffic_light.ico")
    traffic_light = TrafficLight(window)
    window.mainloop()
