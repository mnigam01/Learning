import java.util.*;

public class GroupAnagram {

    public List<List<String>> groupAnagrams(String[] strs) {
        // Method 1
        /*
            HashMap<String, List<String>> map = new HashMap<>();
            for (String word : strs){
                char[] tmp = word.toCharArray();
                Arrays.sort(tmp);
                String sortedWord = Arrays.toString(tmp);
                if (!map.containsKey(sortedWord)){
                    map.put(sortedWord, new ArrayList<>());
                }
                map.get(sortedWord).add(word);

            }
            return new ArrayList<>(map.values());
        */

        HashMap<String, List<String>> map = new HashMap<>();
        for (String word : strs){
            int[] tmp = new int[26];
            for (char c:word.toCharArray()){
                tmp[c-'a']++;
            }
            String sortedWord = Arrays.toString(tmp);
            if (!map.containsKey(sortedWord)){
                map.put(sortedWord, new ArrayList<>());
            }
            map.get(sortedWord).add(word);

        }
        return new ArrayList<>(map.values());
        
    }
    
}
