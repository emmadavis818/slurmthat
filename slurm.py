import os

class job:

    def __init__(self, HPC=None, email=None, dir=None, job=None, partition=None,
                 account=None):
        self.HPC = HPC
        self.account = account
        self.email = email
        self.dir = dir
        self.job = job
        self.partition = partition
        if self.dir is None:
          self.dir = os.getcwd()
        if self.job is None:
          self.job = 'my_job'
        self.filename = os.path.join(self.dir, self.job + ".sh")

    def write(self, fail=False, start=False, finish=False, out_file=None, 
              err_file=None, time=32, cpus=10, nodes=1, memory=48):
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
      sh_filename = self.filename

      with open(sh_filename, 'w') as f:
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
            out_file = f"{sh_filename.split('.sh')[0]}.out"
          f.write(f'#SBATCH --output={out_file}\n')
          if err_file is None:
            err_file = f"{sh_filename.split('.sh')[0]}.err"
          f.write(f'#SBATCH --error={err_file}\n')
          f.write(f'''#SBATCH --time={time}:00:00
#SBATCH --mem={memory}G
#SBATCH --cpus-per-task={cpus}
#SBATCH --nodes={nodes}\n
''')
          print(f'wrote .sh file to {sh_filename}')
          return sh_filename
    def add_line(self, line):
      with open(self.filename, 'a') as f:
          f.write(f'{line}\n')



    def run(self, conda=None):
      if conda is not None:
        with open(self.filename, 'a') as f:
          f.write('source ~/.bashrc\n')
          f.write(f'conda activate {conda}\n')
      os.system(f'sbatch {self.filename}')
