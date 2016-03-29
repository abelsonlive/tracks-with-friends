import os
import sys
import shlex
import json
import tempfile
import subprocess
from traceback import format_exc


def run_cmd(*args, **kwargs):
    """
    run a command string / list args.
    optionally parse json output
    """
    kwargs.setdefault('shell', False)
    kwargs.setdefault('json', False)

    # parse command string / args
    args = list(args)
    str_cmd = " ".join(args)
    if len(args) == 1:
        if not kwargs['shell']:
            args = shlex.split(str_cmd)
        else:
            args = str_cmd

    # execute
    try:
        p = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=kwargs['shell']
        )

        out, err =  p.communicate()

    # catch subprocess errors
    except (OSError, subprocess.CalledProcessError) as exception:
        msg = "Error occured running:\n$ %s \n%s"  % (str_cmd, format_exc())
        raise Exception(msg)

    # catch system errors
    if p.returncode != 0:
        msg = "Exception occured running:\n$ " + str_cmd
        if err:
            print(msg)
            print('Std. Error:') 
            print(err)
        if out:
            print(msg)
            print('Std. Out:') 
            print(out)
        raise Exception(msg)

    # parse json
    if kwargs['json']:
        return json.loads(out.decode('utf-8'))
    return out
