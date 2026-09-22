# NOVELLE — WordPress & Elementor Master Implementation Guide

This guide provides the complete blueprint and 1-click import instructions to build the **NOVELLE** luxury fashion e-commerce website using **native Elementor Flexbox Containers and Widgets**, exactly reproducing the visual reference.

---

## 1. Quick 1-Click Import

Two ready-to-import Elementor templates are available in the repository:
1. 📁 **`elementor/novelle-elementor-template.json`** — Complete 10-section homepage template.
2. 📁 **`elementor/novelle-product-card-template.json`** — Reusable WooCommerce Product Card (Loop Item) template with minimal editorial borders, image zoom hover, wishlist heart toggle, and sharp rectangular ADD TO CART button.

### Import Steps:
1. Log in to your WordPress Dashboard.
2. Ensure **Elementor** (and **Elementor Pro** if using WooCommerce Loop Builder) is installed and active.
3. Enable **Flexbox Container** in *Elementor > Settings > Features > Flexbox Container* (Active by default in modern Elementor).
4. Navigate to **Templates > Saved Templates > Import Templates**.
5. Choose and upload `novelle-elementor-template.json` and `novelle-product-card-template.json`.
6. Create a new Page (e.g. "Home"), click **Edit with Elementor**, click the **Folder icon (Add Template)**, select the **My Templates** tab, and insert **"NOVELLE - Luxury Fashion Homepage"**.
7. In the Featured Collection section, use Elementor's **Loop Grid** widget and select **"NOVELLE - Reusable WooCommerce Product Card"** as the template to dynamically output WooCommerce products.

---

## 2. Elementor Site Settings (Global Styles)

Configure these in **Site Settings** (hamburger icon on the top-left of the Elementor panel) to ensure complete consistency:

### Global Colors
| Color Token | Hex Code | Purpose |
|---|---|---|
| **Primary** | `#221E1C` | Logo, main headlines, dark buttons, dark footer |
| **Secondary** | `#665549` | Buttons, badge accents, hover states |
| **Text** | `#6E6660` | Body copy, descriptions |
| **Accent** | `#C8B8A6` | Subtle accents, dividers, highlights |
| **Background Main** | `#FAF7F2` | Warm sand/cream page background |
| **Border Color** | `#E5DFD6` | Subtle card borders and horizontal rules |
| **Star Rating** | `#B99156` | Review stars |

### Global Fonts
- **Primary / Headings**: `Cormorant Garamond` (Serif)
  - H1: 64px (Desktop), 40px (Mobile), Letter-spacing: 0.04em, Line-height: 1.05
  - H2: 36px–40px, Letter-spacing: 0.05em, Line-height: 1.15
  - H3: 20px–22px, Letter-spacing: 0.06em
- **Secondary / Body**: `Inter` (Sans-Serif)
  - Body Normal: 15px, Line-height: 1.65, Font weight: 300 / 400
  - Buttons / Labels: 12px–13px, Letter-spacing: 2px–3px, Uppercase, Weight: 500

---

## 3. Supplied Original Images Reference Table

All images are placed in **`assets/images/`**:

