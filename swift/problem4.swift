/*
Problem 4
左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
では, 3桁の数の積で表される回文数の最大値を求めよ.
*/

var i:Int, j:Int, pnum = 0
for i = 100; i < 1000; i++ {
    for j = i; j < 1000; j++ {
        let n = i * j
        if String(n) == String(String(n).characters.reverse()) && n > pnum {
            pnum = n
        }
    }
}
print("\(pnum)")
