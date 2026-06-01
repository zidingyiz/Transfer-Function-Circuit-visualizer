# Transfer Function Circuit Visualizer

A Python-based transfer function and circuit visualization toolkit for learning, designing, and analyzing analog filters.

The final version of this project will be packaged as a web application. Users will be able to choose a predefined filter or enter a custom transfer function, then generate Bode plots, transfer equations, and reference circuit diagrams.

## Project Status

This project is currently in the early Python prototype stage.

The existing desktop prototype is implemented with Tkinter, NumPy, and Matplotlib. It currently supports:

- Selecting low-pass, high-pass, and band-pass filters from a simple desktop interface
- Entering filter parameters such as cutoff frequencies and gain
- Generating transfer function text for the selected filter
- Plotting basic Bode magnitude and phase graphs
- Using either an approximate or precise phase calculation for the current band-pass prototype, depending on the cutoff-frequency spacing

The current implementation is a work in progress. Some calculations, validation rules, and user-interface details still need refinement before the web version is built.

## Planned Web Application

The finished web application will provide two modes.

### Filter Mode

Filter Mode will guide users through common filter designs. Users will be able to:

- Select a filter type
- Enter the required filter parameters
- Generate Bode magnitude and phase plots
- Switch between hand-drawn asymptotic approximations and precise plots
- View the corresponding transfer equation
- View a reference circuit diagram for the selected filter

### Free Mode

Free Mode will allow users to enter a custom transfer function directly. The application will:

- Parse the transfer function
- Generate approximate or precise Bode plots
- Provide a reference circuit diagram when the transfer function is physically realizable
- Explain when a physically realizable reference circuit cannot be provided

## Roadmap

- [x] Create an initial Python desktop prototype
- [x] Add low-pass, high-pass, and band-pass filter selection
- [x] Generate initial Bode magnitude and phase plots
- [x] Generate transfer function text for predefined filters
- [ ] Refine mathematical calculations and input validation
- [ ] Add a consistent manual switch for approximate and precise plotting
- [ ] Add circuit-diagram generation for predefined filters
- [ ] Implement custom transfer-function parsing
- [ ] Add physical-realizability checks and reference circuit suggestions
- [ ] Package the visualizer as a web application

## Running the Current Prototype

Install the required Python packages:

```bash
pip install numpy matplotlib
```

Run the desktop prototype:

```bash
python MVP_Visualizer.py
```

## Technology

Current prototype:

- Python
- Tkinter
- NumPy
- Matplotlib

Planned web version:

- Python backend
- HTML, CSS, and JavaScript frontend

## Author

Designed and implemented by Qijun Zhou.
