class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        
        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
        
        return True