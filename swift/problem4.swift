/*
Problem 4
左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
では, 3桁の数の積で表される回文数の最大値を求めよ.
*/
func palindrome(num :Int) -> Bool {
    let number:[Int] = "\(num)".characters.flatMap { Int("\($0)") }
    var rnumber:[Int] = []
    for n in number {
        rnumber.insert(n, atIndex: 0)
    }
    return number == rnumber
}


var pnum = 0
var i:Int, j:Int
for i = 100; i < 1000; i++ {
    for j = i; j < 1000; j++ {
        let n = i * j
        if palindrome(n) {
            pnum = n > pnum ? n : pnum
        }
    }
}
print("\(pnum)")
