#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#pragma warning(disable:4996)
int main() {
  int N, dp[12];
  dp[1]=1;
  dp[2]=2;
  dp[3]=4;
  for (int i=4; i<12; i++) dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
  scanf("%d", &N);
  for (int i=0; i<N; i++){
    int fin;
    scanf("%d", &fin);
    printf("%d\n", dp[fin]);
  }

  return 0;
}