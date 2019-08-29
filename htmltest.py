from tkinterhtml import HtmlFrame
from tkinter import *

root = Tk()
root.title("KAXs Overlay")
root.geometry('500x250')
frame = HtmlFrame(root, horizontal_scrollbar="auto")

frame.set_content("""
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title></title>
  <meta name="author" content="r4nd0wn">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="5">
</head>

<body>
<iframe frameborder="0"
        scrolling="no"
        id="chat_embed"
        src="https://www.twitch.tv/embed/hebo/chat"
        height="500"
        width="350">
</iframe>
</body>
</html>
""")
root.mainloop()