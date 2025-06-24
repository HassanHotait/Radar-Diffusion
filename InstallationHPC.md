# ⚙️ Python venv Setup for `consistency-models` (with CUDA-Enabled PyTorch)

This script sets up a Python virtual environment with all required dependencies, including CUDA-enabled PyTorch and optional packages.

## 🔧 Setup Script

```bash
#!/bin/bash

# Exit immediately on error
set -e

# Create and activate virtual environment
python3 -m venv consistency-venv
source consistency-venv/bin/activate

# Upgrade pip tools
pip install --upgrade pip setuptools wheel

# Install CUDA-enabled PyTorch (adjust CUDA version if needed)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install required packages
pip install \
    matplotlib \
    pillow \
    easydict \
    einops \
    fvcore \
    joblib \
    open3d \
    cython \
    pandas \
    numpy \
    scipy \
    tqdm \
    albumentations==0.4.3 \
    lmdb \
    mpi4py \
    piq==0.7.0

# Install OpenAI CLIP
pip install git+https://github.com/openai/CLIP.git

# Install flash-attn
pip install flash-attn==0.2.8 --no-build-isolation || echo "⚠️ flash-attn installation failed, may require manual build"

# Install local package if setup.py exists
if [ -f setup.py ]; then
    pip install -e .
fi

# Final check
python -c "import torch; print('Torch version:', torch.__version__, '| CUDA available:', torch.cuda.is_available())"

echo "✅ Environment setup complete!"
```
