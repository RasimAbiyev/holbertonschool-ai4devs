#include <stdio.h>

int calculate_sum(int numbers[], int size) {
    int sum = 0;

    for (int i = 0; i <= size; i++) {
        sum += numbers[i];
    }

    return sum;
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    int result = calculate_sum(numbers, size);

    printf("Sum: %d\n", result);

    return 0;
}
