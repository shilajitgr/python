class Solution():
    
    def greet(self, names):
        greeting = "Hello"
        print(f" id of greeting in greet: {id(greeting)}")
        def greet_helper(name):
            greeting = "Hi" # updating "free variable" stores the data in a new memory location
            # without updating the variable in the outer scope
            print(f" id of greeting in greet_helper: {id(greeting)}")
            print(f"{greeting} {name}")
            print(f"{locals().get('greeting')}")

        for name in names:
            greet_helper(name)
        
        greeting = "Hey"
        print(f" id of greeting in greet: {id(greeting)}")
    
sol_obj = Solution()
print(Solution().greet(["john"]))

