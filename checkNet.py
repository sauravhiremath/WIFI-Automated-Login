import subprocess, platform


def pingOk(sHost):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)

    except Exception or e:
        return False

    return True

pingchk = pingOk('www.google.com')
print(pingchk)
