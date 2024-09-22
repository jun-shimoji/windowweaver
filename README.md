# WindowWeaver

WindowWeaver is a lightweight tool designed to enhance window management on Windows. It allows users to move, resize, and drag windows with simple keyboard shortcuts, utilizing the **Shift** and **Context Menu** keys. The **Alt** key is no longer used in this version.

## Features

- **Move Windows**: Press and hold the **Shift key** and move the mouse to drag the active window.
- **Resize Windows**: Press and hold the **Shift key** and the **Context Menu key** to resize the active window by moving the mouse.
- **Drag Function**: Press and hold the **Context Menu key** and move the mouse to simulate a left-click drag operation.

## Installation

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone the Repository**

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

You can run the script without any arguments:

   ```bash
   python windowweaver.py
   ```

## Usage
* Move Windows: Press and hold the Shift key and move your mouse to drag the active window.
* Resize Windows: Press and hold the Shift key and the Context Menu key and move your mouse to resize the active window.
* Drag Function: Press and hold the Context Menu key and move your mouse to simulate a left-click drag operation.

Note: The Alt key functionality has been completely removed in this version. All actions are now controlled using the Shift and Context Menu keys.

## Virtual Environment (Optional)
For users who prefer to keep their project dependencies isolated, it's recommended to create a virtual environment. This is not required but can be helpful for managing dependencies.

Create a Virtual Environment Navigate to your project directory:

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
