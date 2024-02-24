#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
void dfs(int, int);
int M, N, a[50][50]={0};
int main() {
    int K, T;
    scanf("%d", &T);
    for (int i=0; i<T; ++i){
        int cnt=0;
        scanf("%d %d %d", &M, &N, &K);
        for (int j=0; j<K; ++j){
            int x, y;
            scanf("%d %d", &x, &y);
            a[x][y]=1;
        }
        for (int j=0; j<M; ++j){
            for (int k=0; k<N; ++k){
                if (a[j][k]==1) {
                    dfs(j, k);
                    cnt++;
                }
            }
        }
        printf("%d\n", cnt);
    }
}
void dfs(int x, int y){
    a[x][y]=0;
    if (x + 1 < M && a[x + 1][y] == 1) dfs(x + 1, y);
    if (x - 1 >= 0 && a[x - 1][y] == 1) dfs(x - 1, y);
    if (y + 1 < N && a[x][y + 1] == 1) dfs(x, y + 1);
    if (y - 1 >= 0 && a[x][y - 1] == 1) dfs(x, y - 1);

}