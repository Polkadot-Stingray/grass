#include <stdio.h>
#include <string.h>
#include <stdbool.h>
char a[1000010], b[37], c[1000010];
int lena, lenb, cnt=0;
bool is_there(int start){
  for (int i=start; i<start+lenb; ++i){
    if(c[i]!=b[i-start]) return false;
  }
  return true;
}
int main(){
  scanf("%s %s", a, b);
  lena=(int)strlen(a);
  lenb=(int)strlen(b);
  for (int i=0; i<lena; ++i){
    c[cnt++]=a[i];
    if (cnt-lenb>=0 && is_there(cnt-lenb)) cnt-=lenb;
  }
  c[cnt]='\0';
  printf("%s\n", cnt ? c : "FRULA");
}