import java.util.*;

public class ProductArrayAllExcpetSelf {
    public int[] productExceptSelf(int[] nums) {
        int N = nums.length;
        int[] res = new int[N];
        Arrays.fill(res, 1);
        for (int i=1; i<N;i++){
            res[i] = res[i-1]*nums[i-1];
        }
        int right = 1;
        for (int i=N-1;i>=0;i--){
            res[i]*=right;
            right*=nums[i];
        }
        return res;
        
    }
}