| Section | Image File | Media Library Recommended Title | Dimensions |
|---|---|---|---|
| **Hero Campaign** | `assets/images/hero.jpg` | `novelle-hero-campaign` | 1024×572 |
| **Product 1** | `assets/images/prod_1.jpg` | `novelle-linen-midi-dress` | 1024×1024 (₹4,990) |
| **Product 2** | `assets/images/prod_2.jpg` | `novelle-tailored-warm` | 1024×1024 (₹5,190) |
| **Product 3** | `assets/images/prod_3.jpg` | `novelle-knit-top` | 1024×1024 (₹2,990) |
| **Product 4** | `assets/images/prod_4.jpg` | `novelle-wide-leg-trousers` | 1024×1024 (₹3,490) |
| **Product 5** | `assets/images/prod_5.jpg` | `novelle-shirt-dress` | 1024×1024 (₹4,490) |
| **Product 6** | `assets/images/prod_6.png` | `novelle-knit-sweater` | Reference crop (₹3,990) |
| **About Us** | `assets/images/about.jpg` | `novelle-about-tailored-blazer` | 1024×572 high-resolution |
| **New Season** | `assets/images/new_season.png` | `novelle-new-season-banner` | Campaign visual |
| **Category 1** | `assets/images/cat_dresses.png` | `novelle-cat-dresses` | Dresses ("Grace in every step") |
| **Category 2** | `assets/images/cat_tailoring.png`| `novelle-cat-tailoring` | Tailoring ("Power in simplicity") |
| **Category 3** | `assets/images/cat_essentials.png`| `novelle-cat-essentials` | Essentials ("Everyday must-haves") |
| **Avatar 1** | `assets/images/avatar_1.png` | `novelle-testimonial-ananya` | Ananya R. |
| **Avatar 2** | `assets/images/avatar_2.png` | `novelle-testimonial-sneha` | Sneha R. |
| **Avatar 3** | `assets/images/avatar_3.png` | `novelle-testimonial-meera` | Meera S. |
| **Contact** | `assets/images/contact.png` | `novelle-contact-lifestyle` | Lifestyle model with coffee |

---

## 4. Widget & Container Hierarchy (Key Sections)

### Section 3: Featured Collection & Reusable Product Card
- **Parent Container**: Boxed, Padding: 80px 40px, Background: `#FAF7F2`.
  - **Header Row Container (Flex Row, Space-Between, Align: Center)**:
    - Left: Subtitle "SHOP" (12px, `#948B83`), Title "FEATURED COLLECTION" (36px, Cormorant Garamond)
    - Right: Category Filter Pills ("All" active `#665549`, "Dresses", "Tops", "Bottoms", "Outerwear", "Accessories")
  - **Loop Grid / Product Grid Container**:
    - Uses **`novelle-product-card-template.json`**:
      1. **Image Box Container** (`aspect-ratio: 3/4`, overflow hidden):
         - Product Featured Image widget with hover zoom (`transform: scale(1.045)`).
         - Upper-right Wishlist Icon Button (`position: absolute; top: 8px; right: 8px; width: 30px; height: 30px; border-radius: 50%`) with white hover and red heart fill.
      2. **Product Name**: 13px Inter, 400 weight, `#221E1C`.
      3. **Price**: 14px Inter, 600 bold, `#221E1C`.
      4. **ADD TO CART Button**: Rectangular, flat zero border-radius (`border-radius: 0px`), 11px uppercase, 2px letter-spacing, background `#665549`, hover `#554438`. Touch-optimized min-height (42px) on mobile.

### Section 4: About Us Section
- **Parent Container**: Boxed, Flex Row, Align: Center, Gap: 60px, Padding: 80px 40px.
  - **Left Container (Width: 48% Desktop, 100% Mobile — Order 1)**:
    - Image Widget: `assets/images/about.jpg` (High-res supplied image of model in camel blazer).
    - Image proportions: `aspect-ratio: 4 / 3.4` (Desktop) / `16 / 10` (Mobile), `object-fit: cover`.
  - **Right Container (Width: 48% Desktop, 100% Mobile — Order 2)**:
    - Subtitle / Label: "ABOUT US" (12px, `#948B83`, uppercase, letter-spacing: 2px).
    - Heading: "CRAFTED FOR YOUR<br>SIGNATURE STYLE" (40px, Cormorant Garamond, line-height: 1.15).
    - Text: Editorial description paragraph in `#6E6660`, 15px, line-height 1.75.
    - **Statistics Container (Flex Row, Border-top: 1px `#E5DFD6`, Padding-top: 25px)**:
      - Counter 1: **12+** / Collections
      - Counter 2: **8K+** / Happy Customers
      - Counter 3: **100%** / Curated Style
      - Mobile: Forms a compact, responsive 3-column row with centered stat values and labels.

