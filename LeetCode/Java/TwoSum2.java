public class TwoSum2 {
    public int[] twoSum(int[] nums, int target) {

        int l=0,r = nums.length-1;
        while (l<r){
            int tot = nums[l]+nums[r];
            if (tot==target){
                return new int[]{l+1,r+1};
            }else if (tot>target){
                r--;
            }else{
                l++;
            }
        }
        return new int[]{};
        
    }
}
