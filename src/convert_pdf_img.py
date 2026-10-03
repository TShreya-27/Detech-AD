from pathlib import Path
import fitz
import re


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


RAW_DIR = Path("D:\\detect-ad\\detect-ad\\data\\raw")
PAGES_DIR = Path("D:\\detect-ad\\detect-ad\\data\\pages")


NEWSPAPERS = [
    "toi",
    "dainik_jagran",
    "the_hindu"
]


# ============================================================
# CLEAN ISSUE NAME
# ============================================================

def clean_name(filename):
    """
    Convert PDF filename into a clean folder name.

    Example:
        TOI 20-09-2026.pdf
        →
        TOI_20-09-2026
    """

    name = Path(filename).stem

    name = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        name
    )

    return name


# ============================================================
# CONVERT ONE PDF
# ============================================================

def convert_pdf(pdf_path, output_dir):

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    print("\n===================================")
    print(f"Processing: {pdf_path.name}")
    print("===================================")

    try:

        doc = fitz.open(pdf_path)

        total_pages = len(doc)

        print(f"Total pages: {total_pages}")

        for page_number, page in enumerate(
            doc,
            start=1
        ):

            output_file = (
                output_dir /
                f"page_{page_number:03d}.jpg"
            )

            # Render page 400 DPI
            pix = page.get_pixmap(
                dpi=400,
                alpha=False
            )

            pix.save(output_file)

            print(
                f"  Saved page {page_number}/{total_pages}"
            )

        doc.close()

        print("Finished:", pdf_path.name)

    except Exception as e:

        print(
            f"ERROR processing {pdf_path.name}: {e}"
        )


# ============================================================
# PROCESS ONE NEWSPAPER
# ============================================================

def process_newspaper(newspaper):

    input_dir = RAW_DIR / newspaper
    output_dir = PAGES_DIR / newspaper

    if not input_dir.exists():

        print(
            f"\nWARNING: Folder not found: {input_dir}"
        )

        return

    pdf_files = sorted(
        input_dir.glob("*.pdf")
    )

    print("\n")
    print("###################################")
    print(f"NEWSPAPER: {newspaper}")
    print(f"PDFs found: {len(pdf_files)}")
    print("###################################")

    for pdf_file in pdf_files:

        # Each PDF gets its own folder
        issue_name = clean_name(
            pdf_file.name
        )

        issue_output_dir = (
            output_dir / issue_name
        )

        convert_pdf(
            pdf_file,
            issue_output_dir
        )


# ============================================================
# MAIN
# ============================================================

def main():

    print("\nStarting PDF → page conversion...\n")

    for newspaper in NEWSPAPERS:

        process_newspaper(
            newspaper
        )

    print("\n===================================")
    print("ALL PDFs PROCESSED")
    print("===================================")


if __name__ == "__main__":
    main()