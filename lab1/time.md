# Wyniki testów wydajnościowych

## Metodologia 
Pierwszy pomiar czaus wykonałem z użyciem wykorzystywanego przez Olimpiadę Informatyczną pakietu [sio2jail](https://github.com/sio2project/sio2jail), którego specyfika została opisana szerzej w pracy [praca](https://hitagi.dasie.mimuw.edu.pl/files/licencjat/pracalic-logo.pdf), za pośrednictwem wrappera [oiejq](https://oi.edu.pl/static/attachment/20181007/oiejq.tar.gz). Pomiar oparty jest o liczniki sprzętowe. 

Kolejnego pomiaru dokonałem z wykorzystaniem programu time z systemu linux, zapisując zmierzony czas użytkownika. 


## Algorytm naiwny
Czas zmierzony przy pomocy sio2jail:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      | 3ms        | 3658ms          | 1125ms
| Python               |      | 238ms      | ---             | 4028ms
| PyPy                 |      | 45ms       | 8716ms          | 886ms

Czas zmierzony przy pomocy narzędzia time:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      |  3ms       | 700ms           | 300ms
| Python               |      |  85ms      | ---             | 990ms
| PyPy                 |      |  33ms      | 1670ms          | 274ms

## Algorytm kmp

Czas zmierzony przy pomocy sio2jail:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++ z vector         |      | 4ms        | 4572ms          | 673ms 
| C++ z tablicami C    |      | 3ms        | 3517ms          | 668ms   
| Python               |      |  |  |  
| PyPy                 |      |  |  |   

Czas zmierzony przy pomocy narzędzia time:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      | 4ms        | 1100ms          | 223ms      |
| C++ z tablicami C    |      | 3ms        | 1000ms          | 189ms
| Python               |      |            |                 |  
| PyPy                 |      |            |                 | 


## Automat skończony 

