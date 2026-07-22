# DSA Notes – GCD (Greatest Common Divisor)

## Problem

Given two integers `n1` and `n2`, find their Greatest Common Divisor (GCD).

**Example:**

* Input: `9, 12`
* Output: `3`

---

# 1. My First Idea (Brute Force)

### Thought Process

* Find all factors of `n1`.
* Find all factors of `n2`.
* Compare both collections to find the common factors.
* Return the largest common factor.

### Code Idea

* Store factors in two lists.
* Initially tried comparing both lists element by element.
* Realized this approach wasn't reliable because common factors don't necessarily appear at the same indices.

Example:

```
12 -> [1, 2, 3, 4, 6, 12]
18 -> [1, 2, 3, 6, 9, 18]
```

Comparing indices is not a general solution.

---

# 2. Second Idea

### Insight

Instead of manually comparing lists, convert them into sets.

```
set1.intersection(set2)
```

This gives all common factors directly.

Then return the maximum element.

**Important Mistake**

Do **not** use:

```python
intersection.pop()
```

because sets are unordered.

Correct approach:

```python
max(intersection)
```

---

# 3. Better Brute Force

### New Insight

I originally tried finding the smaller list (`cmp_arr`) to reduce comparisons.

The better realization is:

> Every common divisor must be less than or equal to the smaller number.

Therefore, there is no need to generate factor lists.

```python
gcd = 1

for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
```

Space complexity becomes **O(1)**.

---

# 4. Optimal Solution — Euclid's Algorithm

### Key Property

```
GCD(a, b) = GCD(b, a % b)
```

Keep replacing the pair until the second number becomes 0.

Example:

```
GCD(12, 9)

12 % 9 = 3

GCD(9, 3)

9 % 3 = 0

GCD(3, 0)

Answer = 3
```

Python:

```python
while n2 != 0:
    n1, n2 = n2, n1 % n2

print(n1)
```

---

# Why Euclid's Algorithm Works

If

```
20 = 15 × 1 + 5
```

Any number that divides both **20** and **15** must also divide

```
20 - (15 × 1) = 5
```

So

```
GCD(20,15)
=
GCD(15,5)
```

The GCD never changes—only the numbers become smaller.

---

# Complexity

| Approach              | Time               | Space      |
| --------------------- | ------------------ | ---------- |
| Factor Lists          | O(n1 + n2)         | O(n1 + n2) |
| Check till min(n1,n2) | O(min(n1,n2))      | O(1)       |
| Euclid's Algorithm    | O(log(min(n1,n2))) | O(1)       |

---

# What I Learned

* Don't create extra data structures unless necessary.
* Before coding, ask: **Can this problem be solved using a property instead of storing information?**
* Lists → Sets → Mathematical observation → Optimal algorithm.
* Optimizing the search space is often better than optimizing comparisons.
* A working brute-force solution is a good first step; then improve it step by step.

---

# Personal Thought Process (Today's Session)

1. Generated factors of both numbers.
2. Tried comparing both lists using indices.
3. Realized that approach was incorrect.
4. Remembered `set.intersection()` and solved the problem.
5. Learned a better brute-force solution using `min(n1, n2)`.
6. Finally understood Euclid's Algorithm and why it works.

**Lesson:** Getting stuck isn't failure. Each failed idea helped reveal a better one.
