from PIL import Image
import numpy as np

"""
przykładowe pomysły: 
1. W linijce 49 (img_out.putpixel(...) - mozemy zamiast min ustawiac max, np.mean, np.median - dla numpy przekonwertuj na int

2. Zakomentuj linijke 49 i odkomentuj 28-32 oraz 50-53 - wtedy mozesz manipulowac wartosciami macierzy dla uzyskania ciekawych efektow

Zachęcam do wymyslenia wlasnego filtru :)

"""



# Wczytanie obrazu
image = Image.open(image_path)          # zastąp image_path obrazem np. 'LENA.jpg'

# Konwertowanie obrazu na tryb RGB
image = image.convert("RGB")
img_out = image.convert("RGB")
width, height = image.size

matrix_size = 6            #matrix_size okresla dlugosc macierzy - tym mozemy manipulowac dla lepszego efektu, jak za dlugo liczy polecam zmniejszyc :)
pixs_taken = matrix_size // 2


#matrix_size = 2
#pixs_taken = matrix_size // 2
#filter_matrix = np.array([[-1, -1, -1],
#                          [ -1, 5, -1],
#                          [-1, -1, -1]])

for y in range(pixs_taken + 1, height - pixs_taken - 1):            #wczytujemy kazdy piksel ze zdjęcia
    for x in range(pixs_taken + 1, width - pixs_taken - 1):
        list_R = []
        list_G = []
        list_B = []
        normalized_list = []
        count = 0
        for i in range(x - pixs_taken, x + pixs_taken + 1):         #pobieramy macierz o wielkosci matrix_size x matrix_size
            for j in range(y - pixs_taken, y + pixs_taken + 1):
                pixel_colour = image.getpixel((i, j))
                list_R.append(pixel_colour[0])                  #pobieramy dane o intensywnosci koloru kazdego pixela z macierzy
                list_G.append(pixel_colour[1])
                list_B.append(pixel_colour[2])
                normalized_list.append((list_R[count] + list_G[count] + list_B[count]) / 3)
                count += 1
        img_out.putpixel((x, y), (int(np.median(list_R)), int(np.median(list_G)), int(np.median(list_B))))
        #normalized_matrix = np.reshape(normalized_list, (3, 3))
        #result_matrix = normalized_matrix * filter_matrix
        #img_out.putpixel((x,y), int(np.sum(result_matrix)))
#img_out = img_out.convert('L')              # zamieniamy zdjecie na czarno-biale
img_out.show()