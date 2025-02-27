HOW TO THINK AND GO ABOUT PROGRAM DESIGN, DEVELOPMENT AND TESTING AND THE OVERALL PROJECT ENVIRONMENT AROUND THAT 

use this during: 
a) New Software System Design and Development and 
b) as a Structured Checklist what areas to look for and reverse engineer from existing solution
to Map Out how it was designed and developed
c) as Plan for ongoing training

---------------------------------------------------------------------------------------------------------------------

The Data in the Program/System / Data Structures, Define and Organizw/Structure the Data in thge Program /  the Data the Program operates upon:

    Scalar:

        Numeric:
            int
            float
            complex number
        string
        date
    
    Data Structures:

        Sequence/Range
        Tuple
        Enumeration
        Data Class
        List (also a surogate Array)
        Dictionary (HashMap)
        Set
        Queue (several implementations, including List)
        Stack (same as above)
        Class
        Array (Numpy)
        DataFrame (Pandas), this is essentially a RDBMS Table abstraction
        TimeSeries (Pandas and several more)

        Nested Variants of all of the above

        Functional (Data Access and Manipulation) Basic Primitives for each of the above (the basic/first order/primordial algos for the basic/primordial data structures)

Algorithms:

    Operate on the above Data - Scalar and Data Structure 

Program/System Organization / Architecture / Modular Structure:

    Data - Data Models, Data Flows, Data Access Patterns:
    System - System Modules/Components:
        Internal:
            Algorithms and Data / Data Structures
            Functions
            Classes (and class hierarchies)
            Modules
            Packages
        External/Remotable:
            IPC
            Services
            Message Brokers / ESB - Message Transfer
            File / Batch Data Transfer
    Functional Responsibilities of Modules/Components - allocate/design
    Intefaces between Modules/Components and Interactions between modules (flow of control and data)
    System Context - Externally Facing System Interfaces and the Execution Env/Platform for the Program
    End User Interface

    Name Sapces, Variable Scope and Module Loading Order in Python

Error Handling / Reliability Design:

    Error conditions/logic, error codes, exceptions
    Program Input/Output and Input/Output Validation
    Logging

Python Bytecode and Virtual Machine:

    Internals
    Stnadrd Lib Debuging, Profiling and Garbage COllection control
    Reflection

Parallel Programming:

    MultiThreding
    MultiProcessing
    AsyncIO

    the overall framewrk apis for each of teh above, including semaphors, locks etc
    
Decorators:

    Useful for Plugins for Framework Extensions

Useful Standard/Built-In Functions:

    sorted
    len
    filter
    type
    etc

Other Language Features:

    OOP in Python - overiding operators (+, =, etc), abstract, etc
    Yeild, Generators
    With / Context Management
    List/Dict Comprehension
    Exceptions
    Logging
    Program Input Param parsing and validation
    Runtime instrumentation
    Json and Request
    FileIO
    NetworkIO
    Reflection, runtime code instantiation and interogation
    
    Math Operations, Equations and Algos - Math and Qunat Operators and Libs 

Ecosystem of useful third-party Frameworks/Platforms/Libs:

    PySpark
    FastAPI
    Pandas
    Numpy
    Data Visualization
    ML - Keras, Pytorch, SciPy etc
    etc

Project Related:

    Testing - Manual Tetsing with Debugger and Logging, Automated Unit Testing (Python SPecific), System Integration Testing, Code Coverage (%)
    Lint - coding style standards
    Environments (Dev, UAT, Prod) and Deployment to different environments
    Instrumentation and Ongoing Monitoring
    Python virtual env manageemnt, pip, requirements.txt gen etc
    Packaging, Distribution of system components/libs, package repos - internal external
    Testing - Funcional, Scalability, Reliability
    Dev Workflow - code repositories, PRs, repo branching structure etc, CD/CI Pipelines - their organization and structure and how to participate in them
    Project Management and Documentation - Confluence, JIRas, Backlogs, etc

Business:

https://www.google.com/search?q=python+portfolio+var+historical+scenarios&oq=python+portfolio+var+historical+scenarios&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRiPAtIBCjQwMDQwajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8
https://campus.datacamp.com/courses/introduction-to-portfolio-risk-management-in-python/value-at-risk?ex=3
https://www.linkedin.com/pulse/copy-option-greeks-hemant-thapa-dn8fe/
https://github.com/omartinsky/QuantAndFinancial/blob/master/yield_curve_bootstrapping/bootstrapping.ipynb
https://www.youtube.com/watch?v=g-efwWZZBvA
https://www.youtube.com/watch?v=QsccAA3k_1o
https://python.plainenglish.io/feature-engineering-for-time-series-forecasting-in-python-7c469f69e260

https://medium.com/@matt_84072/historical-simulation-value-at-risk-explained-with-python-code-a904d848d146

https://www.interactivebrokers.eu/campus/trading-course/ibkrs-risk-navigator/
