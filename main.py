"""
BEAM-ANALYSIS

1. Define Beam Parameters
2. Add Loads
3. Input Boundary Conditions
4. Run Analysis
"""

from beam_analysis.Beam import Beam

if __name__ == "__main__":
    print("running...")
    
    # =============================== #
    # ======= Youngs Modulus E ====== #
    # ===== Moment of Inertia I ===== #
    # ======== Beam Length L ======== #
    # =============================== #
    E = 207 * 10**9
    I = 2 * 10**-8
    L = 1.0

    # =============================== #
    # = Make the beam and add loads = #
    # =============================== #
    B = Beam(L, E, I)
    B.addPointLoad(0, 11)
    B.addPointLoad(1, 11)
    B.addPointLoad(0.5, -21)
    B.addDistributedLoad(0, 1, -1.0)

    # =============================== #
    # === Add Boundary Conditions === #
    # =============================== #
    # currently req 1 to be angle and other to be deflection
    B.addBoundaryCondition(0.5, "angle", 0.0)
    B.addBoundaryCondition(0.0, "deflection", 0.0)

    # =============================== #
    # ======== Display Info ========= #
    # =============================== #
    B.showParams()

    # =============================== #
    # ======== Run Analysis ========= #
    # =============================== #
    B.analyze()