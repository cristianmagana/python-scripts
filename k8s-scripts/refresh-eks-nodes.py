import os
import sys
import time
import subprocess

class bcolors:
    GREEN = '\033[92m'  # GREEN
    YELLOW = '\033[93m'  # YELLOW
    RED = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    LIGHT_BLUE = '\033[36m'
    ERROR = '\033[91m'

LOG="log.txt"

def refresh_loop(eksNode):
    K8SPODCMD="""kubectl get po -A -o wide | grep {} | aws '{{print $1, $2}}'""".format(eksNode)
    
    logFile = open(LOG, 'w')
    subprocess.call(K8SPODCMD, shell=True, stdout=logFile, stderr=logFile)

    with open(LOG, 'w') as ns_inputs:
        for ns in ns_inputs:           
            ns = ns.strip()
            print("-------------  Evaluating " + ns +" -------------  ")
            get_tenant_info(tenantEnv, ns)



if __name__ == '__main__':
    refresh_loop(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])