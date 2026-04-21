import serial
import tkinter as tk
from tkinter import ttk, messagebox
import winsound   # Windows ke liye sound

arduino = serial.Serial('COM4', 9600)

window = tk.Tk()
window.title("Smart Water IoT Dashboard")
window.geometry("480x520")
window.config(bg="#0b1220")

# TITLE
title = tk.Label(window, text="💧 SMART WATER DASHBOARD",
                 font=("Arial", 18, "bold"),
                 bg="#0b1220", fg="white")
title.pack(pady=15)

# VALUE DISPLAY
value_label = tk.Label(window, text="Sensor Value: --",
                       font=("Arial", 14),
                       bg="#0b1220", fg="white")
value_label.pack(pady=10)

# STATUS DISPLAY
status_label = tk.Label(window, text="Waiting Data...",
                        font=("Arial", 18, "bold"),
                        bg="#0b1220", fg="yellow")
status_label.pack(pady=10)

# PROGRESS BAR
progress = ttk.Progressbar(window, orient="horizontal",
                           length=380, mode="determinate")
progress.pack(pady=25)
progress["maximum"] = 1023

alert_shown = False

def update():
    global alert_shown

    if arduino.in_waiting:
        data = arduino.readline().decode().strip()

        try:
            val = int(data)

            # update UI
            value_label.config(text=f"Sensor Value: {val}")
            progress["value"] = val

            # LOW
            if val < 300:
                status_label.config(text="🟢 WATER LOW", fg="lightgreen")
                alert_shown = False

            # MEDIUM
            elif val < 700:
                status_label.config(text="🟡 WATER MEDIUM", fg="orange")
                alert_shown = False

            # FULL ALERT
            else:
                status_label.config(text="🔴 WATER FULL!", fg="red")

                # popup alert (sirf ek baar)
                if not alert_shown:
                    messagebox.showwarning("Alert", "Water Tank is FULL!")
                    winsound.Beep(1000, 500)  # beep sound
                    alert_shown = True

        except:
            status_label.config(text="Reading Error", fg="red")

    window.after(800, update)

update()
window.mainloop()