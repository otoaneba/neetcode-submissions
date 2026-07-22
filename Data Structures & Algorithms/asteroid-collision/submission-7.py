class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        make a stack
        for each asteroids
            if the length of stack is bigger than 1
                check the last two asteroids
                right = stack[-1]
                left = stack[-2]
                if right < 0 and left > 0 
                    will collide
                    pop the smaller one
            else
                insert into stack
             
        return stack as list
        """
        stack = []
        for asteroid in asteroids:
            alive = True
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroid):
                    # right one is bigger. pop first, then append asteroid
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    # they are the same. both destroyed
                    stack.pop()
                    alive = False
                    break
                else: 
                    # right one is smaller. Set alive to False
                    alive = False
                    break
                    
            if alive:       
                stack.append(asteroid)
        return stack