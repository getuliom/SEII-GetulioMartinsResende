#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]){
    cout<<argv[1]<<endl;
    cout<<argv[2]<<endl;

    FILE * fpointer1=fopen(argv[1],"rb");
    FILE * fpointer2=fopen(argv[2],"wb");

    fgets(argv[1],sizeof(fpointer1),fpointer1);
    
    fclose(fpointer1);
    fclose(fpointer2);
 

    return 0;
}