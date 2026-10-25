/* Sub-chunk 1.3: five tiny functions. Compile to assembly, then annotate every line.
 * Build:  make asm      (writes build/O0.s and build/O2.s)
 */
#include <stdint.h>

int sum_loop(const int *a, int n) {
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}

void array_copy(uint32_t *dst, const uint32_t *src, int n) {
    for (int i = 0; i < n; i++) dst[i] = src[i];
}

struct point { int8_t tag; int32_t x; int32_t y; };
int32_t struct_access(const struct point *p) { return p->x + p->y; }

int pick(int a, int b) {
    if (a > b) return a - b;
    else       return b - a;
}

int apply(int (*f)(int, int), int a, int b) { return f(a, b); }
