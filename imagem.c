#include <math.h>
#include <stdio.h>

#define LIN 236
#define COL 417

int main(){
    FILE *fptr, *novo;
    fptr = fopen("car_track2.pgm", "r");
    novo = fopen("teste.pgm", "w");
    for (int i=0; i<LIN; i++){
        for(int j=0; j<COL; j++){
            if(fptr[i][j] < 100){fprintf(novo, "%d", 0);}
            else if(fptr[i][j] < 200){fprintf(novo, "%d", 100);}
            else{fprintf(novo, "%d", 255);}
        }

    }
    fclose(fptr);
    fclose(novo);
    return 0;
}
