import matplotlib.pyplot as plt

def plot_slices(volume_tensor, num_slices=9):
    """
    Plot equally spaced slices from a 3D MRI volume for quick visual inspection.

    Parameters:
        volume_tensor (torch.Tensor or np.ndarray): 
            A 3D MRI volume as a PyTorch tensor or NumPy array. 
            Shape is expected to be (1, H, W, D) or (H, W, D).
        num_slices (int): 
            The number of slices to display from the volume. Default is 9.

    Returns:
        None. Displays a matplotlib figure with the slices.
    """
    # Convert torch tensor to numpy if needed and remove channel dimension if present
    volume = volume_tensor.squeeze().numpy()
    
    # Determine total number of slices in the depth (axial) direction
    depth = volume.shape[-1]
    
    # Calculate step size to evenly sample slices
    step = max(1, depth // num_slices)

    # Set up the plotting grid
    fig, axes = plt.subplots(1, num_slices, figsize=(15, 4))

    # Plot selected slices
    for i in range(num_slices):
        slice_index = i * step
        axes[i].imshow(volume[:, :, slice_index], cmap='gray')
        axes[i].set_title(f"Slice {slice_index}")
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()