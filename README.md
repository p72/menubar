# MenuBar

A simple macOS menu bar application built with Python and rumps.

## Features

- Runs as a menu bar application
- Lightweight and minimal interface
- Built with Python 3.12

## Requirements

- macOS
- Python 3.12
- rumps library
- py2app (for building)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/p72/menubar.git
cd menubar
```

2. Install dependencies:
```bash
pip install rumps py2app
```

## Usage

### Run from source:
```bash
python menubar.py
```

### Build standalone app:
```bash
python simple_setup.py py2app
```

The built application will be available in the `dist/` folder as `menubar.app`.

## Development

- `menubar.py` - Main application file
- `simple_setup.py` - Build configuration for py2app

## License

MIT License