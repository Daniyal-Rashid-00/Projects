import subprocess
import os
import sys

def ppt_to_pdf(input_path, output_dir=None):
    # 👇 Use your exact LibreOffice path
    soffice = r"F:\Software\Libra office\program\soffice.exe"

    # Verify the path actually exists
    if not os.path.exists(soffice):
        raise FileNotFoundError(f"LibreOffice not found at {soffice}")

    # Normalize paths
    input_path = os.path.abspath(input_path)
    if output_dir is None:
        output_dir = os.path.dirname(input_path)
    else:
        os.makedirs(output_dir, exist_ok=True)

    # Run LibreOffice in headless mode to convert
    cmd = [soffice, "--headless", "--convert-to", "pdf", "--outdir", output_dir, input_path]
    subprocess.run(cmd, check=True)

    pdf_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_path))[0] + ".pdf")
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ppt_to_pdf.py <file_or_folder>")
        sys.exit(1)

    target = sys.argv[1]
    if os.path.isdir(target):
        for file in os.listdir(target):
            if file.lower().endswith((".ppt", ".pptx")):
                full_path = os.path.join(target, file)
                try:
                    pdf_file = ppt_to_pdf(full_path, target)
                    print(f"✅ Converted: {file} → {os.path.basename(pdf_file)}")
                except Exception as e:
                    print(f"❌ Failed: {file} ({e})")
    else:
        try:
            pdf_file = ppt_to_pdf(target)
            print(f"✅ Converted: {os.path.basename(target)} → {os.path.basename(pdf_file)}")
        except Exception as e:
            print(f"❌ Error: {e}")
