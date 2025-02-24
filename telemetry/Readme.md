Model Telemetry Development Plan:

1. Assess and select the best Telemetry packages and APIs - ref below the list of candidates included in this task. Only one option/candidate
will be selected and used in the actual solution
2. Implement injectable and configurable Telemetry framework, which incorporates the above
3. Integrate the new Telemetry in the currently implemented models
4. Test the currently implemented models with increasing dataset sizes to fit a Scalability and Memory Allocation Profiles/Curve/Function 
5. Time/quantify the impact of incorporating memory profiling (does have some impact) on the speed of the overall codebase 
6. Incorporate the Memory Allocation curve/function in automatic decision making algo to decide whether to triger production run of a Model based
on a) Input Dataset Size, b) Available RAM on the Model execution environment e.g. Kubernetes POD or cancel the run and raise alert proactively.
The same algorithm would also make and log prediction about the run time of the Model based on the size of the input dataset

List of Telemetry packages and APIs to assess and select from:

CPU/code speed/time Profiling:

    OS Process Space CPU Profiling:
        psutil

    App code speed/time in Python Interpreter/VM Profiling
        line-profiler
        cProfile
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
            tracemalloc
            objgraph
            stackimpact
            pyrasite
            guppy3
    
