# Manga Text Remover

## Description
Manga Text Remover is a Python application designed to automatically detect and remove text from manga images, providing a clean and unobstructed view of the artwork.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python 3.9** or lower is installed on your system.
- The following Python libraries are installed:
  - **Pillow**: For image processing.
  - **EasyOCR**: For optical character recognition.
  - **Torch**: For deep learning models.

## Installation
To install Manga Text Remover, follow these steps:

1. Clone the repository:

```markdown
git clone https://github.com/MELLO-88/Manga-Test-Remover.git
```
2. Navigate to the cloned directory:

```markdown
cd Manga-Test-Remover
```
3. Install the required libraries:

```markdown
pip install Pillow easyocr torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Usage
To use Manga Text Remover, follow these steps:

1. Place your manga images in the `manga_folder` directory.
2. Run the application:
```markdown
python main.py
```
3. Processed images will be saved in the `output_folder` directory.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