### Section 5: New Season Banner
- **Parent Container**: Full Width, Flex Row, Background: `#836754`.
  - **Left Container (Width: 50%, Padding: 70px 80px)**:
    - Heading: "THE NEW SEASON" (44px, Cormorant Garamond, White)
    - Text: "Fresh styles. Timeless pieces. A new chapter in your wardrobe."
    - Button: "DISCOVER COLLECTION →" (White outline)
  - **Right Container (Width: 50%)**:
    - Image Widget: `new_season.png`

### Section 6: Categories
- **Parent Container**: Boxed, Padding: 80px 40px.
  - Header Row with Subtitle "SHOP BY", Title "CATEGORIES", and "VIEW ALL →" link.
  - **Categories Container (Flex Row, Gap: 24px)**:
    - Card 1: `cat_dresses.png`, Heading: "DRESSES", Caption: "Grace in every step →"
    - Card 2: `cat_tailoring.png`, Heading: "TAILORING", Caption: "Power in simplicity →"
    - Card 3: `cat_essentials.png`, Heading: "ESSENTIALS", Caption: "Everyday must-haves →"

### Section 7: Testimonials
- **Parent Container**: Boxed, Padding: 80px 40px.
  - Header Row with Title "WHAT OUR CUSTOMERS SAY" and "VIEW ALL →".
  - **Review Cards Container (Flex Row, Gap: 24px)**:
    - 3 Cards (Border: 1px `#E5DFD6`, Padding: 28px):
      - Avatar image (`avatar_1.png`, etc.)
      - Name ("Ananya R.", "Sneha R.", "Meera S.")
      - Star Rating Widget: 5 Stars (`#B99156`)
      - Quote text in italics

### Section 8: Contact Section
- **Parent Container**: Boxed, Flex Row, Align: Center, Gap: 40px, Padding: 80px 40px.
  - **Left Container (Width: 30%)**: Image `contact.png`.
  - **Middle Container (Width: 45%)**:
    - Subtitle "GET IN TOUCH", Heading "CONTACT US", Text.
    - Form Widget: Name, Email, Message, Submit Button "SEND MESSAGE →".
  - **Right Container (Width: 25%)**:
    - Icon Box 1: Envelope icon, Email `hello@novelle.com`
    - Icon Box 2: Phone icon, `+91 98765 43210`
    - Icon Box 3: Map Marker icon, `123 Fashion Street, Bangalore, India - 560001`

### Section 9: Newsletter Section
- **Parent Container**: Boxed, Flex Column, Align: Center, Text-align: Center, Padding: 70px 40px.
  - Subtitle "STAY UPDATED"
  - Title "JOIN THE NOVELLE CIRCLE"
  - Description
  - Form Widget (Inline): Email input + Submit Button "SUBSCRIBE →" (`#221E1C`)

### Section 10: Footer
- **Parent Container**: Boxed, Background: `#221E1C`, Text: `#FAF7F2`, Padding: 80px 40px 40px.
  - **Top Row (Flex Row, Space-Between)**:
    - Col 1: Brand "NOVELLE" + Tagline "Style · Quality · You"
    - Col 2: SHOP links (New Arrivals, Dresses, Tops, Bottoms, Accessories)
    - Col 3: ABOUT links (Our Story, Sustainability, Careers, Blog)
    - Col 4: HELP links (Shipping, Returns, Size Guide, FAQs)
    - Col 5: CONTACT (Email, Phone, Bangalore address, Social Icons)
  - **Bottom Row (Flex Row, Space-Between, Border-top: 1px `#3D3531`)**:
    - Left: "© 2026 Novelle. All rights reserved."
    - Right: Payment badges (VISA, Mastercard, RuPay, PayPal)

---

## 5. Responsive Behavior Breakdown
- **Desktop (1200px+)**: Multi-column layouts (3 hero panels, 6 products row, 3 categories, 3 testimonials, 3 contact columns, 5 footer columns).
- **Laptop (1024px)**: 3 products per row, contact image hidden or stacked, 3 footer columns.
- **Tablet (768px)**: 2 products per row, hero single panel, categories stacked, testimonials stacked, contact single column.
- **Mobile (375px–480px)**: 1 product per row, hamburger menu navigation, full-width buttons and forms.
