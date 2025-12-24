class Cache:
    _MAX_CAPACITY = 0
    
    """
    Static method to get the maximum capacity of the cache
    """
    #Lazy initialization during the first invocation of the static method
    @staticmethod
    def get_max_capacity():
        if Cache._MAX_CAPACITY==0:
            val=int(input("Enter the max capacity of this cache:"))
            Cache._MAX_CAPACITY=val
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
