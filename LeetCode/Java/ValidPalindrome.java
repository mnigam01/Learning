public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int N = s.length();
        int l=0,r = N-1;
        while (l<r){
            if (!alphaNumeric(s.charAt(l))){
                l++;
            }
            else if (!alphaNumeric(s.charAt(r))){
                r--;
            }
            else{
                char left = Character.toLowerCase(s.charAt(l));
                char right = Character.toLowerCase(s.charAt(r));
                if (left==right){
                    l++;
                    r--;
                }else{
                    return false;
                }

            }
        }
        return true;
        
    }
    public boolean alphaNumeric(char c){

        return (c>='0' && c<='9' ) || (c>='a' && c<='z') || (c>='A' && c<='Z');
    }
}
