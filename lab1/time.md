# Wyniki testów wydajnościowych

## Metodologia 
Pierwszy pomiar czaus wykonałem z użyciem wykorzystywanego przez Olimpiadę Informatyczną pakietu [sio2jail](https://github.com/sio2project/sio2jail), którego specyfika została opisana szerzej w pracy [praca](https://hitagi.dasie.mimuw.edu.pl/files/licencjat/pracalic-logo.pdf), za pośrednictwem wrappera [oiejq](https://oi.edu.pl/static/attachment/20181007/oiejq.tar.gz). Pomiar oparty jest o liczniki sprzętowe. 

Kolejnego pomiaru dokonałem z wykorzystaniem programu time z systemu linux, zapisując zmierzony czas użytkownika. 


## Algorytm naiwny
Czas zmierzony przy pomocy sio2jail:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      | 3ms        | 3 658ms         | 1 125ms
| Python               |      | 238ms      | 269 830ms       | 4 028ms
| PyPy                 |      | 45ms       | 8 716ms         | 886ms

Czas zmierzony przy pomocy narzędzia time:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      |  3ms       | 700ms           | 300ms
| Python               |      |  85ms      | 1 103 000ms     | 990ms
| PyPy                 |      |  33ms      | 1 670ms         | 274ms

## Algorytm kmp

Czas zmierzony przy pomocy sio2jail:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      | 2ms        | 3 044ms         | 669ms 
| Python               |      | 250ms      | 276 915ms       | 4 617ms
| PyPy                 |      | 54ms       | 5 347ms         | 684ms

Czas zmierzony przy pomocy narzędzia time:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      | 3ms        | 751ms           | 193ms      |
| Python               |      | 93ms       | 53 634ms        | 989ms
| PyPy                 |      | 28ms       | 1 190ms         | 214ms

## Automat skończony 

Czas zmierzony przy pomocy sio2jail:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      |            |                 |  
| Python               |      | 160ms      | 158 177ms       | 3652ms
| PyPy                 |      |            |                 | 

Czas zmierzony przy pomocy narzędzia time:

| Sposób implementacji | Kod  | Test "art" | Test "kruszwil" | Test "AAA" |  
|:--------------------:|:----:|:----------:|:---------------:|:----------:|
| C++                  |      |            |                 |            |
| Python               |      | 72ms       | 36 140ms        | 862ms
| PyPy                 |      |            |                 | 
