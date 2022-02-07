import os
import sys
import time
import subprocess

LOG="log.txt"
PODLOGS="podlogs.txt"

class bcolors:
    GREEN = '\033[92m'  # GREEN
    YELLOW = '\033[93m'  # YELLOW
    RED = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    LIGHT_BLUE = '\033[36m'
    ERROR = '\033[91m'

def refresh_loop(eksNode):

    logFile = open(LOG, 'w')
    K8SPODCMD="""kubectl get po -A -o wide --show-labels | grep {} | awk '{{print $2, $11}}'""".format(eksNode)
    
    subprocess.call(K8SPODCMD, shell=True, stdout=logFile, stderr=logFile)

    with open(LOG, 'r') as podsToDrain:
        for line in podsToDrain:           
            pod = line.split(" ")[0]
            label = line.split(" ")[1].split(",")[0]
            print(label)
            drain_pod(eksNode, pod, label)

def drain_pod(eksNode, pod, label):
    podLog = open(PODLOGS, 'a')
    ECHOCMD="""echo draining {} on node {}""".format(pod,eksNode)
    subprocess.call(ECHOCMD, shell=True, stdout=podLog, stderr=podLog)
    K8SDRAINCMD = """kubectl drain {} --ignore-daemonsets --delete-emptydir-data --pod-selector={}""".format(eksNode,label)
    subprocess.call(K8SDRAINCMD, shell=True, stdout=podLog, stderr=podLog)

if __name__ == '__main__':
    refresh_loop(sys.argv[1])