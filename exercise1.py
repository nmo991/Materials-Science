from pymatgen.core import Structure, Lattice
from matminer.featurizers.structure import DensityFeatures
import numpy as np

# Create NaCl structure manually
lattice = [[5.64, 0, 0], [0, 5.64, 0], [0, 0, 5.64]]
species = ["Na", "Na", "Na", "Na", "Cl", "Cl", "Cl", "Cl"]
coords = [
    [0.0, 0.0, 0.0],    # Na
    [0.0, 0.5, 0.5],    # Na
    [0.5, 0.0, 0.5],    # Na
    [0.5, 0.5, 0.0],    # Na
    [0.5, 0.5, 0.5],    # Cl
    [0.5, 0.0, 0.0],    # Cl
    [0.0, 0.5, 0.0],    # Cl
    [0.0, 0.0, 0.5]     # Cl
]

# Create the structure
nacl_structure = Structure(lattice, species, coords)

print("NaCl Structure:")
print(nacl_structure)
print(f"\nFormula: {nacl_structure.formula}")
print(f"Number of sites: {len(nacl_structure)}")
print(f"Lattice parameters: {nacl_structure.lattice.parameters}")

# Calculate density and packing fraction using DensityFeatures
featurizer = DensityFeatures()
features = featurizer.featurize(nacl_structure)

print("\nDensity Features:")
print(f"Density: {features[0]:.4f} g/cm³")
print(f"Packing fraction: {features[1]:.4f}")
print(f"Volume per atom: {features[2]:.4f} Å³/atom")

# You can also get the feature names to see what each value represents
feature_names = featurizer.feature_labels()
print(f"\nFeature names: {feature_names}")