Model Telemetry Development Plan:

1. Assess and select the best Telemetry packages and APIs
2. Implement injectable and configurable Telemetry framework, which incorporates the above
3. Integrate the new Telemetry in the currently implemented models
4. Test the currently implemented models with increasing dataset sizes to fit a Scalability and Memory Allocation Profiles 
5. Incorporate the curve/function in automatic decision making algo to decide whether to triger production run of a Model based
on a) Input Dataset Size, b) Available RAM on the Model execution environment e.g. Kubernetes POD or cancel the run and raise alert proactively 

Telemetry packages and APIs to assess and select from:

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
    
