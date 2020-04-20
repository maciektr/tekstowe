# Algorytm statycznej kompresji Huffmana
## Format pliku wyjściowego 
Kompresor definiuje, jako format klasy struct, dwa rozmiary zmiennych - zmiennej przechowującej długość użytego w tekście 
alfabetu, oraz częstości wystąpień kolejnych liter, jako bajty (int). Definiuje 
też kodowanie użyte w nagłówku pliku wyjściowego, jako UTF-8.  

Nagłówek skompresowanego pliku wyjściowego składa się z:
* Długości alfabetu (ilości znaków) 
* Wszystkich znaków występujących w alfabecie w kolejności od najczęściej do najrzadziej występującego
* Częstości wystąpień kolejnych znaków

Podczas dekompresji program najpierw odczytuje nagłówek, na podstawie którego konstruuje drzewo Huffmana.

Modyfikacja parametrów kompresora pozwoliłaby potencjalnie na kompresję dłuższych tekstów, większych alfabetów, lub 
oszczędność (liniową względem rozmiaru alfabetu) miejsca na dysku. jednak w celu zachowania przenośności warto byłoby 
wtedy zapisać informację o użytych przy kompresji parametrach w pliku nagłówkowym. Ponieważ w tym zadaniu posługuję się 
krótkim alfabetem polskim, a czas wykonania ogranicza praktyczność zastosowania dla dużych plików zdecydowałem nie 
zawierać tych informacji w pliku nagłówkowym. 

## Otrzymane wyniki
| Rozmiar przed kompresją | Rozmiar po kompresji | Czas wykonania | 
|:-----------------------:|:--------------------:|:--------------:|
| 1.1kB | 0.825kB | 0.049s|
| 9.6kB | 5.8kB | 0.277s|
| 97.7kB| 55.9kB |3.811s| 
| 1.0MB | 595.4kB | 119.829s|