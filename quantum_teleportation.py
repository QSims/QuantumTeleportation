####################################

#Created by: Simsarul Haq Vengasseri
#Date: 30/10/2017

# This program demonstrations quantum teleportation. This program is designed to teleport any of the following three quantum states. However, this algorithm can be used to teleport any quantum state.
# 1) |0>
# 2) |1>
# 3) (1/sqrt(2))|0> + (1/sqrt(2))|1>
# Please modify the path to the referenceqvm directory to import the api library.



import sys
sys.path.insert(0, '/home/infinitylabs/Documents/QSimulations/QSims/reference-qvm/referenceqvm')
import api
import pyquil.quil as pq
from pyquil.gates import *

qvm = api.SyncConnection()

def quantum_teleport(quantum_state):
    ins = pq.Program()
    ins.inst(I(1), I(2), H(1), CNOT(1,2)) #Creating B00
    if(quantum_state==0):
        ins.inst(I(0))
        qbits, addr = qvm.wavefunction(ins, [0,1])
        print "Initial state is {}".format(qbits)
        ins.inst(CNOT(0,1),H(0))
        ins.measure(0,0).measure(1,1).if_then(1, X(2)).if_then(0, Z(2))
    elif(quantum_state==1):
        ins.inst(X(0))
        qbits, addr = qvm.wavefunction(ins, [0,1])
        print "Initial state is {}".format(qbits)
        ins.inst(CNOT(0,1),H(0))
        ins.measure(0,0).measure(1,1).if_then(1, X(2)).if_then(0, Z(2))
    elif(quantum_state==2):
        ins.inst(I(0),H(0))
        qbits, addr = qvm.wavefunction(ins, [0,1])
        print "Initial state is {}".format(qbits)
        ins.inst(CNOT(0,1),H(0))
        ins.measure(0,0).measure(1,1).if_then(1, X(2)).if_then(0, Z(2))
    qbits, addr = qvm.wavefunction(ins, [0,1])
    return qbits


if __name__ == '__main__':
    if (len(sys.argv)>1):
        try:
            quantum_state = int(sys.argv[1])
            if(quantum_state==0 or quantum_state==1 or quantum_state==2):
                result = quantum_teleport(quantum_state)
                print "Final state is {}".format(result)
            else:
                print "Please specify the correct qauntum state you need to teleport. \n 1) |0> \n 2) |1> \n 3) (1/sqrt(2))|0> + (1/sqrt(2))|1> \n Please input any number denoting the quantum state as argument."

        except ValueError:
            print ("Enter an integer as argument.")
            sys.exit(1)
    else:
        print "Please specify which of the following qauntum state you need to teleport. \n 1) |0> \n 2) |1> \n 3) (1/sqrt(2))|0> + (1/sqrt(2))|1> \n Please input any number denoting the quantum state as argument. "
