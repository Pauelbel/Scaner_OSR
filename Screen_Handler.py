# Библиотека tkinter (графика)
import tkinter as tk
# Библиотека (скриншот)
from PIL import Image, ImageTk, ImageGrab, ImageEnhance
#######################
from io import StringIO
import win32clipboard
#######################


root = tk.Tk()          # Главное окно
root.resizable(0, 0)    # Запрещаем разворачивать окно

# Метод отвечает за работу с изображением
def show_image(image):
    win = tk.Toplevel()
    win.image = ImageTk.PhotoImage(image)
    tk.Label(win, image=win.image).pack()
    win.grab_set()
    win.wait_window(win)

# Метод отвечает за работу с захватом экрана
def area():
    x1 = y1 = x2 = y2 = 0
    roi_image = None

    def on_mouse_down(event):
        nonlocal x1, y1
        x1, y1 = event.x, event.y
        canvas.create_rectangle(x1, y1, x1, y1, outline='yellow', tag='roi')

    def on_mouse_move(event):
        nonlocal roi_image, x2, y2
        x2, y2 = event.x, event.y
        canvas.delete('roi-image')  # удалить старое наложение изображения
        # получить изображение выбранного региона
        roi_image = image.crop((x1, y1, x2, y2))
        canvas.image = ImageTk.PhotoImage(roi_image)
        canvas.create_image(x1, y1, image=canvas.image,
                            tag=('roi-image'), anchor='nw')
        canvas.coords('roi', x1, y1, x2, y2)
        # убедитесь, что выделенный прямоугольник находится сверху наложенного изображения
        canvas.lift('roi')

    root.withdraw()  # скрыть корневое окно
    image = ImageGrab.grab()  # захватить весь экран в качестве фона выбранного региона
    bgimage = ImageEnhance.Brightness(image).enhance(
        0.3)  # затемнить захваченное изображение
    # создать полноэкранное окно для выполнения действия выбора региона
    win = tk.Toplevel()
    win.attributes('-fullscreen', 1)
    win.attributes('-topmost', 1)
    canvas = tk.Canvas(win, highlightthickness=0)
    canvas.pack(fill='both', expand=1)
    tkimage = ImageTk.PhotoImage(bgimage)
    canvas.create_image(0, 0, image=tkimage, anchor='nw', tag='images')
    # привязать события мыши для выбора региона
    win.bind('<ButtonPress-1>', on_mouse_down)
    win.bind('<B1-Motion>', on_mouse_move)
    win.bind('<ButtonRelease-1>', lambda e: win.destroy())
    # используйте клавишу Esc, чтобы отменить захват
    win.bind('<Escape>', lambda e: win.destroy())
    # сделать окно захвата модальным
    win.focus_force()
    win.grab_set()
    win.wait_window(win)
    root.deiconify()  # восстановить корневое окно
    # показать изображение захвата
   

    if roi_image:
        show_image(roi_image)
##############################################
    """ if roi_image:
        def send_to_clipboard(clip_type, data):
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(clip_type, data)
            win32clipboard.CloseClipboard()
  
        filepath = roi_image
        image = Image.open(filepath)
        
        output = StringIO()
        image.convert("RGB").save(output, "PNG")
        data = output.getvalue()[8:]
        output.close()
        
        send_to_clipboard(win32clipboard.CF_DIB, data) """

#######################

# Дизайн кнопок и выполнение команды
tk.Button(root, text='Захват экрана', width=30, command=area).pack()
tk.Button(root, text='Потом придумаю', width=30, bg="sky blue").pack()

# Завершаем работу и зацикливаем приложение
root.mainloop()
