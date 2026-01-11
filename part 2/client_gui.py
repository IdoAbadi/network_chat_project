import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import simpledialog

class ChatClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        
        # הקמת החלון הראשי
        self.root = tk.Tk()
        self.root.title("Python Network Chat")
        
        # אזור תצוגת ההודעות (Scrollable)
        self.chat_area = scrolledtext.ScrolledText(self.root, state='disabled', height=20, width=50)
        self.chat_area.pack(padx=10, pady=10)
        
        # שורת קלט (Input)
        self.msg_entry = tk.Entry(self.root, width=40)
        self.msg_entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.msg_entry.bind("<Return>", lambda x: self.send_message()) # שליחה ב-Enter

        # כפתור שליחה
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)

    def connect(self):
        try:
            self.client.connect((self.host, self.port))
            # בקשת שם משתמש בחלון קופץ
            self.username = tk.simpledialog.askstring("Username", "Choose your username:", parent=self.root)
            if self.username:
                self.client.send(self.username.encode('utf-8'))
                # התחלת Thread להאזנה להודעות
                threading.Thread(target=self.receive_messages, daemon=True).start()
                self.root.mainloop()
            else:
                self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect: {e}")

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            self.client.send(msg.encode('utf-8'))
            self.msg_entry.delete(0, tk.END) # ניקוי השורה אחרי שליחה

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert(tk.END, message + "\n")
                    self.chat_area.config(state='disabled')
                    self.chat_area.yview(tk.END) # גלילה אוטומטית למטה
                else:
                    break
            except:
                break

# הרצה
if __name__ == "__main__":
    # וודא שה-IP כאן הוא ה-IP של המחשב שמריץ את השרת
    gui_client = ChatClient('192.168.31.229', 5555)
    gui_client.connect()