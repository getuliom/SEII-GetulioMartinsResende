#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void torre_de_hanoi(int n, char from_rod, char to_rod,char aux_rod){
    if (n==1){
        cout<<"Mova o disco 1 do cilindro "<< from_rod<<
        " para o cilindro "<<to_rod<<endl;
        return;
    }
    torre_de_hanoi(n-1,from_rod,aux_rod,to_rod);
    cout<<"Mova o disco "<< n <<" do cilindro " <<
     from_rod <<" para o cilindro "<<to_rod<<endl;
    torre_de_hanoi(n-1,aux_rod,to_rod,from_rod);
}

int main(int argc, char *argv[]){
    int n=atoi(argv[1]); //converte o char da linha de comando para int.
    torre_de_hanoi(n,'A','C','B');//chama a funcao
    return 0;
}