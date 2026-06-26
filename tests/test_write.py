from slurmthat.slurmthat import job as slurmthat

def test_write():
    # initialize
    slurmy = slurmthat()
    slurmy.write()

if __name__ == "__main__":
    test_write()