# 🧪 Setup Guide for `consistency-models` with CUDA-Enabled PyTorch

This guide walks you through installing all dependencies for the `consistency-models` project, including commented-out modules in `setup.py`.

---

## ✅ Step 1: Check System CUDA Version

```bash
nvidia-smi



conda create -n cm python=3.9 -y
conda activate cm


conda install pytorch=2.1.2 torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y


conda install -c conda-forge \
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
    albumentations=0.4.3 \
    lmdb \
    mpi4py -y

conda install cudatoolkit cuda-version=11

conda install nccl    


pip install piq==0.7.0


pip install git+https://github.com/openai/CLIP.git


pip install flash-attn==0.2.8 --no-build-isolation


pip install -e .


python -c "import torch; print(torch.__version__, torch.cuda.is_available())"

