#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="nnvision",
    version="0.1",
    description="Envisioning the biological visual system with DNN",
    author="Konstantin Willeke",
    author_email="konstantin.willeke@gmail.com",
    packages=find_packages(exclude=[]),
    package_dir={'nnvision': 'nnvision'},
    install_requires=[
        "setuptools>=50.3.2",
        "einops",
        "scikit-image==0.19.1",
        "numpy==1.22.0",
        "datajoint>=0.12.7",
        "GitPython>=3.1.30",
        "matplotlib>=3.3.2",
        "scipy>=1.5.4",
        "torch>=1.7.0",
        "torchvision>=0.8.1",
        "transformers==4.35.2",
        "tqdm>=4.51.0",
        "nnfabrik",
        "neuralpredictors @ git+https://github.com/KonstantinWilleke/neuralpredictors.git@transformer_readout",
        "mei @ git+https://github.com/sinzlab/mei.git@inception_loop",
        "CORnet @ git+https://github.com/KonstantinWilleke/CORnet.git",
        "ptrnets @ git+https://github.com/sacadena/ptrnets.git@6f459a130ff2fb1a73f29d933e6bea5b435341e7",
    ],
    package_data={
        "nnvison": [
            "data/model_weights/*.pth.tar",
            "data/model_weights/*.pth",
            "data/model_weights/*.tar",
            "data/model_weights/v4_multihead_attention_SOTA.pth.tar",

        ],
    },
)
