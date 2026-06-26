from slurmthat import job as j
def test_write():
    # initialize
    slurmy = j()
    slurmy.write()

if __name__ == "__main__":
    test_write()