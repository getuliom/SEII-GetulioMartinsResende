#include <iostream>
#include <cmath>
using namespace std;

float magn,fase,real,imag;

struct Numb{
    float real;
    float imag;
    float magn;
    float fase;
};

void conv_pr(float magn,float fase,float* r,float* im){
    //x= r cos theta
    //y= r sen theta
    *r= magn*cos(fase);
    *im= magn*sin(fase);

}

void conv_rp(float real,float imag,float* m,float* f){
    //r= sqrt(x² + y²)
    // hypot(x,y)= linha acima
    //theta= atan(y/x)
    *m=hypot(real,imag);
    *f=atan(real/imag);
}

int soma(float r1,float r2, float im1,float im2,float* R,float* I){
    *R=r1+r2;
    *I=im1+im2;

    return 0;
}
int subt(float r1,float r2, float im1,float im2,float* R,float* I){
    *R=r1-r2;
    *I=im1-im2;

    return 0;
}
int mult(float r1,float r2, float im1,float im2,float* R,float* I){
    *R=(r1*r2)-(im1*im2);
    *I=(r1*im2)+(im1*r2);
    return 0;
}
int divi(float r1,float r2, float im1,float im2,float* R,float* I){
    *R=(((r1*r2)+(im1*im2))/((im1*im1)+(im2*im2)));
    *I=(((im1*r2)-(r1*im2))/((im1*im1)+(im2*im2)));
    return 0;
}

int main(){
    struct Numb Numb1;
    struct Numb Numb2;
    int choice[4];
    float r,im,m,f,R,I;
    //float magn,fase,real,imag;
    cout<<"Seu primeiro numero esta em forma polar ou retangular?"<<endl;
    cout<<"Digite 1 caso seja polar e 2 caso for retangular = "<<endl;
    cin>>choice[0];

    if (choice[0] == 1){
        cout<<"Digite sua magnitude = "<<endl;
        cin>>Numb1.magn;
        cout<<"Digite sua fase (em radianos) = "<<endl;
        cin>>Numb1.fase;
        conv_pr(Numb1.magn,Numb1.fase,&r,&im);
        Numb1.real=r;
        Numb1.imag=im;
        
    }
    else if (choice[0] == 2){
        cout<<"Digite sua parte real = "<<endl;
        cin>>Numb1.real;
        cout<<"Digite sua parte imaginaria = "<<endl;
        cin>>Numb1.imag;
        conv_rp(Numb1.real,Numb1.imag,&m,&f);
        Numb1.magn=magn;
        Numb1.fase=f;
    }
    cout<<"Seu segundo numero esta em forma polar ou retangular?"<<endl;
    cout<<"Digite 1 caso seja polar e 2 caso for retangular = "<<endl;
    cin>>choice[1];
    if (choice[1] == 1){
        cout<<"Digite sua magnitude = "<<endl;
        cin>>Numb2.magn;
        cout<<"Digite sua fase (em radianos)= "<<endl;
        cin>>Numb2.fase;
        conv_pr(Numb2.magn,Numb2.fase,&r,&im);
        Numb2.real=r;
        Numb2.imag=im;
        
    }
    else if (choice[1] == 2){
        cout<<"Digite sua parte real = "<<endl;
        cin>>Numb2.real;
        cout<<"Digite sua parte imaginaria = "<<endl;
        cin>>Numb2.imag;
        conv_rp(Numb2.real,Numb2.imag,&m,&f);
        Numb2.magn=magn;
        Numb2.fase=f;
    }


    cout<<"\nQual operação você deseja efetuar?"<<endl;
    cout<<"Digite 1 para soma, 2 para subtracao, "<<endl;
    cout<<"3 para multiplicacao e 4 para divisao "<<endl;
    cin>>choice[2];

    if(choice[2]==1){
        soma(Numb1.real,Numb2.real,Numb1.imag,Numb2.imag,&R,&I);
        cout<<"\n\aA soma resulta em = "<<endl;
        cout<<R<<"+i"<<I<<endl;
        cout<<"Voce deseja ver em forma polar? Entao digite 1"<<endl;
        cin>>choice[3];
        if(choice[3]==1){
            conv_rp(R,I,&m,&f);
            cout<<"\n\aA soma resulta em "<<endl;
            cout<<"Amplitude = "<<m<<" Fase (radianos)= "<<f<<endl;
        }
    }
    if(choice[2]==2){
        subt(Numb1.real,Numb2.real,Numb1.imag,Numb2.imag,&R,&I);
        cout<<"\n\aA subtracao resulta em = "<<endl;
        cout<<R<<"+i"<<I<<endl;
        cout<<"Voce deseja ver em forma polar? Entao digite 1"<<endl;
        cin>>choice[3];
        if(choice[3]==1){
            conv_rp(R,I,&m,&f);
            cout<<"\n\aA soma resulta em "<<endl;
            cout<<"Amplitude = "<<m<<" Fase (radianos)= "<<f<<endl;
        }
    }
    if (choice[2]==3){
        mult(Numb1.real,Numb2.real,Numb1.imag,Numb2.imag,&R,&I);
        cout<<"\n\aA multiplicacao resulta em = "<<endl;
        cout<<R<<"+i"<<I<<endl;
        cout<<"Voce deseja ver em forma polar? Entao digite 1"<<endl;
        cin>>choice[3];
        if(choice[3]==1){
            conv_rp(R,I,&m,&f);
            cout<<"\n\aA soma resulta em "<<endl;
            cout<<"Amplitude = "<<m<<" Fase (radianos)= "<<f<<endl;
        }
    }
    if(choice[2]==4){
        divi(Numb1.real,Numb2.real,Numb1.imag,Numb2.imag,&R,&I);
        cout<<"\n\aA divisao resulta em = ";
        cout<<R<<"+i"<<I<<endl;
        cout<<"Voce deseja ver em forma polar? Entao digite 1"<<endl;
        cin>>choice[3];
        if(choice[3]==1){
            conv_rp(R,I,&m,&f);
            cout<<"\n\aA soma resulta em "<<endl;
            cout<<"Amplitude = "<<m<<" Fase (radianos)= "<<f<<endl;
        }
    }


    return 0;
}