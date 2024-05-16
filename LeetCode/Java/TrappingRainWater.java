import java.util.Stack;

public class TrappingRainWater {

    int res = 0;
        int n = height.length;

        // Method 1

        /*
            for (int i=0;i<n;i++){
                int l = i, r = i;
                
                for (int j = 0;j<i;j++){
                    if (height[j]>height[l]){
                        l = j;
                    }
                }

                for (int j = i;j<n;j++){
                    if (height[j]>height[r]){
                        r = j;
                    }
                }

                res += Math.min(height[l],height[r])-height[i];

            }

            return res;
        */

        // Method 2
        /*
            int[] left = new int[n];
            int[] right = new int[n];

            for (int i=0;i<n;i++){
                left[i] = height[i] ;
                if (i!=0)
                left[i] = Math.max(left[i], left[i-1]);
            }
            for (int i=n-1;i>=0;i--){
                right[i] = height[i] ;
                if (i!=n-1)
                right[i] = Math.max(right[i], right[i+1]);
                res += Math.min(left[i],right[i]) - height[i];
            }
            return res;
        */


        // Method 3
        Stack<Integer> stk = new Stack<>();
        for (int i=0;i<n;i++){
            while (stk.size()!=0 && height[stk.peek()]<height[i]){
                int ind = stk.pop();
                if (stk.size()!=0){
                    int w = i-stk.peek()-1;
                    int h = Math.min(height[i], height[stk.peek()]) - height[ind];
                    res += w*h;
                }
            }
            stk.push(i);
        }
        return res;
        
    }
    
}
