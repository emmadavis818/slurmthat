#1 --- "Shebang":
- Subdirective / Command: #!/bin/bash
- What it Does: Used to tell the cluster system to use the bash interpreter at the path /bin/bash on the system.
- Corresponding Line #(s): 1
- Ex of Output & How it’s Provided: n/a



#2 --- "Sbatch":
- Subdirective / Command: (---)
- What it Does: Request your resources with SBATCH directives.  SBATCH directives are always preceded with a # sign and should be in uppercase format.  

These directives provide SLURM with information and specifics about your job including the hardware you require, how long you need access to the hardware, where job output is written, and how to alert the user of job status.
- Corresponding Line #(s): 3-12
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command: #SBATCH --account=arcc
- What it Does: Tells the system which account/project you’re running your job under.  In the example, the job is run associated with the arcc project.   If arcc were not a valid project or account, or the submitter isn’t a member of the project/account, the job will not run.  Account is a mandatory directive that must be included within your submission script.  Jobs that don’t specify a time or a qos won’t run. 
- Corresponding Line #(s): 3
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command: #SBATCH --qos=debug
- What it Does: Tells SLURM to submit the job to the debug qos/queue. 
- Corresponding Line #(s): 4
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command: #SBATCH --time=0-00:10:00
- What it Does: The example requests a job with a time limit of 0 days - 00 hours : 10 minutes : 00 seconds.
- Corresponding Line #(s): 5
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command: #SBATCH --nodes=1
- What it Does: Tells SLURM the entire job will run on a single node on the cluster
- Corresponding Line #(s): 6
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command: #SBATCH --ntasks=24
- What it Does: Tells SLURM that we will be running our job across 24 tasks at a time
- Corresponding Line #(s): 7
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  #SBATCH --cpus-per-task=4
- What it Does: Tells SLURM we will need 4 CPUs to running each task
- Corresponding Line #(s): 8
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  #SBATCH --mem-per-cpu 2G
- What it Does: Tells SLURM that each task running on 4 CPUs will also be allocated 2GB of RAM
- Corresponding Line #(s): 9
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  #SBATCH --mail-user=cowboyjoe@uwyo.edu
- What it Does: Tells SLURM to e-mail the specified user (cowboyjoe@uwyo.edu) for all events specified under --mail-type directive.
- Corresponding Line #(s): 10
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  #SBATCH --mail-type=BEGIN,END,FAIL
- What it Does: Tells SLURM to e-mail the above e-mail address during the following events: job start (BEGIN), job finish (END) and job failure/error (FAIL).
- Corresponding Line #(s): 11
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  #SBATCH --get-user-env
- What it Does: Tells SLURM to get the login environment variables.  Users should be aware that any environment variables already set by #SBATCH will take precedent over the local user’s login environment.  Users should clear environment variables before calling #SBATCH directives if they are not to be applied to the spawned program.
- Corresponding Line #(s): 12
- Ex of Output & How it’s Provided: (---)



#3 --- "Open MP":
- Subdirective / Command:  (---)
- What it Does: Specifies threads and how they’re set up/distributed using OpenMP Framework
- Corresponding Line #(s): 14-16
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  export OMP_PROC_BIND=true
- What it Does: Specifies the number of OMP threads for the job (Value should equal --ntasks * --cpus-per-task specified above in SBATCH directives.  Ex:  24 * 4 = 96).  
Note: The total number of threads here should be less than or equal to the maximum number of cores on any single nodes if you’ve specified specific node(s) in your SBATCH directives (example: #SBATCH --partition=<partition_name>, or #SBATCH --qos=<qos_name>)
export OMP_NUM_THREADS=96
- Corresponding Line #(s): 14
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  export OMP_PLACES=threads; export OMP_DISPLAY_ENV=true; export; OMP_DISPLAY_AFFINITY=true; export OMP_AFFINITY_FORMAT="Thread Affinity %0.3L %.8n %.15{thread_affinity}%.12H"; export OMP_PROC_BIND=true
- What it Does: Enables thread binding using OpenMP and prints out information about thread affinity to the start of the job output file.
- Corresponding Line #(s): 15
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  export OMP_NUM_THREADS=32
- What it Does: Bind each thread to a core/cpu (export OMP_PLACES=cores)
- Corresponding Line #(s): 16
- Ex of Output & How it’s Provided: (---)



#4 --- Module(s):
- Subdirective / Command:  (---)
- What it Does: Load any required software
- Corresponding Line #(s): 18-19
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  module load miniconda3
- What it Does: Load miniconda3 software to use during the course of the job
- Corresponding Line #(s): 18
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  module load gcc/14.2.0
- What it Does: Load gcc compiler to use during the course of the job, specifically version 14.2.0
- Corresponding Line #(s): 19
- Ex of Output & How it’s Provided: (---)
 
#5) --- Slurm Run:
- Subdirective / Command:  (---)
- What it Does: Executes whatever follows srun now.  Don’t do other commands until this finishes.  (By default, next processes are blocked).
- Corresponding Line #(s): (---)
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  srun echo "Start Job Process"
- What it Does: Print “Start Job Process” to the terminal. 
- Corresponding Line #(s): (---)
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  srun hostname
- What it Does: Print the hostname of the node we’re running on to the terminal. Don’t do next commands until this finishes.
- Corresponding Line #(s): (---)
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  srun sleep 30
- What it Does: Stop executing things for 30. Don’t do next commands until this finishes.
- Corresponding Line #(s): (---)
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  srun --cpu-bind=cores check-hybrid.gnu.pm
- What it Does: The executable check-hybrid.gnu.pm performed is to be bound to the allotted cores, .Don’t do next commands until this finishes.
- Corresponding Line #(s): (---)
- Ex of Output & How it’s Provided: (---)

- Subdirective / Command:  srun echo "End Job Process"
- What it Does: Print “End Job Process” to the terminal. Don’t do next commands until this finishes.
- Corresponding Line #(s): (---)
- Ex of Output & How it’s Provided: (---)