# NOVELLE — Elementor Global Design System Blueprint

This document specifies the exact **Global Design System** for NOVELLE, tailored for a **sophisticated editorial luxury-fashion aesthetic** without excessive shadows, gradients, or rounded bubble corners.

---

## 1. Global Colors

Navigate to **Elementor > Site Settings > Global Colors**:

| Token Name | Hex Code | Visual Reference / Description | Usage in NOVELLE |
|---|---|---|---|
| **Primary Text** | `#231F1E` | Deep espresso dark brown | Logo, major editorial headings, product prices, dark buttons |
| **Secondary Text** | `#6E6660` | Muted taupe brown | Body copy, about description, testimonial quotes, contact details |
| **Background (Main)** | `#FAF7F2` | Warm ivory / cream | Whole page background, navbar background, testimonial cards background |
| **Secondary Areas** | `#F2ECE1` | Soft beige / subtle warm tint | Hero backdrop, image placeholders |
| **Warm Banner** | `#836754` | Terracotta / bronze taupe | "The New Season" banner background |
| **Accent** | `#665549` | Deep warm taupe | "Shop Collection", "Add to Cart", "Send Message" buttons, filter pill active state |
| **Accent Tan** | `#C8B8A6` | Warm sand / tan | Subtle divider lines, hover accents |
| **Dark Footer** | `#221E1C` | Rich dark espresso brown | Full-width footer section |
| **Borders** | `#E5DFD6` | Subtle light warm hairline | Product card borders, testimonial borders, newsletter input borders |
| **Subtle Borders** | `#ECE7E0` | Ultra-light header divider | Header bottom hairline border |
| **Section Labels** | `#948B83` | Light warm grey-brown | Small uppercase subtitles ("SHOP", "ABOUT US", "GET IN TOUCH") |
| **Star Rating** | `#B99156` | Refined warm champagne gold | 5-star review icons |

---

## 2. Global Typography

Navigate to **Elementor > Site Settings > Global Fonts**:

### Headings (Serif — *Cormorant Garamond*)
| Token Name | Font Family | Size | Weight | Line Height | Letter Spacing | Transform |
|---|---|---|---|---|---|---|
| **Hero Heading** | `Cormorant Garamond` | 64px (Desktop) / 40px (Mobile) | 400 | 1.05 | 2.5px (0.04em) | Uppercase |
| **Section Headings (H2)** | `Cormorant Garamond` | 36px–40px | 400 | 1.15 | 2px (0.05em) | Uppercase |
| **Card / Category (H3)** | `Cormorant Garamond` | 22px | 500 | 1.2 | 1.5px (0.06em) | Uppercase |
| **Stat Numbers** | `Cormorant Garamond` | 38px | 400 | 1.1 | 0px | Normal |

### UI & Body (Sans-Serif — *Inter*)
| Token Name | Font Family | Size | Weight | Line Height | Letter Spacing | Transform |
|---|---|---|---|---|---|---|
| **Section Label** | `Inter` | 11px | 500 | 1.4 | 2.5px (0.22em) | Uppercase |
| **Navigation** | `Inter` | 12.5px | 500 | 1.2 | 1.8px (0.12em) | Uppercase |
| **Buttons** | `Inter` | 12px | 500 | 1.2 | 2.2px (0.18em) | Uppercase |
| **Body Copy** | `Inter` | 15px | 300 | 1.65 | 0.2px | Normal |
| **Product Titles** | `Inter` | 13px | 400 | 1.4 | 0.4px | Normal |
| **Product Prices** | `Inter` | 14px | 600 | 1.2 | 0.2px | Normal |
| **Footer Links** | `Inter` | 13px | 300 | 2.0 | 0.5px | Normal |

---

## 3. Strict Editorial Aesthetic Rules (No Bubble / Shadow Overload)

1. **Border Radius**:
   - Buttons: `0px` to `2px` max (crisp tailored rectangles).
   - Product / Category Cards: `0px` (flat editorial edges).
   - Testimonial Cards: `0px` to `2px`.
   - Category Filter Pills: Capsule (`9999px`) only on filter pills as shown in template.
2. **Shadows**:
   - `none` or ultra-subtle ambient shadow (`0 4px 20px rgba(0, 0, 0, 0.03)`).
   - Absolutely NO heavy blurred drop-shadows.
3. **Borders**:
   - Hairline borders: `1px solid #E5DFD6`.
4. **Dividers**:
   - 1px crisp horizontal divider rules (`#E5DFD6`) next to section titles and above stats.

---

## 4. Elementor Custom CSS (Paste in Site Settings > Custom CSS)

```css
/* ==========================================================================
   NOVELLE Luxury Fashion - Editorial Refinements
   ========================================================================== */

/* Typography Overrides */
.novelle-serif,
.elementor-widget-heading h1,
.elementor-widget-heading h2 {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-weight: 400;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

/* Hairline borders */
.novelle-border {
  border: 1px solid #E5DFD6 !important;
}

/* Subtle editorial hover */
.novelle-hover-lift {
  transition: transform 0.3s ease, border-color 0.3s ease;
}
.novelle-hover-lift:hover {
  transform: translateY(-3px);
  border-color: #C8B8A6 !important;
}

/* Form inputs */
.elementor-field-group .elementor-field-textual {
  background: transparent !important;
  border: 1px solid #E5DFD6 !important;
  border-radius: 0px !important;
  color: #231F1E !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 13px !important;
  padding: 12px 16px !important;
}
.elementor-field-group .elementor-field-textual:focus {
  border-color: #665549 !important;
  outline: none !important;
}

/* Clean Button Styling */
.elementor-button {
  border-radius: 0px !important;
  font-family: 'Inter', sans-serif !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  font-weight: 500 !important;
}
```
