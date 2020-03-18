# Makefile

main: kmp naive fsm

kmp: 
	g++ -static -O2 -Wall -Wshadow kmp.cpp -o kmp.o
naive: 
	g++ -static -O2 -Wall -Wshadow naive.cpp -o naive.o
fsm: 
	g++ -static -O2 -Wall -Wshadow fsm.cpp -o fsm.o
table:
	g++ -static -O2 -Wall -Wshadow fsm_table.cpp -o fsm_table.o
	g++ -static -O2 -Wall -Wshadow kmp_table.cpp -o kmp_table.o