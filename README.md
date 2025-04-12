# KineticCore Performance Index v2.1

> A web-based calculator to determine a unified hardware performance index based on CPU, GPU, and TDP.

<!-- Example Badges (Use placeholders if URLs not provided) -->
![Version](https://img.shields.io/badge/version-2.1-blue?style=flat-square) <!-- Hardcoded version from project name -->

## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About The Project

This project provides a single-page web application that calculates a 'KineticCore Performance Index'. Users input their CPU single-core score, multi-core score, GPU OpenCL score, and optionally the system's TDP.

The application uses a complex algorithm (v2.1) involving normalization, temporal adjustments, weighting, balance factors, synergy bonuses, latency boosts, and thermal penalties to generate a unified performance score and classify the system into a performance tier. It also includes multi-language support (English/Chinese).

**Key Features:**

*   Calculates a unified performance index from CPU (SC/MC), GPU (OpenCL), and TDP inputs.
*   Uses the KineticCore v2.1 algorithm with normalization, temporal adjustment, balance/synergy factors, and thermal penalties.
*   Classifies results into detailed performance tiers (e.g., Apex, Titan, Quantum).
*   Provides a detailed breakdown of contributing factors and component snapshot.
*   Responsive design for different screen sizes.
*   Multi-language support (English/Chinese) with UI switching.
*   Visual feedback with score, tier, descriptions, and animated bars.
*   Client-side calculation (no backend required).
*   Error handling for invalid inputs.

### Built With

*   HTML5
*   CSS3 (including Flexbox, Grid, gradients, backdrop-filter)
*   JavaScript (ES6+) (Vanilla JS, DOM manipulation, complex calculations, localization)

## Getting Started

This section guides you through running the project locally. As it's a single HTML file, no complex setup is needed.

### Prerequisites

*   A modern web browser supporting HTML5, CSS3, and JavaScript (ES6+). Examples include recent versions of Chrome, Firefox, Safari, or Edge.

### Installation

1.  Download the `index.html` file (or clone the repository containing it).
    ```sh
    git clone https://github.com/KuekHaoYang/KinetiCore.git
    cd KinetiCore
    ```
2.  No further installation steps are required. Simply locate the downloaded `index.html` file.

## Usage

1.  Open the `index.html` file in your web browser (e.g., by double-clicking it or using File > Open).
2.  Enter your CPU Single-Core score (e.g., from a benchmark like Geekbench 6 SC).
3.  Enter your CPU Multi-Core score (e.g., from Geekbench 6 MC).
4.  Enter your GPU Compute score (e.g., from Geekbench 6 OpenCL or Vulkan).
5.  (Optional) Enter the system's TDP (Thermal Design Power) in Watts. If left blank or invalid, a default value (currently 150W) will be used.
6.  Click the "Analyze Performance" button.
7.  Wait for the analysis to complete (a brief "Analyzing..." message will appear).
8.  The results, including the KineticCore Index score, the assigned performance tier (like "Quantum Elite" or "Phoenix"), and a detailed breakdown of normalized scores and contributing factors, will be displayed below the button. A component snapshot provides context on individual input values relative to reference points.
9.  (Optional) Click the language button ("中文" or "English") in the top-right corner to switch the interface language between English and Chinese. The results will automatically update to the selected language if already calculated.

## License

Distributed under the Not Specified License. See `LICENSE` for more information (assuming a `LICENSE` file exists or will be created).
