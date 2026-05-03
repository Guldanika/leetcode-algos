<h2><a href="https://leetcode.com/problems/maximize-distance-to-closest-person">Maximize Distance to Closest Person</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given an array representing a row of <code>seats</code> where <code>seats[i] = 1</code> represents a person sitting in the <code>i<sup>th</sup></code> seat, and <code>seats[i] = 0</code> represents that the <code>i<sup>th</sup></code> seat is empty <strong>(0-indexed)</strong>.</p>

<p>There is at least one empty seat, and at least one person sitting.</p>

<p>Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.&nbsp;</p>

<p>Return <em>that maximum distance to the closest person</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/distance.jpg" style="width: 650px; height: 257px;" />
<pre>
<strong>Input:</strong> seats = [1,0,0,0,1,0,1]
<strong>Output:</strong> 2
<strong>Explanation: </strong>
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> seats = [1,0,0,0]
<strong>Output:</strong> 3
<strong>Explanation: </strong>
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> seats = [0,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= seats.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>seats[i]</code>&nbsp;is <code>0</code> or&nbsp;<code>1</code>.</li>
	<li>At least one seat is <strong>empty</strong>.</li>
	<li>At least one seat is <strong>occupied</strong>.</li>
</ul>



Follow-up: вернуть индекс максимально удалённого места

Если нужно вернуть не только максимальную дистанцию, но и индекс посадочного места, можно использовать ту же декомпозицию на три подзадачи. В каждой подзадаче будем формировать кортеж (дистанция, индекс), а в финале — выбирать максимум по этим кортежам. Python сравнивает кортежи лексикографически: сначала по дистанции, и индекс «приедет» вместе с лучшим кандидатом.

Идея по индексам





Подзадача 1 (слева): дистанция = left, индекс = 0 — садимся в самый левый край.





Подзадача 2 (справа): дистанция = right, индекс = n - 1 — садимся в самый правый край.


```
from typing import List, Tuple

class Solution:

    def maxDistToClosestWithIndex(self, seats: List[int]) -> Tuple[int, int]:

        n = len(seats)

        # Подзадача 1: посадка слева

        left = 0

        while seats[left] == 0:

            left += 1

        left_result = (left, 0)

        # Подзадача 2: посадка справа

        right = 0

        right_ind = n - 1

        while seats[right_ind] == 0:

            right += 1

            right_ind -= 1

        right_result = (right, n - 1)

        # Подзадача 3: посадка посередине

        mid = 0

        mid_max = 0

        mid_end = -1  # правый индекс лучшей серии нулей

        for i in range(left, right_ind + 1):

            if seats[i] == 0:

                mid += 1

                if mid > mid_max:

                    mid_max = mid

                    mid_end = i

            else:

                mid = 0

        mid_dist = (mid_max + 1) // 2

        mid_index = mid_end - mid_max + mid_dist if mid_max > 0 else -1

        mid_result = (mid_dist, mid_index)

        # max по кортежам сравнит сначала дистанции и вернёт индекс вместе с ней

        return max(left_result, right_result, mid_result)//
```





Подзадача 3 (середина): при проходе запоминаем правую границу самой длинной серии нулей mid_end. Левая граница серии = mid_end - mid_max + 1. Дистанция = (mid_max + 1) // 2. Индекс посадки = mid_end - mid_max + mid_dist (это эквивалентно «левый край серии + (mid_max - 1) // 2»).
