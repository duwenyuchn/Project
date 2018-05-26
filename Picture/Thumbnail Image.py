from PIL import Image
im = Image.open(r'C:\Users\duwenyu\Desktop\*.jpg')  # 复制路径传入图片对象
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save(r'C:\Users\duwenyu\Desktop\thumb.jpg', 'JPEG')