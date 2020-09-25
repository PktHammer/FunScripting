import dslib

if __name__ == "__main__":

    vtest = [1] * 30
    addarr = [0] * 70
    vtest.extend(addarr)
    print(vtest)
    print(dslib.stat_typical.find_variance_defi_method(vtest))