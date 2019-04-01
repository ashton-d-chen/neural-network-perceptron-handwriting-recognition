from PIL import Image


def loadImage():
    WIDTH = 28
    HEIGHT = 28
    im = Image.open("input.bmp")
    size = im.size
    print size[0]
    print size[1]
    im = im.resize((WIDTH,HEIGHT))
    size = im.size
    print size[0]
    print size[1]
    temp = []
    print "from string"
    for i in range(len(im.getdata())):
        temp.append(im.getdata()[i])
    print "end"
    im = temp
    result = []

    for i in range(0,28):
        test = ''
        for j in range(0,28):
            if im[i*28+j] == (255,255,255):
                result.append(' ')
            elif im[i*28+j] == (0,0,0):
                result.append('#')
            test += result[i*28+j]
        print test

    print result
    print 'hihi'

    text_file = open("output", "w")
    for i in range(0,27):
        test = ''
        for j in range(0,27):
            if result[i*28+j] == ' ':
                if result[(i+1)*28+j] == '#':
                    result[i*28+j] = '+'
                elif result[(i-1)*28+j] == '#':
                    result[i*28+j] = '+'
                elif result[i*28+j+1]== '#':
                    result[i*28+j] = '+'
                elif result[i*28+j-1] == '#':
                    result[i*28+j] = '+'
            text_file.write(result[i*28+j])
        text_file.write("\n")
        
    text_file.close()

loadImage()
            
