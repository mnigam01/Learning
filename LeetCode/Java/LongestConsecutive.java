import java.util.*;

public class LongestConsecutive {

    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i:nums){
            set.add(i);
        }
        int res = 0;
        for (int val:nums){
            int cnt = 0;
            int j = val;
            while (set.contains(j)){
                j++;
                cnt++;
            }
            res = Math.max(res,cnt);
        }

        return res;
        
    }
    
}
