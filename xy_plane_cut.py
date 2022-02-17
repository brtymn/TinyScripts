import numpy as np

# Phaseon definition function that slices the phase space along the XY plane.
def PlaneCutXY(pdf_arr, num_points, num_cuts):
    plane_cut = []
    # Reshape the probability density function to a one dimensional array for the following operations.
    shaped = np.reshape(pdf_arr, (1, num_points**2), order = "C")[0]
    # Define an interval to perform the 2D cuts.
    cut_interval = np.linspace(min(shaped), max(shaped), num_cuts+1)
    for i in range(num_cuts):
        # Construct a mask (array that consists of True/False) to apply the boundary conditions of the phaseons, i.e. the cut intervals.
        mask = np.logical_and(shaped >= cut_interval[i], shaped <= cut_interval[i+1])
        # Apply the mask on the 1D PDF array.
        masked_shaped = np.where(mask, shaped, np.nan)
        # Reshaping the masked 1D array yields the phaseon.
        single_cut = masked_shaped.reshape((num_points, num_points))
        # Construct an array that contains single phaseons with shape (num_phaseon-1, num_points, num_points).
        plane_cut.append(single_cut)

    return plane_cut
