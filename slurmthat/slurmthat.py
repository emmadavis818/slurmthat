import os

class job:
    '''Job
      
    Class for creating a job submission script for SLURM.     

      Attributes:
          HPC (str): String. Name of the HPC system.
          email (str): String. Email address for job notifications.
          dir (str): String. Directory for the job script.
          job (str): String. Name of the job.
          partition (str): String. Partition for the job.
          account (str): String. Account for the job.
          shfilename (str): String. Name of the shell script file.
          nodes(int): Integer. Number of nodes requested for the job. Default is 1.
          memory(int): Integer. Amount of memory (in GB) requested for the job. Default is 48 GB.
      
      '''

    def __init__(self, HPC=None, email=None, dir=None, job=None, partition=None,
                 account=None,shfilename=None):
        self.HPC = HPC
        self.account = account
        self.email = email
        self.dir = dir
        self.job = job
        if self.job is None:
          self.job = 'my_job_%j'
        self.partition = partition
        if self.dir is None:
          self.dir = os.getcwd()
        if shfilename is None:
          shfilename = 'my_script'
        self.shfilename = shfilename
        self.filename = os.path.join(self.dir, self.shfilename + ".sh")

    def write(self, fail=False, start=False, finish=False, out_file=None, 
              err_file=None, time=32, cpus=10, nodes=1, memory=48, conda=None):
      '''Write
      
      Write a .sh file for slurm submission.
        
      Args:
          fail(bool): Boolean. If True, sends email on job failure.
          start(bool): Boolean. If True, sends email when job starts.
          finish(bool): Boolean. If True, sends email when job finishes.
          out_file(str): String. Name of the output file. 
          err_file(str): String. Name of the error file. 
          time(int): Integer. Time (in hours) requested for the job. Default is 32 hours.
          cpus(int): Integer. Number of CPUs requested for the job. Default is 10.
          nodes(int): Integer. Number of nodes requested for the job. Default is 1.
          memory(int): Integer. Amount of memory (in GB) requested for the job. Default is 48 GB.
      
      Returns:
          str: The name of the .sh file written.
      '''

      with open(self.filename, 'w') as f:
          f.write('#!/bin/bash\n')
          if self.account is not None:
            f.write(f'#SBATCH --account={self.account}\n')
          if self.email is not None:
            f.write(f'#SBATCH --mail-user={self.email}\n')
          f.write(f'#SBATCH --job-name={self.job}\n')
          if self.partition is not None:
            f.write(f'#SBATCH -p {self.partition}\n')

          if fail and finish and start:
            f.write('#SBATCH --mail-type=FAIL,END,BEGIN\n')
          elif fail and start:
            f.write('#SBATCH --mail-type=FAIL,BEGIN\n')
          elif fail and finish:
            f.write('#SBATCH --mail-type=FAIL,END\n')
          elif start and finish:
            f.write('#SBATCH --mail-type=BEGIN,END\n')
          elif fail:
            f.write('#SBATCH --mail-type=FAIL\n')
          elif start:
            f.write('#SBATCH --mail-type=BEGIN\n')
          elif finish:
            f.write('#SBATCH --mail-type=END\n')
          if out_file is None:
            out_file = f"{self.filename.split('.sh')[0]}.out"
          f.write(f'#SBATCH --output={out_file}\n')
          if err_file is None:
            err_file = f"{self.filename.split('.sh')[0]}.err"
          f.write(f'#SBATCH --error={err_file}\n')
          f.write(f'''#SBATCH --time={time}:00:00
#SBATCH --mem={memory}G
#SBATCH --cpus-per-task={cpus}
#SBATCH --nodes={nodes}\n''')
          if conda is not None:
            f.write('source ~/.bashrc\nconda activate Modeling\n')
          print(f'wrote .sh file to {self.filename}')
          return self.filename
    def add_line(self, line):
      '''Add line

      Add a line to the .sh file.

      Args:
          line(str): String. Line to add to the .sh file.

      Returns:
          None
      '''
      with open(self.filename, 'a') as f:
          f.write(f'{line}\n')



    def run(self):
      '''Run

      Run the job submission script using sbatch.

      Args:
          None
      Returns:
          None
      '''
      os.system(f'sbatch {self.filename}')
