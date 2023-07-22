# Image To PDF Maker

The **Image To PDF Maker** is a Python script that allows users to convert a collection of images into a PDF document with a simple and user-friendly graphical interface. The script utilizes the Tkinter library to create the graphical user interface (GUI) and the img2pdf library for the image to PDF conversion.

## Features

1. **Testing Text File**:
   - This option creates a text file named "img_files.txt" containing the list of image files sorted numerically by their filenames. It is useful for testing and verifying the correct sorting of images before converting them into a PDF.

2. **PDF Conversion**:
   - This option converts the images into a PDF document with adjustable DPI (dots per inch) settings for different output qualities. The user can select from three DPI options: Screen (72 DPI), Ebook (150 DPI), and Prepress (300 DPI). Higher DPI values result in higher quality PDFs with larger file sizes.

3. **Normal Conversion**:
   - This option performs a standard conversion of the images into a PDF document without any DPI options. Images are sorted naturally by filename (using a custom sort key function) and then converted into a PDF at a fixed DPI of 300.

## Requirements

- Python 3.x
- img2pdf library (`pip install img2pdf`)

## How to Use

1. Run the Python script `image_to_pdf_maker.py`.
2. A window with the Image To PDF Maker GUI will appear.
3. Select the image directory by clicking the "Select Image Directory" button. The chosen directory will be displayed below.
4. Enter the image extension (e.g., ".png", ".jpg") in the entry field. This extension will be used to filter the images in the selected directory for conversion.
5. Choose the desired conversion option by selecting the corresponding radio button:
   - "Testing Text File": This will create a text file containing the sorted list of image filenames.
   - "PDF Conversion": This will convert the images into a PDF document with selectable DPI options.
   - "Normal Conversion": This will convert the images into a PDF document using the default DPI of 300.
6. If you select "PDF Conversion," you can further choose the DPI option (Screen, Ebook, or Prepress) from the nested radio buttons.
7. Click the "Convert" button to start the conversion process.
8. If you choose "Testing Text File" or "Normal Conversion," a file dialog will prompt you to select the destination where the converted PDF will be saved.
9. If you choose "PDF Conversion," a file dialog will prompt you to select the DPI option, and then another file dialog will prompt you to select the destination for the converted PDF.
10. After successful conversion, a message box will display the result ("Files stored in img_files.txt" or "Images converted to PDF successfully").
11. If any errors or issues occur during the conversion process, warning message boxes will appear to notify you.

## License

This project is licensed under the [MIT License](LICENSE).

## Contribution

Contributions to this project are welcome. If you find any issues or have improvements to suggest, feel free to open a pull request or submit an issue.

## Contact

For any questions or inquiries, you can contact the project maintainer at [email@proton.me](mailto:oprrnazoro@proton.me).
