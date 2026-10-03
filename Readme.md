# Indian E-Newspaper Advertisement Detection

## Overview

This project focuses on detecting advertisements in Indian e-newspapers and extracting structured information from the detected advertisements.

The project is being developed as a proof of concept (POC) using newspaper pages from Indian e-newspapers. The initial POC focuses on **The Times of India (TOI)**, with plans to extend the dataset to additional newspapers such as **The Hindu** and **Dainik Jagran**.

The overall objective is to identify advertisements on newspaper pages, isolate individual advertisements, and eventually extract information such as company and product names.

---

# Proof of Concept (POC)

## POC Objective

The initial POC is designed to verify whether advertisements can be reliably localized within Indian e-newspaper pages using annotated newspaper-page data.

The POC currently focuses on:

- The Times of India (TOI)
- Advertisement localization
- Bounding-box based annotations
- Different advertisement sizes and layouts
- Pages containing multiple advertisements
- Pages containing no advertisements

The POC uses a single advertisement class:

```text
0 = advertisement

data/
├── raw/
│   ├── toi/
│   ├── the_hindu/
│   └── dainik_jagran/
│
├── pages/
│   ├── toi/
│   ├── the_hindu/
│   └── dainik_jagran/
│
└── yolo_dataset/
    ├── images/
    │   ├── train/
    │   ├── val/
    │   └── test/
    │
    └── labels/
        ├── train/
        ├── val/
        └── test/