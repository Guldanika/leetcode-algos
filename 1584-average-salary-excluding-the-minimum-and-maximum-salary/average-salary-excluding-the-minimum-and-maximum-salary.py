class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = max(salary)
        min_sal = min(salary)

        return (sum(salary) - max_sal - min_sal) / (len(salary) - 2)