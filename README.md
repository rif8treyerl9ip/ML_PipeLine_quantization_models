# ML_PipeLine_quantization_models

**Note:** This repository assumes the use of ONNX GPU and PyTorch GPU. You need to install the corresponding GPU drivers, CUDA Toolkit, and CuDNN. Install the appropriate versions of drivers, CUDA Toolkit, CuDNN, ONNX, and ONNX-gpu according to your environment. It is recommended to set the versions based on the [environment requirements for ONNX-gpu](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#requirements).

## Overview

This tool is designed to efficiently manage the training process and experimental results of machine learning models. By using a database to organize experimental results, it facilitates result comparison and analysis. Users can easily observe performance changes associated with multiple models or parameter adjustments.

## Features

- **Local Environment Usage**: Users can use the tool on their own PC, enabling experiment management even in environments without an internet connection.
- **Support for Diverse Models**: It supports different types of machine learning models and frameworks, catering to a wide range of experimental needs.
- **Interactive Result Display**: Experimental results are displayed in a visually comprehensible form, such as graphs or tables, allowing for quick understanding of data trends and characteristics.
- **Automated Experiment Tracking**: Parameters, achievements, logs, and other information for each experiment are automatically recorded, eliminating the need for manual record-keeping.
- **Customizable Report Generation**: Users can create customized reports tailored to their needs, facilitating presentations and documentation.

## Setup

- Install postgresql according to your operating system.
- Using pgadmin, create a database (e.g., ML_models) for managing machine learning models.
- Install packages using requirements.txt.

```bash
pip install -r requirements.txt
```
- Start the PostgreSQL server

```bash
# For example
cd C:/Program Files/PostgreSQL/12
pg_ctl start -D data
```

## Steps for Database Connection and Table Creation

1. Edit the `DBConfigurations` class in `./db/src/configurations.py` to configure the database connection settings.
2. Run `./db/app.py` to test if the configuration is functioning correctly. This script will automatically create the necessary tables in the database.

## Usage

### Running Experiments in a GPU-enabled Environment
- This tool assumes the use of ONNX GPU and PyTorch GPU. When running experiments in a GPU-enabled environment, ensure that the appropriate GPU drivers and CUDA Toolkit are installed.

### Setting up Database Connection
- Prepare a configuration file (config file) containing the necessary information (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_SERVER`) to connect to the database.
- Test the configuration file by loading it from a notebook and performing a connection test.

### Running Experiments
- Use the notebooks in the `./notebooks` folder to conduct experiments.
- In the notebooks, you will manually set parameters such as the short commit hash and model name.
- With the set parameters, you can train models, add models to the database, and visualize training results.
