#include <stdio.h>
#include <time.h>

int length(int num);
void itoa(int num, char *cnum);
int palindrome(int num);

int main() {

    int max = 999;
    int min = 999;
    int ans;
    clock_t start,end;
    start = clock();

    // ある程度大きな回文を見つけて、積の要素の最低値を決める
    while (min > 0)
    {
        ans = max * min;
        if (palindrome(ans)) break;
        min--;
    }
    printf("min     = %d\n", min);
    printf("min ans = %d\n", ans);

    // 計算回数カウント用
    int count = 0;

    int heikin = (max + min) / 2;
    for (int i = max - 1; i >= heikin; i--)
    {
        int j = i;
        for (; j >= min; j--)
        {
            // if(i < heikin && j < heikin) break;
            int r = i * j;
            count++;
            if (palindrome(r))
            {
                if (r > ans) ans = r;
                break;
            }
            j--;
        }
    }

    printf("回文 =  %d\n", ans);

    end = clock();
    printf("%d回計算しました。\n", count);
    printf("%.10f秒かかりました\n",(double)(end-start)/CLOCKS_PER_SEC);

    return 0;
}



// 回分系
int length(int num) {
    int len = 0;
    while(num != 0){
        num = num / 10;
        len++;
    }
    return len;
}

void itoa(int num, char *cnum) {
    int len = length(num);
    int i = len - 1;
    for (; i >= 0; i--) {
        cnum[i] = num % 10 + '0';
        num /= 10;
    }
}

int palindrome(int num) {
    int result = 1;
    
    // 数値を数字に変換
    char cnum[length(num) + 1];
    itoa(num, cnum);

    // nullを除いた除いた数字サイズの取得
    int size;
    size = sizeof(cnum) / sizeof(char);
    size = size - 1;

    // 最後の数字の番号取得
    int last = size - 1;
    int center = size / 2;
    // 数字を左右から比較することで回文かどうか判定
    for (int i = 0; i <= center; i++) {
        if (cnum[i] != cnum[last - i]) {
            result = 0;
            break;
        }
    }
    return result;
}
