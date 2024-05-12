import java.util.*;

public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, HashSet<Character>> row = new HashMap<>();
        HashMap<Integer, HashSet<Character>> col = new HashMap<>();
        HashMap<Pair<Integer, Integer>, HashSet<Character>> box = new HashMap<>();
        for (int i=0;i<9;i++){
            for (int j=0;j<9;j++){
                char val = board[i][j];
                if (val=='.')continue;
                if (!row.containsKey(i)) row.put(i, new HashSet<>());
                if (!col.containsKey(j)) col.put(j, new HashSet<>());
                Pair<Integer, Integer> boxKey = new Pair<>(i / 3, j / 3);
                if (!box.containsKey(boxKey)) box.put(boxKey, new HashSet<>());

                if (row.get(i).contains(val) || col.get(j).contains(val) || box.get(boxKey).contains(val)) {
                    return false;
                }
                
                row.get(i).add(val);
                col.get(j).add(val);
                box.get(boxKey).add(val);
                
            }
        }
        return true;

        
    }
}
