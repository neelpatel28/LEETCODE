class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        
        curr_mass = mass  # local variable
        
        for a in asteroids:
            if curr_mass < a:
                return False
            curr_mass += a
        
        return True