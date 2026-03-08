"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {e.id: e for e in employees}

        def dfs(emp_id):
            emp = employee_dict[emp_id]
            return emp.importance + sum(dfs(sub_id) for sub_id in emp.subordinates)

        return dfs(id)        