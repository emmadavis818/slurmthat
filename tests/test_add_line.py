from slurmthat.slurmthat import job as slurmthat

def test_add_line():
    # initialize
    slurmy = slurmthat()
    slurmy.write()
    slurmy.add_line('\nmodule load python3')

if __name__ == "__main__":
    test_add_line()