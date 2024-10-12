import pennylane as qml
from pennylane import numpy as np

def circA(wires):
    qml.RY(2*np.arccos(1/np.sqrt(3)), wires = wires[2])
    qml.RY(np.pi/4, wires = wires[3])
    qml.CNOT( wires = [wires[2],wires[3]])
    qml.RY(-np.pi/4, wires = wires[3])
    qml.CNOT(wires = [wires[3],wires[4]])
    qml.CNOT(wires = [wires[2],wires[3]])

    qml.CRY(-np.pi/3, wires = [wires[3],wires[0]])
    qml.PauliX(wires = wires[3])

    qml.CRY(np.pi/3, wires = [wires[4],wires[0]])

    qml.PauliZ(wires = wires[4])
    qml.PauliX(wires = wires[4])

    qml.CNOT(wires = [wires[2],wires[0]])
    qml.PauliX(wires = wires[0])

    qml.Hadamard(wires = wires[1])
    qml.CNOT(wires = [wires[1],wires[2]])
    qml.CNOT(wires = [wires[1],wires[3]])
    qml.CNOT(wires = [wires[1],wires[4]])

def circB(wires):
    qml.RY(-np.pi, wires=wires[1])

    qml.RY(2*np.arccos(1/np.sqrt(3)), wires = wires[2])
    qml.RY(np.pi/4, wires = wires[3])
    qml.CNOT( wires = [wires[2],wires[3]])
    qml.RY(-np.pi/4, wires = wires[3])
    qml.CNOT(wires = [wires[3],wires[4]])
    qml.CNOT(wires = [wires[2],wires[3]])

    qml.CRY(-np.pi/3, wires = [wires[3],wires[0]])
    qml.PauliX(wires = wires[3])

    qml.CRY(np.pi/3, wires = [wires[4],wires[0]])

    qml.PauliZ(wires = wires[4])
    qml.PauliX(wires = wires[4])

    qml.CNOT(wires = [wires[2],wires[0]])
    qml.PauliX(wires = wires[0])

    qml.CNOT(wires = [wires[1],wires[2]])
    qml.CNOT(wires = [wires[1],wires[3]])
    qml.CNOT(wires = [wires[1],wires[4]])
    qml.Hadamard(wires = wires[1])

def circC(wires):
    qml.RY(-np.pi, wires=wires[0])
    qml.RY(-np.pi, wires=wires[1])
    
    qml.CNOT(wires = [wires[0],wires[1]])
    qml.Hadamard(wires = wires[0])

    qml.CNOT(wires = [wires[0],wires[2]])
    qml.Hadamard(wires = wires[2])
    qml.CNOT(wires = [wires[2],wires[3]])

    qml.CNOT(wires = [wires[1],wires[3]])

    qml.adjoint(qml.T)(wires= wires[0])
    qml.T(wires = wires[1])
    qml.CNOT(wires = [wires[0],wires[1]])
    qml.Hadamard(wires = wires[0])
    qml.T(wires = wires[0])
    qml.CNOT(wires = [wires[1],wires[0]])

    qml.adjoint(qml.T)(wires= wires[0])
    qml.T(wires = wires[1])
    qml.Hadamard(wires = wires[0])
    qml.CNOT(wires = [wires[0],wires[1]])
    
    qml.PauliX(wires = wires[1])

    qml.CRY(-2*np.arccos(1/np.sqrt(3)), wires=[wires[1],wires[0]])

    qml.PauliX(wires = wires[1])
    qml.CNOT(wires = [wires[0],wires[1]])
    qml.PauliX(wires = wires[0])

def circD(wires):
    qml.RY(-np.pi, wires=wires[0])
    qml.RY(-np.pi, wires=wires[1])
    qml.RY(-np.pi, wires=wires[2])

    qml.CNOT(wires = [wires[0],wires[1]])
    qml.CNOT(wires = [wires[2],wires[3]])
    qml.Hadamard(wires = wires[0])
    qml.Hadamard(wires = wires[2])

    qml.CNOT(wires = [wires[0],wires[2]])
    qml.CNOT(wires = [wires[1],wires[3]])

    qml.adjoint(qml.T)(wires= wires[0])
    qml.T(wires = wires[1])
    qml.CNOT(wires = [wires[0],wires[1]])
    qml.Hadamard(wires = wires[0])
    qml.T(wires = wires[0])
    qml.CNOT(wires = [wires[1],wires[0]])

    qml.adjoint(qml.T)(wires= wires[0])
    qml.T(wires = wires[1])
    qml.Hadamard(wires = wires[0])
    qml.CNOT(wires = [wires[0],wires[1]])
    
    qml.PauliX(wires = wires[1])

    qml.CRY(-2*np.arccos(1/np.sqrt(3)), wires=[wires[1],wires[0]])

    qml.PauliX(wires = wires[1])
    qml.CNOT(wires = [wires[0],wires[1]])
    qml.PauliX(wires = wires[0])

