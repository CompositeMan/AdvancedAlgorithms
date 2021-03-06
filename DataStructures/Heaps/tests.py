from fib_heap import FibHeap
from random import random, seed

seed(9)
def sortkey(v): return round(random()*100, 2)
def push_test():
        xs = list(range(15))
        f = FibHeap(xs, sort_key=sortkey)
        print(f)

        R = 3
        mins = [None]*R
        for _ in range(R):
                mins[_] = f.pop_min()
        print(f"Mins : {mins}")
        print(f)
        ps = list(range(100,103))
        for p in ps:
                f.push(p)

        print(f)

def pop_test():
        R = 5
        xs = list(range(R))
        f = FibHeap(xs, sort_key=sortkey)
        print(f)
        min = f.pop_min()
        print(f"Min : {min}")
        print(f)        

def sibling_test():
        R = 5
        xs = list(range(R))
        f = FibHeap(xs, sort_key=sortkey)

        print(f)

        min = f.pop_min()
        print(f"Min : {min}")
        
        print(f)
        
        i = 0
        for s in FibHeap._siblings(f.min_root.child):
                print(f" {i}th sibling : {f._nodestr(s)}")
                i += 1

def tests():
        push_test()
        pop_test()
        sibling_test()

if __name__ == "__main__":
        tests()