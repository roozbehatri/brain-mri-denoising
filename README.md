# 🧠 MRI Preprocessing and Exploration

This project provides a practical, modular pipeline for loading, preprocessing, and visualizing 3D brain MRI scans using Python. It is designed to support exploratory analysis, deep learning model preparation, and preprocessing tasks such as intensity normalization, resizing, and visualization.

## 📁 Project Structure

```text
project/
├── data/
│   ├── raw/                # Raw MRI NIfTI files (e.g., T1, T2, PD)
│   └── preprocessed/       # Outputs after preprocessing (e.g., skull-stripped, rescaled)
├── notebooks/
│   ├── 01_mri_exploration.ipynb     # MRI loading and 2D/3D visualization
│   └── 02_preprocessing_mri.ipynb   # Rescaling, resizing, saving preprocessed volumes
├── src/
│   ├── io_utils.py         # Functions for loading/saving MRI data
│   ├── preprocess.py       # Rescaling and resizing transformations
│   └── visualize.py        # MRI slice plotting tools
└── README.md
```

## 🔧 Features

- Load and save `.nii` or `.nii.gz` format MRI volumes using TorchIO and NiBabel
- Intensity normalization and 3D resizing
- Modular and reusable code structure
- Quick visualization of multiple MRI slices
- Easily extendable for denoising, skull stripping, and registration

## 🧪 Requirements

- Python 3.8+
- [torchio](https://github.com/fepegar/torchio)
- nibabel
- matplotlib
- numpy

Install via `conda`:
```bash
conda create -n mri-env python=3.9
conda activate mri-env
pip install torchio nibabel matplotlib numpy


## 📊 Example Usage
```python
from src.io_utils import load_mri, save_mri
from src.preprocess import rescale_intensity, resize
from src.visualize import plot_slices

subject = load_mri("data/raw/100_Guys/T1.nii.gz")
subject = rescale_intensity(subject)
subject = resize(subject)
plot_slices(subject.mri.data)
save_mri(subject.mri.data, subject.mri, "data/preprocessed/100_Guys_preprocessed.nii.gz")
```