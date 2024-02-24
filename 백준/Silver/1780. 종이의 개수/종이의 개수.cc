#include<stdio.h>
#include<stdbool.h>
int paper[2200][2200];
int minus=0, zero=0, plus=0, check;
int index1=0, index2=0;
bool is_it_all(int N, int index1, int index2){
  check=paper[index1][index2];
  for (int i=index1; i<index1+N; i++){
    for (int j=index2; j<index2+N; j++){
      if (paper[i][j]!=check) return false;
    }
  }
  return true;
}
void papercut(int N, int index1, int index2){
  if (is_it_all(N, index1, index2)==true){
    if (check==-1) minus++;
    else if (check==0) zero++;
    else plus++;
  }
  else {
    int size=N/3;
    for(int i=0; i<3; i++){
      for (int j=0; j<3; j++){
        papercut(size, index1+size*i, index2+size*j);
      }
    }
  }
}
int main(){
  int N;
  scanf("%d", &N);
  for (int i=0; i<N; i++){
    for (int j=0; j<N; j++){
      scanf("%d", &paper[i][j]);
    }
  }
  papercut(N, 0, 0);
  printf("%d\n%d\n%d", minus, zero, plus);
}