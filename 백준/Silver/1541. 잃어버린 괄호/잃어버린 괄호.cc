#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#pragma warning(disable:4996)
bool is_digit(char c){
  if (c >= '0' && c <= '9') return true;
  else return false;
}
int main(){
  char arr[51];
  scanf("%s", arr);
  int len=strlen(arr), tmp[25]={0}, temp=0, sum=0, cnt=0;
  for (int i=0; i<=len; i++){
    if (is_digit(arr[i])==true){
      temp=temp*10+arr[i]-'0';
    }
    else{
      sum+=temp;
      if(arr[i]=='-'|| i==len){
        tmp[cnt++]=sum;
        sum=0;
      }
      temp=0;
    }
  }
  int result=tmp[0];
  for (int i=1; i<cnt; i++){
    result-=tmp[i];
  }
  printf("%d", result);
}