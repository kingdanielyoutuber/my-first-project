import tkinter as tk #הגדרת הספריות
import time

# יצירת חלון ראשי
root = tk.Tk()
root.title("MYfirst project")
root.geometry("400x200")

# יצירת מסגרת רקע
BACKGROUNDframe = tk.Frame(root, background="white", padx=10, pady=10)
BACKGROUNDframe.pack(expand=True, fill="both")

# יצירת תווית
label1 = tk.Label(BACKGROUNDframe, text='STTINGS HERE:', font=('Arial', 25))
label1.pack()

# פונקציה לפתיחת חלון לשינוי צבע רקע
def open_toplevel():
    new_window = tk.Toplevel(root)
    new_window.title("main menu bg change")
    new_window.geometry("200x180") # הרקע של החלון שנפתח
    coloroptions  = ["red", "green", "blue", "yellow", "purple", "orange"] #מילון לפונקציה
    for color in coloroptions: #הפונקציה עצמה
        button = tk.Button(new_window, text=color, bg=color, font=("Arial", 15), command=lambda c=color: change_color(c))
        button.pack(pady=5)

# פונקציה לשינוי צבע הרקע
def change_color(color):
    BACKGROUNDframe.config(bg=color)

# כפתור לפתיחת חלון הגדרות
button1 = tk.Button(BACKGROUNDframe, text='clickhere1', font=("Arial", 15), command=open_toplevel)
button1.pack(pady=35)

# יצירת משחק לחיצות
def opentoplevel1():
    new_window1 = tk.Toplevel(root)
    new_window1.title("Click Game")
    new_window1.geometry("300x200")

    class ClickGame:
        def __init__(self, game_window):
            self.game_window = game_window
            self.count = 0
            self.start_time = None

            self.label = tk.Label(game_window, text="לחץ על הכפתור 20 פעמים!", font=("Arial", 14))
            self.label.pack(pady=10)

            self.button = tk.Button(game_window, text="לחץ כאן", font=("Arial", 12), command=self.on_click)
            self.button.pack(pady=10)

        def on_click(self):
            if self.count == 0:
                self.start_time = time.time()  # שמירת זמן התחלה
            
            self.count += 1 #the value of 1 click

            if self.count >= 20:
                elapsed_time = time.time() - self.start_time
                self.show_result(elapsed_time)

        def show_result(self, elapsed_time):
            for widget in self.game_window.winfo_children():
                widget.destroy()  # מחיקת כל הווידג'טים מהחלון
            
            result_label = tk.Label(self.game_window, text=f"כל הכבוד! סיימת ב-{elapsed_time:.2f} שניות!", font=("Arial", 16))  #כותב לך בסיום את התוצאה שלך
            result_label.pack(pady=20)

    game = ClickGame(new_window1)

# כותרת למשחק
game_label = tk.Label(BACKGROUNDframe, text='PLAYHERE:', font=("Arial", 20))
game_label.pack(pady=65)

# כפתור להפעלת המשחק
button2 = tk.Button(BACKGROUNDframe, text='clickhere2', font=("Arial", 15), command=opentoplevel1)
button2.pack()



#חצי מקוד כפתור המשחק לא הבנתי הai copilot עזר לי בו 
#אבל אני עשיתי את settings
#אין סיכוי שעכשיו אני אלמד ספריה חדשה לגמרי "time"

root.mainloop() #shows the window
