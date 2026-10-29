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


## big O Notation

$f(x)$ is $O(g(x))$ if there are constants $C$ and $k$ such that:

$|f(x)| \le C|g(x)|$, whenever $x>k$

Basically g(x) dominates f(x) above x = k.

 $\R[x]_{\le n}$ complexity is $O(x^n)$