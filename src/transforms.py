import torchio as tio

def rescale_intensity(subject):
    """
    Rescale the intensity of the MRI image to a standard range (usually [0, 1] or [0, 255]).

    This is useful for standardizing input values across subjects, 
    especially for visualization or preparing data for machine learning.

    Parameters:
        subject (tio.Subject): A TorchIO Subject containing an MRI image.

    Returns:
        tio.Subject: The same subject with rescaled image intensities.
    """
    transform = tio.RescaleIntensity()
    return transform(subject)


def resize(subject, target_shape=(256, 256, 150)):
    """
    Resize the 3D MRI image to a uniform shape.

    This is important to ensure all input volumes have the same spatial dimensions, 
    which is required for batching in deep learning models.

    Parameters:
        subject (tio.Subject): A TorchIO Subject containing an MRI image.
        target_shape (tuple): Desired output shape as (width, height, depth).

    Returns:
        tio.Subject: The same subject with resized MRI volume.
    """
    transform = tio.Resize(target_shape)
    return transform(subject)