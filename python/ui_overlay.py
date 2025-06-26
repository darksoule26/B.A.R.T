import tkinter as tk
import ctypes
import time
import threading

class BartOverlay:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 BART CORE")
        self.root.geometry("460x260+20+20")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.92)
        self.root.configure(bg="#0e0e0e")
        self.exit_triggered = False

        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("bart.overlay.ui")
        except:
            pass

        self._drag_data = {"x": 0, "y": 0}
        self._build_ui()
        self._make_draggable()
        self.auto_hide_delay = 30
        self.last_activity = time.time()
        self._start_auto_hide()
        self.hide()

    def _build_ui(self):
        neon = "#00ffe1"
        self.border = tk.Frame(self.root, bg=neon, bd=3)
        self.border.pack(fill="both", expand=True)

        inner = tk.Frame(self.border, bg="#0e0e0e")
        inner.pack(fill="both", expand=True, padx=2, pady=2)

        # Exit button
        btn = tk.Button(inner, text="✖", bg="#0e0e0e", fg="red",
                        bd=0, command=self._exit, font=("Consolas", 12, "bold"),
                        activebackground="#2e0e0e", activeforeground="red")
        btn.place(x=430, y=5, width=25, height=25)

        self.status = tk.Label(inner, text="🤖 Bart AI Active", fg=neon,
                               bg="#0e0e0e", font=("Consolas", 10, "italic"))
        self.status.pack(pady=(10, 2), anchor="w", padx=15)

        self.user_input = tk.Label(inner, text="", fg=neon,
                                   bg="#0e0e0e", font=("Consolas", 11), wraplength=420, justify="left")
        self.user_input.pack(anchor="w", padx=15)

        self.bart_output = tk.Label(inner, text="", fg="white",
                                    bg="#0e0e0e", font=("Consolas", 11), wraplength=420, justify="left")
        self.bart_output.pack(anchor="w", padx=15, pady=(5,10))

        self.wave = tk.Label(inner, text="", fg=neon, bg="#0e0e0e", font=("Consolas", 12))
        self.wave.pack()

        self.slider = tk.Scale(inner, from_=50, to=100, orient="horizontal",
                               label="Transparency %", command=self._upd_alpha,
                               bg="#0e0e0e", fg="white", troughcolor="#222")
        self.slider.set(92)
        self.slider.pack(fill="x", padx=15)

        threading.Thread(target=self._pulse, daemon=True).start()

    def _upd_alpha(self, v): self.root.attributes("-alpha", int(v)/100)

    def _make_draggable(self):
        def start(e): self._drag_data.update({"x": e.x, "y": e.y})
        def drag(e): self.root.geometry(f"+{self.root.winfo_x()+e.x-self._drag_data['x']}+{self.root.winfo_y()+e.y-self._drag_data['y']}")
        self.border.bind("<Button-1>", start)
        self.border.bind("<B1-Motion>", drag)

    def _start_auto_hide(self):
        def loop():
            while True:
                time.sleep(5)
                if not self.exit_triggered and time.time() - self.last_activity > self.auto_hide_delay:
                    self.hide()
        threading.Thread(target=loop, daemon=True).start()

    def _pulse(self):
        cols = ["#00ffe1", "#00e0d4", "#00c0bb", "#00a0a2"]
        i = 0
        while True:
            self.border.config(bg=cols[i%4])
            i+=1
            time.sleep(0.5)

    def update(self, user_input="", bart_response="", status="Listening..."):
        self.status.config(text=f"🎧 {status}")
        self.user_input.config(text=f"You: {user_input}")
        self._typing_effect(bart_response)
        self.last_activity = time.time()
        self.show()
        threading.Thread(target=self._wave_animation, daemon=True).start()

    def _typing_effect(self, text):
        def run():
            self.bart_output.config(text="")
            for c in text:
                self.bart_output.config(text=self.bart_output.cget("text") + c)
                time.sleep(0.02)
        threading.Thread(target=run, daemon=True).start()

    def _wave_animation(self):
        frames = ["▁▂▃▅▆▇█", "▂▃▅▆▇█▁", "▃▅▆▇█▁▂", "▅▆▇█▁▂▃", "▆▇█▁▂▃▅", "▇█▁▂▃▅▆","█▁▂▃▅▆▇"]
        for _ in range(3):
            for fr in frames:
                self.wave.config(text=fr); time.sleep(0.05)
        self.wave.config(text="")

    def show(self): self.root.deiconify()

    def hide(self): self.root.withdraw()

    def _exit(self):
        self.exit_triggered = True
        self.root.quit()
