import java.util.ArrayList;
import java.util.List;

public class spiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if(matrix == null || matrix.length  == 0) return result;

        int top = 0;
        int bottom = matrix.length - 1;
        int left = 0;
        int right = matrix[0].length -1;

        while(top <= bottom && left <= right) {
            // Đi sang phải
            for(int col = left; col <= right; col++) {
                result.add(matrix[top][col]);
            }
            top++;

            //Đi xuống
            for(int row = top; row <= bottom; row++) {
                result.add(matrix[row][right]);
            }
            right--;

            // Đi sang trái
            if(top <= bottom) {
                for(int col = right; col >= left; col--) {
                    result.add(matrix[bottom][col]);
                }
                bottom--;
            }

            // Đi lên
            if(left <= right) {
                for(int row = bottom; row >= top; row--) {
                    result.add(matrix[row][left]);
                }
                left++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        spiralMatrix sm = new spiralMatrix();
        int[][] matrix = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        };
        System.out.println(sm.spiralOrder(matrix));
    }
}