def circE(wires):
    qml.RY(-np.pi, wires=wires[0])
    qml.RY(-np.pi, wires=wires[1])
    qml.RY(-np.pi, wires=wires[2])
    qml.RY(-np.pi, wires=wires[3])

    qml.CNOT(wires = [wires[0],wires[1]])
    qml.CNOT(wires = [wires[2],wires[3]])
    qml.Hadamard(wires = wires[0])
    qml.Hadamard(wires = wires[2])

    qml.CNOT(wires = [wires[0],wires[2]])
    qml.CNOT(wires = [wires[1],wires[3]])

    qml.adjoint(qml.T(wires= wires[0]))
    qml.T(wires = wires[1])
    qml.CNOT(wires = [wires[0],wires[1]])
    qml.Hadamard(wires = wires[0])
    qml.T(wires = wires[0])
    qml.CNOT(wires = [wires[1],wires[0]])

    qml.adjoint(qml.T(wires= wires[0]))
    qml.T(wires = wires[1])
    qml.Hadamard(wires = wires[0])
    qml.CNOT(wires = [wires[0],wires[1]])
    
    qml.PauliX(wires = wires[1])

    qml.CRY(-2*np.arccos(1/np.sqrt(3)), wires=[wires[1],wires[0]])

    qml.PauliX(wires = wires[1])
    qml.CNOT(wires = [wires[0],wires[1]])
    qml.PauliX(wires = wires[0])

def circAA(wires):
    qml.RY(2*np.arccos(1/np.sqrt(3)), wires = wires[2])
    qml.RY(np.pi/4, wires = wires[3])
    qml.CNOT( wires = [wires[2],wires[3]])
    qml.RY(-np.pi/4, wires = wires[3])
    qml.CNOT(wires = [wires[3],wires[4]])
    qml.CNOT(wires = [wires[2],wires[3]])

    qml.PauliX(wires = wires[3])

    qml.PauliZ(wires = wires[4])
    qml.PauliX(wires = wires[4])

    qml.PauliX(wires = wires[0])
    qml.CNOT(wires = [wires[2],wires[0]])
    qml.CRY(np.pi/3, wires = [wires[4],wires[0]])
    qml.CRY(-np.pi/3, wires = [wires[3],wires[0]])

    qml.Hadamard(wires = wires[1])
    qml.CNOT(wires = [wires[1],wires[2]])
    qml.CNOT(wires = [wires[1],wires[3]])
    qml.CNOT(wires = [wires[1],wires[4]])


def circBB(wires):
    qml.RY(-np.pi, wires=wires[1])

    qml.RY(2*np.arccos(1/np.sqrt(3)), wires = wires[2])
    qml.RY(np.pi/4, wires = wires[3])
    qml.CNOT( wires = [wires[2],wires[3]])
    qml.RY(-np.pi/4, wires = wires[3])
    qml.CNOT(wires = [wires[3],wires[4]])
    qml.CNOT(wires = [wires[2],wires[3]])

    qml.PauliX(wires = wires[3])


    qml.PauliZ(wires = wires[4])
    qml.PauliX(wires = wires[4])

    qml.PauliX(wires = wires[0])
    qml.CNOT(wires = [wires[2],wires[0]])
    qml.CRY(np.pi/3, wires = [wires[4],wires[0]])
    qml.CRY(-np.pi/3, wires = [wires[3],wires[0]])

    qml.CNOT(wires = [wires[1],wires[2]])
    qml.CNOT(wires = [wires[1],wires[3]])
    qml.CNOT(wires = [wires[1],wires[4]])
    qml.Hadamard(wires = wires[1])