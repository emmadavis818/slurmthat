from slurmthat import job as j

def test_add_line():
    # initialize
    slurmy = j()
    slurmy.write()
    slurmy.add_line('\nmodule load python3')

if __name__ == "__main__":
    test_add_line()