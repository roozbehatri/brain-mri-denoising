import nibabel as nib         # For handling NIfTI images
import torchio as tio         # For preprocessing medical images
import torch                 # Required to check tensor types
import numpy as np          

def load_mri(path):
    """
    Load an MRI volume using TorchIO and wrap it in a Subject object.
    
    Parameters:
        path (str): File path to the MRI image (e.g., .nii or .nii.gz)

    Returns:
        torchio.Subject: A Subject object containing the loaded MRI image
    """
    return tio.Subject(mri=tio.ScalarImage(path))


def save_mri(tensor, reference_image, output_path):
    """
    Save a processed MRI tensor as a NIfTI image using a reference affine.

    Parameters:
        tensor (torch.Tensor or np.ndarray): Image tensor to be saved, shape (1, H, W, D) or (H, W, D)
        reference_image (torchio.Image): TorchIO image to extract affine transformation from
        output_path (str): Destination path to save the image (e.g., .nii.gz)

    Returns:
        None
    """
    # Convert tensor to numpy if it's a PyTorch tensor
    if isinstance(tensor, torch.Tensor):
        tensor = tensor.squeeze().numpy()  # Remove singleton dimensions if needed

    # Use the affine from the reference image to preserve spatial metadata
    affine = reference_image.affine

    # Create a NIfTI image and save it to disk
    nifti_img = nib.Nifti1Image(tensor, affine=affine)
    nib.save(nifti_img, output_path)