import java.util.*;
class ContainDuplicate {
    public boolean containsDuplicate(int[] nums) {
        //  Method 1
        /*
            Arrays.sort(nums);
            for (int i=1;i<nums.length;i++){
                if (nums[i]==nums[i-1]){
                    return true;
                }
            }
            return false;
        */

        // Method 2
        /*
            HashSet<Integer> seen = new HashSet<>();
            for (int num:nums){
                seen.add(num);
            }
            return seen.size()!=nums.length;
        */

        // Method 3
        
        HashSet<Integer> seen = new HashSet<>();
        for (int num:nums){
            if (seen.contains(num)){
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}