from PIL import Image

mode = "RGB" # binary, only black and white
size = (400, 400)
color = "black"

img = Image.new(mode, size, color)
# img.show()

pixels = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixels[x, y] = (x, y, 100)

for x in range(img.size[0]):
    pixels[x, x] = (0, 0, 0)

# img.show()


img2 = Image.new("1", size, color = "white")
#img2.show()

pix = img2.load()
for x in range(img2.size[0]):
    pix[x, x] = 1

#img2.show()


a = ['0101', '0111', '0101', '0111']


def paint_gold(frame):
    print(frame)
    size = frame.__len__()
    gold = Image.new("1", (4, 4), color = "black")
    bits = "".join(frame)
    pxls = gold.load()

    print(bits)
    for x in range(gold.size[0]):
        for y in range( gold.size[1]):
            #print(x*img.size[0]+y)
            if bits[y*gold.size[0]+x] == "1":
                print("jest 1 dla {} {} {}".format(x*gold.size[0]+y, x, y))
                pxls[x, y] = 0
            else:
                pxls[x, y] = 1

    #gold = gold.resize((128,128))
    gold.show()
    gold.save("gold_4.BMP", "BMP")

    if size == 16:
        pass

    #print("GOLD FRAME!" + str(frame))

paint_gold(a)