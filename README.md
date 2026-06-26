# slurmthat
#TJ in development

Group 21, CodeAstro 2026

This package creates and submits an sbatch .sh file on a user-inputed computer/computing system. 

In general, the following workflow is recommended:

Bash:

  > pip install slurmthat
  
Python:

  > from slurmthat.slurmthat import job as j

  > job = j(account='<your_HPC_account>', email = '<your_email>', job='<your_job_name>', shfilename='</path/to/job>') #will add the .sh automatically
  
  > job.write(fail=True, start=True, finish=True, out_file='</path/to/job.out>',
  > err_file='</path/to/job.err>', conda='<your_conda_environment>') #all of these arguments are optional, defaults can be shown by running job.write?
  
  > job.add_line("echo 'hello world!'")
  
  > job.add_line("python your.py")
  
  > job.run()


#Example of a bash script to launch a job

#!/bin/bash

#SBATCH --account=arcc

#SBATCH --qos=debug

#SBATCH --time=0-00:10:00

#SBATCH --nodes=1

#SBATCH --ntasks=24

#SBATCH --cpus-per-task=4

#SBATCH --mem-per-cpu=2G

#SBATCH --mail-user=cowboyjoe@uwyo.edu

#SBATCH --mail-type=BEGIN,END,FAIL

#SBATCH --get-user-env

export OMP_PROC_BIND=true

export OMP_PLACES=threads

export OMP_NUM_THREADS=32

module load miniconda3 

module load gcc/14.2.0

srun echo "Start Job Process"

srun hostname

srun sleep 30
srun --cpu-bind=cores check-hybrid.gnu.pm
srun echo "End Job Process"
