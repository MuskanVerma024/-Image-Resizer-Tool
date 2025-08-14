from PIL import Image
if __name__ == '__main__':
    image = Image.open('fuzi-san.jpeg')
   # image.show()
    width, height = image.size
print(width, height)
new_width = width//3
new_height = height//3
resized_image = image.resize((new_width , new_height))
print(resized_image.size)
resized_image.show()
resized_image.save("resized-fuzi-san.jpez")