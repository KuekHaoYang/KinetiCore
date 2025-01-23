# KineticCore 🚀

> A sophisticated system performance evaluation tool that provides instant, future-aware hardware ratings.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

KineticCore is an intelligent system analysis tool that evaluates hardware components using advanced metrics and provides meaningful insights about your system's capabilities. It uses quantum-inspired normalization and temporal adjustments to deliver accurate, future-proof performance ratings.

## Features

- 🎯 **Instant Performance Rating**: Get a comprehensive score out of 140 points
- 🔮 **Future-Aware Analysis**: Automatically adjusts scores based on technological progression
- 🌡️ **Thermal Efficiency**: Considers power consumption and thermal characteristics
- 📊 **Component-Level Analysis**: Detailed insights for CPU and GPU performance
- 📈 **Multiple Export Formats**: Save reports in JSON, CSV, or TXT formats
- 🎨 **Color-Coded Output**: Intuitive visual feedback using terminal colors

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KuekHaoYang/KinetiCore.git
cd kineticcore
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python main.py
```

Follow the prompts to input your system's benchmark scores:
- Single-Core CPU Score
- Multi-Core CPU Score
- OpenCL GPU Score
- TDP (Thermal Design Power) in Watts

## Performance Tiers

The system classifies hardware into the following performance strata:

| Score Range | Tier | Description |
|------------|------|-------------|
| 140+ | Titan Class | Beyond cutting-edge systems |
| 120-139 | Quantum Elite | Flagship workstations |
| 100-119 | Dragonfire | Extreme gaming rigs |
| 80-99 | Phoenix | Enthusiast systems |
| 60-79 | Griffin | Premium devices |
| 40-59 | Basilisk | Productivity systems |
| 20-39 | Chimera | Basic computing |
| 0-19 | Ancient | Legacy hardware |

## Technical Details

### Reference Benchmarks
- Single-Core CPU: 2800 points
- Multi-Core CPU: 18000 points
- GPU (OpenCL): 45000 points
- Reference TDP: 150W

### Scoring Methodology
- Quantum-normalized component scores
- Temporal adjustment for technology progression
- Harmonic weighted averaging
- Thermal efficiency considerations
- System balance analysis

## Requirements

- Python 3.6 or higher
- colorama
- math (standard library)
- datetime (standard library)
- json (standard library)
- csv (standard library)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created with ❤️ by Kuek Hao Yang

## Acknowledgments

- Inspired by modern benchmark methodologies
- Uses colorama for terminal coloring
- Mathematical models based on quantum-inspired normalization 