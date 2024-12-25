import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import moviepy
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_image(input_file, output_file):
    image = Image.open(input_file)
    image.save(output_file)

def convert_audio(input_file, output_file):
    audio = AudioFileClip(input_file)
    audio.write_audiofile(output_file)

def convert_video(input_file, output_file):
    video = VideoFileClip(input_file)
    video.write_videofile(output_file)

def convert_file():
    input_file = filedialog.askopenfilename(title="Выберите файл")
    if not input_file:
        return

    output_format = format_var.get().strip()  # Получаем выбранный формат
    output_file = filedialog.asksaveasfilename(defaultextension=f".{output_format}", title="Сохранить как")

    try:
        if output_format in ['jpg', 'png', 'gif']:
            convert_image(input_file, output_file)
        elif output_format in ['mp3', 'wav', 'ogg', 'flac']:
            convert_audio(input_file, output_file)
        elif output_format in ['mp4', 'avi', 'mov', 'mkv']:
            convert_video(input_file, output_file)
        else:
            messagebox.showerror("Ошибка", "Неподдерживаемый формат")
            return

        messagebox.showinfo("Успех", "Конвертация завершена!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Создание GUI
root = tk.Tk()
root.title("Конвертер файлов")
root.geometry("250x200")  # Установка размера окна

# Общий список форматов с пометками
formats = [
    "jpg",
    "png",
    "gif",
    "mp3",
    "wav",
    "ogg",
    "flac",
    "mp4",
    "avi",
    "mov",
    "mkv"
]

# Комментарии для отображения
comments = [
    "# Фото",
    "# Аудио",
    "# Видео"
]

# Объединяем комментарии и форматы в один список для отображения
display_list = []
for comment in comments:
    display_list.append(comment)
    if comment == "# Фото":
        display_list.extend(formats[:3])  # jpg, png, gif
    elif comment == "# Аудио":
        display_list.extend(formats[3:7])  # mp3, wav, ogg, flac
    elif comment == "# Видео":
        display_list.extend(formats[7:])  # mp4, avi, mov, mkv

  # Устанавливаем значение по умолчанию

tk.Label(root, text="Выберите формат для конвертации:").pack(pady=(10, 5))

format_var = tk.StringVar(value=formats[0])
format_dropdown = tk.OptionMenu(root, format_var, *display_list)
format_dropdown.pack(pady=(0, 15))

tk.Button(root, text="Конвертировать", command=convert_file).pack(pady=(0, 25))  # Расстояние между кнопками

root.mainloop()
