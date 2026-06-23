# slurmthat
#TJ in development

Group 21, CodeAstro 2026

This package creates and submits an sbatch .sh file on a user-inputed computer/computing system. 

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
