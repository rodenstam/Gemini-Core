import markdown
from xhtml2pdf import pisa
from pathlib import Path

class PDFGenerator:
    """A shared tool to convert Markdown to professional PDF documents."""
    
    @staticmethod
    def get_default_css():
        return """
        @page {
            size: a4;
            margin: 2cm;
        }
        body {
            font-family: Helvetica, Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.5;
            color: #333;
        }
        h1 {
            font-size: 24pt;
            color: #2c3e50;
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 5pt;
            margin-bottom: 20pt;
        }
        h2 {
            font-size: 18pt;
            color: #2c3e50;
            margin-top: 20pt;
            border-bottom: 1px solid #ccc;
        }
        h3 {
            font-size: 14pt;
            color: #34495e;
        }
        p { margin-bottom: 10pt; }
        ul { margin-bottom: 10pt; }
        li { margin-bottom: 5pt; }
        hr { border: 0; border-top: 1px solid #ccc; margin: 20pt 0; }
        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            text-align: center;
            font-size: 9pt;
            color: #999;
        }
        """

    def generate(self, md_content, output_pdf_path, title="Dokument"):
        """Converts markdown text to a PDF file."""
        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'smarty'])
        
        # Wrap in a full HTML structure with CSS
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>{self.get_default_css()}</style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Create the PDF
        with open(output_pdf_path, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)
            
        return not pisa_status.err

if __name__ == "__main__":
    # Test the generator
    gen = PDFGenerator()
    test_md = "# Test\nDetta är en **test-PDF** skapad via Python."
    gen.generate(test_md, "test_output.pdf")
    print("Test-PDF skapad!")
