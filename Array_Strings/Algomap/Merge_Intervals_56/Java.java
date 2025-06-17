import java.util.*;
public class mergeIntervals {
    public static List<int[]> merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0])); //Sắp xếp

        List<int[]> merged = new ArrayList<> ();

        for (int[] interval: intervals) {
            if (merged.isEmpty() || merged.get(merged.size()-1)[1] <interval[0]) {
                merged.add(interval); //Không chồng lấn -> Thêm mới
            } else {
                merged.get(merged.size() -1)[1] = Math.max(merged.get(merged.size()-1)[1], interval[1]);
            }
        }
        
        return merged;
    }
    public static void main(String[] args) {
        int[][] input = {{1,3},{2,6},{8,10},{15,18}};
        List<int[]> result = merge(input);

        for (int[] interval: result) {
            System.out.println(Arrays.toString(interval));
        }
    }
}
    

