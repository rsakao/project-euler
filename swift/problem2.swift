/*
Problem 2
フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
数列の項の値が400万以下の, 偶数値の項の総和を求めよ.
*/

var fib:[Int] = [1, 2]
var sum = 2
while fib.last! < 4000000 {
    var count = fib.count
    var last = fib.last!
    var last2 = fib[count - 2]
    
    fib.append(last + last2)
    if fib.last! < 4000000 && fib.last! % 2 == 0 {
        sum += fib.last!
    }
}
print("\(sum)")

//var num = 2
//var pre = 1
//var sum2 = 0
//while num < 4000000 {
//    if num % 2 == 0 {
//        sum2 += num
//    }
//    num = num + pre
//    pre = num - pre
//}
//print("\(sum)")


