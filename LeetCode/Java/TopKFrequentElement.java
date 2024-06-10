import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;

public class TopKFrequentElement {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> d = new HashMap<>();
        for (int val: nums){
            d.put(val, d.getOrDefault(val,0)+1);
        }
        int[][] tmp = new int[d.size()][2];
        int i = 0;
        for (int key:d.keySet()){
            tmp[i][0] = key;
            tmp[i][1] = d.get(key);
            i++;
        }
        Arrays.sort(tmp,(a,b) -> b[1]-a[1]);
        int[] res  = new int[k];
        for (i=0;i<k;i++){
            res[i] = (tmp[i][0]);
        }
        return res;
    }

    public int[] topKFrequent2(int[] nums, int k) {
        HashMap<Integer, Integer> d = new HashMap<>();
        for (int val: nums){
            d.put(val, d.getOrDefault(val,0)+1);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)-> a[0]-b[0]);
        
        for (int key:d.keySet()){
            pq.add(new int[]{d.get(key),key});
            while (pq.size()>k){
                System.out.println(Arrays.toString(pq.peek()));
                pq.poll();
            }
        }
        int[] res  = new int[k];
        int i = 0;

        for (i=0;i<k;i++){
            res[i] = pq.poll()[1];
        }
        return res;

    }

    public int[] topKFrequent3(int[] nums, int k) {
        HashMap<Integer, Integer> d = new HashMap<>();
        for (int val: nums){
            d.put(val, d.getOrDefault(val,0)+1);
        }
        List<Integer>[] buckets = new ArrayList[nums.length+1];
        
        
        for (int key:d.keySet()){
            int val = d.get(key);
            if (buckets[val]==null){
                buckets[val] = new ArrayList<>();
            }
            buckets[val].add(key);
            
        }
        int[] res  = new int[k];
        int i = 0;

        for (int j = buckets.length-1;j>=0;j--){
            if (buckets[j]!=null)
            {    for (int val:buckets[j]){
                    res[i] = val;
                    i++;
                    if (i==k){
                        return res;
                    }
                }
            }
        }
        return res;

    }
    
}
