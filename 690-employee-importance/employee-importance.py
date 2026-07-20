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

        emp_map = {emp.id: emp for emp in employees}
        
        def dfs(emp_id):
            employee = emp_map[emp_id]
            total_importance = employee.importance
            
            for sub_id in employee.subordinates:
                total_importance += dfs(sub_id)
                
            return total_importance
        
        
        return dfs(id)