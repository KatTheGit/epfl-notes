# Algorithms

## Complexity

### Linear

n

## Algorithms

### Binary Search

Find an element in a sorted list.

- inspect middle
- continue in the half that may contain target
- repeat

Each iteration removes half the list.   

### Selection Sort

- Choose the smallest value, add it to the sorted list.

complexity: $\frac{n^2}{2}$

### Bubble Sort

### Insertion Sort

Insert element in correct position in new list

## Partitions

odd or distinct parts

odd: additions of odd numbers (n)

discinct: additions of distinct numbers (n-1)

# Growth of Functions (Complexity of Algorithms)

We mostly care about growth rather than exact values. Multiplicative constant ($f(n) = \alpha n$) is not so relevant


## Big-O Notation

$f(x)$ is $O(g(x))$ if there are constants $C$ and $k$ such that:

$|f(x)| \le C|g(x)|$, whenever $x>k$

$n! > 2^n > n^2 > n \log n > n > \log n > 1 \quad$ ("$>$" used as substitute for "$O()$")

### Theorems

$\R[x]_{\le n}$ complexity is $O(x^n)$

If $\displaystyle \lim_{x \to \infin} \frac{f(x)}{g(x)}$ is finite, then $f(x)$ is $O(g(x))$

## Big-Omega Notation

Opposite of Big-O.

$f(x)$ is $\Omega(g(x))$ if there are constants $C$ and $k$ such that:

$|f(x)| \ge C|g(x)|$, whenever $x>k$

## Big-Theta Notation

A function is $\Theta(g(x))$ if it is both $O(g(x))$ and $\Omega(G(x))$.

### Theorems

$\R[x]_{\le n}$ is $\Theta(x^n)$

## Little o

$f$ is $o(g(x))$ if $\displaystyle \lim_{x \to \infin} \frac{f(x)}{g(x)} = 0$