# WindowWeaver

WindowWeaver is a lightweight tool that allows you to easily move and resize windows on Windows using keyboard shortcuts. You can choose to use either the Alt key or the Context Menu key as the modifier key for these actions.

## Features

- Move Windows: Press and hold the modifier key (Alt or Context Menu) to move the active window by dragging the mouse.
- Resize Windows: Press and hold the modifier key and Shift key to resize the active window by dragging the mouse.

## Installation

### Prerequisites

- Python 3.6+: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps

1. Clone the Repository

   ```bash
   git clone https://github.com/yourusername/WindowWeaver.git
   cd WindowWeaver
   ```

2. Install the required Python packages

   Navigate to the project directory and install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run WindowWeaver

   You can run WindowWeaver with the default settings or specify your preferred modifier key:

   ```bash
   python windowweaver.py --key alt
   ```

   Or use the Context Menu key (default):

   ```bash
   python windowweaver.py --key context
   ```

   You can also simply run the script without any arguments, and it will default to using the Context Menu key:

   ```bash
   python windowweaver.py
   ```

## Usage

- Move Windows: Press and hold the selected modifier key (Alt or Context Menu) and move your mouse to drag the active window.
- Resize Windows: Press and hold the selected modifier key along with the Shift key and move your mouse to resize the active window.

### Command Line Arguments

- `--key alt`: Use the Alt key as the modifier key.
- `--key context`: Use the Context Menu key as the modifier key (default).

### Help

For more information on how to use the script, run:

```bash
python windowweaver.py --help
```

## Virtual Environment (Optional)

For users who desire to keep their project dependencies isolated, it's recommended to create a virtual environment. This is not required but can be helpful in managing dependencies.

### 1. Create a Virtual Environment

1. Navigate to your project directory:

   ```bash
   cd WindowWeaver
   ```

2. Create the virtual environment:

   On Windows:

   ```bash
   python -m venv venv # for background process, use pythonw
   ```

   On macOS/Linux:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Deactivate the virtual environment when you're done:

   ```bash
   deactivate
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
