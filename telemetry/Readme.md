key methods for PROFILING:

Framework Technical Features:

1. reflection - used for a) collect things to profile/measure and/or b) automatically (and transperantly for the end user) decorate with profiling capability 
    inside module
    inside class
2. decorators (for function and class)
    manual
    automatically injected (through reflection and injection)
3. snapshoting (and filtering out unesessary stuff)
4. standalone util functions for reuse as is and explictly - to measure individual var  

OS memory:
    measure the total OS process ram and % utilization
python heap memory:
    measure the mem increment of every line in code in function - note this measures smaller Pandas (equivalent to not Deep)
    snapshot measure all - periodically, and eventually filter some which are of specific interest, sort in descending order, and e.g. top 10
        - trace_malloc / pympler snapshots
        - get all local and global vars and measure them with other APIs
    - measure specific/named or registered (in a global registry) vars - pass the var to function to measure and log or decorate the functions during the 
    execution of whcih to measure the registered vars 
reference counts
    - absolute counts
    - circular relationships
visualization:
    visualization of mem utilization over time
    visualization of object graphs

key methods for INTEGRATION - Telemetry Integration Methods:

get all global vars/objects (and then filter on specific types) - same for class variables - reflection - then dedicated decorator to snapshot the vars
get all local vars/objects (and then filter on specific types) - same for class variables - reflection - then dedicated decorator to snapshot the vars
get all objects tracked by gc (and then filter on specific types)
register object for tracking explicitly - then the sizes are tracked by dedicated decorator 
decorate function (manual and automatic) - memory-profiler, pympler style snapshots

all decorators - all to have on/off functionality by config - the entire profiling functionality

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
            #pyrasite
            guppy3
    
poetry add <package-name>

poetry install

poetry python main.py