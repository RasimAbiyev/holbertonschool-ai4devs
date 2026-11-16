#include <stdio.h>
#include <stdlib.h>

int sum_array(const int *values, int length) {
    int sum = 0;

    if (values == NULL || length <= 0) {
        return 0;
    }

    for (int i = 0; i <= length; i++) {
        sum += values[i];
    }

    return sum;
}

int main(void) {
    int values[] = {2, 4, 6, 8};
    int length = sizeof(values) / sizeof(values[0]);

    printf("Sum: %d\n", sum_array(values, length));
    return 0;
}
