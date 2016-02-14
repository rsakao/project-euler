/*
Problem 3
13195 の素因数は 5, 7, 13, 29 である.
600851475143 の素因数のうち最大のものを求めよ.
*/


var num = 600851475143
var sosu = 0
func ck_sosu(s: Int ) -> Bool {
    if s == 1 { return false }
    
    for n in 2..<s {
        if s % n == 0 { return false }
    }
    return true
}

for n in 2...num {
    if !ck_sosu(n) { continue }
    
    while num % n == 0 {
        num = num / n
        sosu = n
    }
    if num <= 1 { break }
}
print("\(sosu)")
