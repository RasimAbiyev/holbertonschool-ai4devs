#include <stdio.h>

int calculate_sum(int numbers[], int size) {
    int sum = 0;

    for (int i = 0; i < size; i++) {
        sum += numbers[i];
    }

    return sum;
}

int main(void) {
    int numbers[] = {10, 20, 30, 40, 50};
    int one[] = {7};
    int empty[] = {0};

    if (calculate_sum(numbers, 5) != 150 ||
        calculate_sum(one, 1) != 7 ||
        calculate_sum(empty, 0) != 0) {
        printf("Bug 4 tests failed\n");
        return 1;
    }

    printf("All Bug 4 tests passed.\n");
    printf("Sum: %d\n", calculate_sum(numbers, 5));

    return 0;
}
