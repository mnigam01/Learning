import java.util.ArrayList;
import java.util.List;

public class EncodeDecodeString {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        String res = "";
        for (String word:strs){
            res += word.length()+"#"+word;
        }

        return res;
        
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        int i = 0;
        // System.out.println(s);
        while (i<s.length()){
            int l = 0;
            while (i<s.length() && s.charAt(i)!='#'){
                l = l*10+(s.charAt(i)-'0');
                i++;
            }
            i++;
            // System.out.println(l);
            res.add(s.substring(i,i+l));
            i+=l;

        }

        return res;
        
    }
}
