import java.util.*;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        // Method 1
        /*
            for (int i=0;i<nums.length;i++){
                for (int j=i+1;j<nums.length;j++){
                    if (nums[i]+nums[j]==target){
                    
                        return new int[]{i,j};
                    }
                }
            }
            return new int[]{};
        */

        // Method 2
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i=0;i<nums.length;i++){
            if (map.containsKey(target-nums[i])){
                return new int[]{map.get(target-nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
        
    }
    
}
