## ADD CODE HERE!

def run_command_on_ARCC(job_directory, job_title, command, cpus = 1, 
memory=32, fail_notification=True, finish_notification=False, time=8, conda="Modeling",
nodes=1):
    filename = os.path.join(job_directory, job_title + ".sh")

    with open(filename, 'w') as f:
        f.write(f'#!/bin/bash\n')
        f.write('#SBATCH --account=galaxies\n')
        if fail_notification and finish_notification:
            f.write('#SBATCH --mail-type=FAIL,END\n')
        elif fail_notification:
            f.write('#SBATCH --mail-type=FAIL\n')
        elif finish_notification:
            f.write('#SBATCH --mail-type=END\n')
        f.write(f'''#SBATCH --mail-user=tjuchau@uwyo.edu
            
#SBATCH --job-name={job_title}
#SBATCH --output={job_title}.out
#SBATCH --error={job_title}.err
#SBATCH --time={time}:00:00
#SBATCH --mem={memory}G
#SBATCH --cpus-per-task={cpus}
#SBATCH --nodes={nodes}
''')

        f.write(f'''
source ~/.bashrc
conda activate {conda}
cd {job_directory}
{command}''')
    os.chdir(job_directory)
    os.system(f'sbatch {job_title}.sh')