# Python's Progress Bar for console
A lightweight, customizable progress bar for Python3.6+

## Features
- Easy to use and integrate
- Highly customizable (colors, length, style)
- Lightweight and dependency-free
- Works seamlessly with loops and background tasks

## Installation
Install the library via pip:
pip install python-progress-bar

## Usage
Here's a quick example to get started:
from progress_bar import ProgressBar

## Initialize the progress bar
```python
from python_progress_bar import ProgressBar

pb = ProgressBar('Progress', bar_char='█')

for i in range(100):
    pb.show(35.0)
```

### Customization

The progress bar can be customized to fit your needs:

```python
from python_progress_bar import ProgressBar, FontScheme

fnts = FontScheme(Title=Font.LightPurple, Bar=Font.Yellow, Percentage=Font.LightGreen)
pb = ProgressBar('#4', bar_char='★', font_scheme=fnts)
```


## Contributing

Contributions are welcome! To contribute:
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Commit your changes (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.


## Stay Connected

Star this repo ⭐ if you find it useful. 

Fork it 🍴 to contribute.

Share your feedback or suggestions by opening an issue.


