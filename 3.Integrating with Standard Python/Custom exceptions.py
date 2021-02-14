# Define SalaryError inherited from ValueError
class SalaryError(ValueError):
    pass
# Define BonusError inherited from SalaryError
class BonusError(SalaryError):
    pass
    
    
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_RAISE = 5000

  def __init__(self, name, salary = 30000):
    self.name = name
    
    # If salary is too low
    if salary < MIN_SALARY:
      # Raise a SalaryError exception
      raise SalaryError("Salary is too low!")
    
    self.salary = salary
    
    
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
       print("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
       print("The salary after bonus is too low!")
      
    else:  
      self.salary += amount
