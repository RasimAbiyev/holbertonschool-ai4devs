public class Bug3 {
    public static double calculateAverage(int[] numbers) {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalArgumentException("Input cannot be empty");
        }

        int sum = 0;

        for (int number : numbers) {
            sum += number;
        }

        return (double) sum / numbers.length;
    }

    public static void main(String[] args) {
        int[] values = {10, 15, 21};
        System.out.println(calculateAverage(values));
    }
}
