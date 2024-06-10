import java.util.*;

public class ValidAnagram {

    
    class Solution {
        public boolean isAnagram(String s, String t) {
            // Method 1
            /* 
                char[] s1 = s.toCharArray(); 
                char[] t1 = t.toCharArray(); 
                Arrays.sort(s1); 
                Arrays.sort(t1); 
                return Arrays.equals(s1,t1);
            */
    
            // Method 2
            /*
                if (s.length()!=t.length())return false;
                HashMap<Character, Integer> counter = new HashMap<>();
                for (char c: s.toCharArray()){
                    counter.put(c, counter.getOrDefault(c,0) + 1);
                }
                for (char c: t.toCharArray()){
                    counter.put(c, counter.getOrDefault(c,0) - 1);
                }
                for (int val: counter.values()){
                    if (val!=0)return false;
                }
                return true;
            */
    
            // Method 3
            int[] counter = new int[26];
            for (char c:s.toCharArray()){
                counter[c-'a']++;
            }
            for (char c:t.toCharArray()){
                counter[c-'a']--;
            }
            for (int val: counter){
                if (val!=0)return false;
            }
            return true;
    
        }
    }
    
}
