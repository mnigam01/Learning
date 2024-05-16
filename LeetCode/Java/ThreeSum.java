/**
 * 3Sum
 */
public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i != 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int tot = nums[i] + nums[l] + nums[r];
                if (tot > 0) {
                    r--;
                } else if (tot < 0) {
                    l++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    int j = l;
                    while (l < r && nums[j] == nums[l]) {
                        l++;
                    }
                }
            }
        }
        return res;
    }
    
}