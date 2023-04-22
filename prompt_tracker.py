import tkinter as tk
from datetime import datetime, timedelta

class PromptTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("GPT-4 Prompt Tracker")
        self.master.geometry("400x250")

        self.prompts_left = 25
        self.last_reset = None
        self.timer_active = False

        self.label = tk.Label(self.master, text=f"Prompts left: {self.prompts_left}/25", font=("Arial", 16))
        self.label.pack(pady=20)

        self.timer_label = tk.Label(self.master, text="Timer: Not Started", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        self.button = tk.Button(self.master, text="Use Prompt", command=self.use_prompt, font=("Arial", 12))
        self.button.pack(pady=10)

        self.reset_button = tk.Button(self.master, text="Reset Prompts", command=self.reset_prompts, font=("Arial", 12))
        self.reset_button.pack(pady=10)

    def use_prompt(self):
        if not self.timer_active:
            self.last_reset = datetime.now()
            self.timer_active = True
            self.update_timer()

        if self.prompts_left > 0:
            self.prompts_left -= 1
        self.label.config(text=f"Prompts left: {self.prompts_left}/25")

    def reset_prompts(self):
        self.prompts_left = 25
        self.last_reset = datetime.now()
        self.label.config(text=f"Prompts left: {self.prompts_left}/25")
        if not self.timer_active:
            self.timer_active = True
            self.update_timer()

    def update_timer(self):
        if self.timer_active:
            now = datetime.now()
            time_since_reset = now - self.last_reset
            time_remaining = timedelta(hours=3) - time_since_reset

            if time_remaining <= timedelta(seconds=0):
                self.reset_prompts()
                self.timer_active = False
                self.timer_label.config(text="Timer: Not Started")
            else:
                hours, remainder = divmod(time_remaining.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.timer_label.config(text=f"Timer: {hours:02d}:{minutes:02d}:{seconds:02d}")
                self.master.after(1000, self.update_timer)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptTracker(root)
    root.mainloop()