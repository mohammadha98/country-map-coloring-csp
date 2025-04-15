class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):

        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.assignment = {}  # تخصیص فعلی
        self.backtrack_count = 0  # شمارنده تعداد بازگشت‌ها
        self.assignment_count = 0  # شمارنده تعداد تخصیص‌ها
        self.failure_count = 0  # شمارنده تعداد شکست‌ها
    
    def solve(self):
        
   

        if not self.ac3():
            return None
        
 
        result = self.backtrack({})
        return result
    
    def backtrack(self, assignment):
  
        

   
        if len(assignment) == len(self.variables):
            return assignment
        
        var = self.select_unassigned_variable(assignment)
        

        self.backtrack_count += 1
        

        for value in self.order_domain_values(var, assignment):

            self.assignment_count += 1
            

            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                
          
                saved_domains = {v: self.domains[v].copy() for v in self.variables}
                
   
                if self.forward_check(var, assignment):
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
                
             
                self.domains = saved_domains
                
      
                del assignment[var]
                
         
                self.failure_count += 1
        
        return None
    
    def select_unassigned_variable(self, assignment):
     

        unassigned = [v for v in self.variables if v not in assignment]
        
    
        mrv_vars = sorted(unassigned, key=lambda var: len(self.domains[var]))
        min_remaining = len(self.domains[mrv_vars[0]])
        mrv_candidates = [var for var in mrv_vars if len(self.domains[var]) == min_remaining]
        
        if len(mrv_candidates) == 1:
            return mrv_candidates[0]
        
   
        return max(mrv_candidates, key=lambda var: sum(neighbor not in assignment for neighbor in self.neighbors[var]))
    
    def order_domain_values(self, var, assignment):
    
        return self.domains[var]
    
    def is_consistent(self, var, value, assignment):
      
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True
    
    def forward_check(self, var, assignment):
    
        value = assignment[var]
        
     
        for neighbor in self.neighbors[var]:
            if neighbor not in assignment:
             
                if value in self.domains[neighbor]:
                    self.domains[neighbor].remove(value)
                
             
                if not self.domains[neighbor]:
                    return False
        
        return True
    
    def ac3(self):
      
        queue = [(xi, xj) for xi in self.variables for xj in self.neighbors[xi]]
        
     
        while queue:
            xi, xj = queue.pop(0)
            
         
            if self.revise(xi, xj):
              
                if not self.domains[xi]:
                    return False
                
            
                for xk in self.neighbors[xi]:
                    if xk != xj:
                        queue.append((xk, xi))
        
        return True
    
    def revise(self, xi, xj):
      
        revised = False
        
      
        for x in list(self.domains[xi]):
         
            if all(not self.constraint_satisfied(xi, x, xj, y) for y in self.domains[xj]):
                self.domains[xi].remove(x)
                revised = True
        
        return revised
    
    def constraint_satisfied(self, xi, x, xj, y):
      
        return x != y
    
    def get_statistics(self):
      
        return {
            'backtrack_count': self.backtrack_count,
            'assignment_count': self.assignment_count,
            'failure_count': self.failure_count
        }
