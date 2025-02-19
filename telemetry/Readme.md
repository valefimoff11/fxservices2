Assess and select the best packages
Implement injectable and configurable Telemetry framework, which incorporates the above
Integrate the new Telemetry in the currently implemented models
Test the currently implemented models with increasing dataset sizes to fit a Scalability and Memory Allocation Profiles 

CPU/code speed/time Profiling:

    OS Process Space CPU Profiling:
        psutil

    App code speed/time in Python Interpreter/VM Profiling
        line-profiler
        cpython profiler 
        sys.timeit etc - profiling

Data Profiling

    Persistent Data Profiling
        Measure the size of the input datasets

    Memory Profiling:
        
        OS Process Space Memory Profiling:
            psutil

        Python Interpreter/VM Memory Heap Profiling
            pympler
            memory-profiler (not supported anymore)
            tracemalloc, gc, gc.getobject
            objgraph
            stackimpact
            pyrasite
    
