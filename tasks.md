Po zrobieniu każdego zadania umieść na UPELu zrzut ekranu kodu oraz efektu, jaki on daje. Zalecamy  robić Zadanie 1 na obrazie 'Lena.jpg', który można [pobrać](https://github.com/miwasil/Photo-editor/blob/main/LENA.jpg) z repozytorium (prawy górny róg tuż nad zdjęciem).
# Zadanie 1
Poprzez manipulację macierzą sprawdź jak działają filtry. Spróbuj znaleźć jakiś ciekawy efekt.
Gotowy kod, na którym będziesz działać:
>from PIL import Image, ImageFilter
>
>#**Wczytanie obrazu** <br />
>image = Image.open(image_path)      # **zamiast image_path dodaj zdjęcie np. 'Lena.jpg', ktore masz w tym samym katalogu co projekt** <br />
>
>#**Definicja macierzy filtru**<br />
>matrix = [ <br />
    -2, -1, 0,                  # **przetestuj jak wartości macierzy wpływają na zdjęcie,** <br />
    -1, 1, 1,                   #  **dla najlepszego efektu suma elementów macierzy powinna byc równa około 0, dla niektórych** <br />
    0, 1, 2						# **filtrów również 1** <br />
] <br />
>
>#**Tworzenie obiektu filtra na podstawie macierzy filtru** <br />
>custom_filter = ImageFilter.Kernel((3, 3), matrix, scale=1)     # **jeśli obraz jest zbyt ciemny ustaw scale w przedziale od 0 do 1,** <br />
                                                                #**jesli zbyt jasny ustaw scale większe od 1** <br />
 >                                                               
>#**Zastosowanie filtra do obrazu** <br />
>filtered_image = image.filter(custom_filter) <br />
>
>#**Wyświetlenie obrazu przefiltrowanego** <br />
>filtered_image.show() <br />

**Plik md file zmienia cudzysłowie, więc tam gdzie otwierasz plik LENA.jpg zmień cudzysłów na ten ze swojej klawiatury**


# Zadanie 2
Stwórz graficzny interfejs użytkownika, w którym za pomocą eksploratora plików otworzysz wybrane zdjęcie 
i zastosujesz wcześniej stworzony filtr przyciskiem. Docelowy (przykładowy) wygląd jest podany na zdjęciu poniżej.
## Zadanie 2a
Najpierw stworzysz GUI wyświetlające zdjęcie ze statycznej ścieżki (np. 'Lena.jpg') z przyciskiem, który zaaplikuje filtr. Rób wszystko w tym samym pliku co Zadanie 1.



**Kroki:**
1. zaimportuj bibliotekę tkinter
2. Zakomentuj linijkę, która wyrzuca zdjęcie na ekran, aby na ekranie pojawiało ci się nowo stworzone GUI
>  filtered_image.show()
4. stwórz okno aplikacji
> app = tkinter.Tk()
5. uruchom swoje GUI dodając na końcu kodu
 >app.mainloop()
6. w oknie utwórz Label, w którym będzie przechowywane zdjęcie
> label = tkinter.Label(app, image=zmiennaprzechowujacazdjecie)
7. nie zapomnij Labela wstawić w ramkę, samo stworzenie nie ustawia widżetów
> label.pack()
8. stwórz przycisk do zastosowania filtru na otworzonym zdjęciu
> button1 = tkinter.Button(app, text= 'TEXT', command=pass)
> button1.pack()
> 
**Plik md file zmienia cudzysłowie, więc zmień cudzysłów na ten ze swojej klawiatury**

9. w miejscu pass użyjemy funkcji filtrującej- akcja po naciśnięciu przycisku. Z tego powodu filtr stworzony w Zadaniu 1 zamień na funkcję.
Możesz spróbować zrobić to samemu, ale ze względu na małą ilość czasu radzimy- skopiuj kod poniższy kod, który zawiera moją propozycję zmiany kodu Zad 1 na funkcję. Wprowadź zmiany w filtrze w niej zawartym analogiczne do tych jakich dokonałeś w Zad 1. Jednocześnie kod z zadania 1 musisz usunąć (z pominięciem importowanych bibliotek). **Plik md file zmienia cudzysłowie, więc tam gdzie otwierasz plik LENA.jpg zmień cudzysłów na ten ze swojej klawiatury**
>imageTK = None  
image = Image.open("LENA.jpg")
>
>def filter():  
>&nbsp;&nbsp;&nbsp;global image, imageTK <br />
&nbsp;&nbsp;&nbsp;matrix = [  
&nbsp;&nbsp;&nbsp;-2, -1, 0,  
&nbsp;&nbsp;&nbsp;-1, 1, 1,  
&nbsp;&nbsp;&nbsp;0, 1, 2  
&nbsp;&nbsp;&nbsp;]  
&nbsp;&nbsp;&nbsp;custom_filter = ImageFilter.Kernel((3, 3), matrix, scale=1)  
&nbsp;&nbsp;&nbsp;filtered_image = image.filter(custom_filter)  
&nbsp;&nbsp;&nbsp;imageTK = ImageTk.PhotoImage(filtered_image)  #tutaj zamieniamy zdjęcie na format odpowiedni dla biblioteki tkinter (PIL -> tkinter)
>
>&nbsp;&nbsp;&nbsp;label.configure(image=imageTK)  #ustawiamy zdjęcie w Label <br />
&nbsp;&nbsp;&nbsp;label.image = imageTK


11. w miejscu gdzie tworzysz przycisk, argument 'command' uzupełnij funkcją, którą będzie miał wykonać
>... command=filter)
12. w miejscu gdzie tworzysz Label, argument 'image' uzupełnij konkretną zmienną
>... image=imageTK)

Jeżeli teraz po naciśnięciu przycisku wyświetla Ci się przefiltrowane zdjęcie ze ścieżki podanej w kodzie to super! 

## Zadanie 2b
Możesz przejść do dodania przycisku z opcją otwierania wybranego zdjęcia z twojego systemu plików, na którym to potem będziesz testował swój filtr

1. stwórz nowy przycisk tak jak poprzednio
2. stwórz funkcję (nie przyjmuje ona argumentów) otwierającą obrazek używając:
>image_path = filedialog.askopenfilename()

oraz już ci znanych:
>image = Image.open(image_path)
>imageTK = ImageTk.PhotoImage(image)
>label.configure(image=imageTK)
3. zmienne imageTK, image_path, image ustaw jako globalne w ciele funkcji

 
Otworzy nam to eksplorator plików, w którym będziemy mogli wybrać dowolne zdjęcie
# Zadanie 3

Uzupełniając kod stwórz własny filtr. Można to zrobić w różne sposoby- podane w kodzie. Dodatkowo dodaj przycisk aplikujący ten filtr do swojego GUI stworzonego w zadaniu 2.

