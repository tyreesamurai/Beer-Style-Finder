from pypdf import PdfReader

reader = PdfReader("Brew_Your_Own_Beer_Impress_your_friends.pdf")

for page in reader.pages:
    print(page.extract_text())
