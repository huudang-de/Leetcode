import java.util.Arrays;

public class ProductExceptSelf {

    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;                        //Lấy độ dài mảng nums
        int[] output = new int[n];                  //Tạo mảng kết quả cùng độ dài

        //Tính tích bên trái
        output[0] = 1;                              //Phần tử đầu tiên không có phần tử bên trái -> gán 1
        for (int i = 1; i < n; i++) {
            output[i] = output[i - 1] * nums[i - 1];
            // output[i] = tích tất cả phần tử bên trái nums[i]
        }

        //Tính tích bên phải và nhân trực tiếp vào output
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] = output[i] * right;          //Nhân tích bên phải vào giá trị đã lưu từ bước 1
            right *= nums[i];
        }

        return output;
    }
    


    // Hàm để kiểm tra:
    public static void main(String[] args) {

        ProductExceptSelf sol = new ProductExceptSelf();

        int[] nums1 = {1, 2, 3, 4};
        System.out.println("Input: " + Arrays.toString(nums1));
        System.out.println("Output: " + Arrays.toString(sol.productExceptSelf(nums1))); 
        // [24, 12, 8, 6]
        
        int[] nums2 = {-1, 1, 0, -3, 3};
        System.out.println("\nInput: " + Arrays.toString(nums2));
        System.out.println("Output: " + Arrays.toString(sol.productExceptSelf(nums2))); 
            // [0, 0, 9, 0, 0]
    }
}