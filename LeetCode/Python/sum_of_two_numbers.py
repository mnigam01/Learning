a = 69
b = 12
while a:
    c = a^b
    print(a&b)
    a = (a&b)*2
    b = c
print(a,b)

class Solution {
    public int getSum(int a, int b) {
        if (a==0){
            return b;
        }
        if (b==0){
            return a;
        }
        return getSum(a^b, (a&b)<<1);
        
    }
}