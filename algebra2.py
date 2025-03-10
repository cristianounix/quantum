import numpy as np
import matplotlib as plt

# ⟨ |Ψ⟩ |Φ⟩

# Define a ket: 
ket_psi = np.array([[1],[2]]) #  |Ψ⟩
ket_phi = np.array([[3],[4]]) #  |Φ⟩

print("|Ψ⟩ = ", ket_psi)
print("|Φ⟩ = ", ket_phi)


# Define a Bra:
bra_psi = ket_psi.conj().T # ⟨Ψ|, Transposed an conjuged of |Ψ⟩
bra_phi = ket_phi.conj().T # ⟨Φ|, Transposed an conjuged of |Φ⟩

print("⟨Ψ| = ", ket_psi)
print("⟨Φ| = ", ket_phi)


# Inner product (Bra-Ket): ⟨Ψ|Φ⟩
inner_product = np.dot(bra_psi, ket_phi)
print("Inner product ⟨Ψ|Φ⟩ = ", inner_product)

# Outer product (Bra-Ket): |Ψ⟩⟨Φ|
outer_product = np.dot(ket_psi, bra_phi)
print("Outer product |Ψ⟩⟨Φ| = ", outer_product)

# Tensorial Product: |Ψ⟩ e |Φ⟩
tensor_product = np.kron(ket_psi, ket_phi)
print("Outer product |Ψ⟩|Φ⟩ = ", tensor_product)


