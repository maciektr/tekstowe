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
| Rozmiar przed kompresją | Rozmiar po kompresji | Współczynnik kompresji |  Czas kompresji | Czas dekompresji | 
|:-----------------------:|:--------------------:|:----------------------:|:--------------:|:----------------:|
| 1.1kB | 0.825kB | 25% | 0.058s | 0.043s
| 9.6kB | 5.8kB | 39.5% | 0.238s | 0.063s
| 97.7kB| 55.9kB | 42.7% | 3.46s | 0.223s 
| 1.0MB | 0.595MB | 40.5% | 110.5s | 2.17s

# Algorytm dynamicznej kompresji Huffmana
## Format pliku wyjściowego 
Kompresor definiuje, jako UTF-8, kodowanie użyte przy zapisie całych liter. W pierwszym bajcie pliku znajduje się liczbą bitów które zostały dopełnione zerami, tak aby plik składał się z całkowitej liczby bajtów. Taką ilość bitów należy pominąć na końcu parsowania pliku. Następny bajt określa zakodowany pierwszy znak pliku.  

## Otrzymane wyniki
| Rozmiar przed kompresją | Rozmiar po kompresji | Współczynnik kompresji |  Czas kompresji | Czas dekompresji | 
|:-----------------------:|:--------------------:|:----------------------:|:--------------:|:----------------:|
| 1kB | 0.71kB | 29% | 0.088s | 0.033s
| 10.3kB | 6.9kB | 33% | 0.583s | 0.065s
| 103kB| 69.4kB | 32.6% | 6.011s | 0.432s 
| 1.0MB | 0.693MB | 30.7% | 69.681s | 3.981s