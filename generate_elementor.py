import json
import uuid
import os

def uid():
    return uuid.uuid4().hex[:7]

elementor_data = {
    "version": "0.4",
    "title": "NOVELLE - Luxury Fashion Homepage",
    "type": "page",
    "page_settings": {
        "page_template": "elementor_header_footer",
        "template": "elementor_header_footer",
        "custom_css": "/* NOVELLE Luxury Theme Custom CSS */\n.novelle-font-serif { font-family: 'Cormorant Garamond', serif !important; }\n.novelle-card { transition: all 0.3s ease; }\n.novelle-card:hover { transform: translateY(-4px); }"
    },
    "content": [
        # 1. Header
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "flex_direction": "row",
                "flex_justify_content": "space-between",
                "flex_align_items": "center",
                "background_background": "classic",
                "background_color": "#FAF7F2",
                "padding": {"unit": "px", "top": "18", "bottom": "18", "left": "40", "right": "40"},
                "border_border": "solid",
                "border_width": {"unit": "px", "top": "0", "bottom": "1", "left": "0", "right": "0"},
                "border_color": "#ECE7E0"
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_gap": {"unit": "px", "size": 32}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": '<a href="#home" style="color:#221E1C;text-decoration:none;font-size:13px;letter-spacing:2px;font-weight:600;border-bottom:2px solid #221E1C;padding-bottom:4px;">HOME</a>'}},
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": '<a href="#shop" style="color:#221E1C;text-decoration:none;font-size:13px;letter-spacing:2px;">SHOP</a>'}},
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": '<a href="#collections" style="color:#221E1C;text-decoration:none;font-size:13px;letter-spacing:2px;">COLLECTIONS</a>'}}
                    ]
                },
                {
                    "id": uid(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "NOVELLE",
                        "align": "center",
                        "typography_typography": "custom",
                        "typography_font_family": "Cormorant Garamond",
                        "typography_font_size": {"unit": "px", "size": 38},
                        "typography_letter_spacing": {"unit": "px", "size": 8},
                        "title_color": "#221E1C"
                    }
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_align_items": "center", "flex_gap": {"unit": "px", "size": 24}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": '<a href="#about" style="color:#221E1C;text-decoration:none;font-size:13px;letter-spacing:2px;">ABOUT</a>'}},
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": '<a href="#contact" style="color:#221E1C;text-decoration:none;font-size:13px;letter-spacing:2px;">CONTACT</a>'}},
                        {"id": uid(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fas fa-search", "library": "fa-solid"}, "size": {"unit": "px", "size": 16}, "primary_color": "#221E1C"}},
                        {"id": uid(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "far fa-user", "library": "fa-regular"}, "size": {"unit": "px", "size": 16}, "primary_color": "#221E1C"}},
                        {"id": uid(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fas fa-shopping-bag", "library": "fa-solid"}, "size": {"unit": "px", "size": 16}, "primary_color": "#221E1C"}}
                    ]
                }
            ]
        },
        # 2. Hero Section
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "full",
                "flex_direction": "row",
                "padding": {"unit": "px", "top": "0", "bottom": "0", "left": "0", "right": "0"},
                "position": "relative",
                "min_height": {"unit": "px", "size": 680},
                "background_background": "classic",
                "background_image": {"url": "assets/images/hero.jpg"},
                "background_position": "center center",
                "background_size": "cover"
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {
                        "flex_direction": "column",
                        "position": "absolute",
                        "z_index": 10,
                        "top": "22%",
                        "left": "6%",
                        "max_width": {"unit": "px", "size": 480},
                        "border_border": "solid",
                        "border_width": {"unit": "px", "top": "0", "bottom": "0", "left": "1", "right": "0"},
                        "border_color": "rgba(255,255,255,0.45)",
                        "padding": {"unit": "px", "top": "0", "bottom": "0", "left": "24", "right": "0"}
                    },
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "THE ART OF", "title_color": "#FFFFFF", "typography_font_size": {"unit": "px", "size": 13}, "typography_letter_spacing": {"unit": "px", "size": 3.5}}},
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "EVERYDAY<br>ELEGANCE", "title_color": "#FFFFFF", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 64}, "typography_line_height": {"unit": "em", "size": 1.05}}},
                        {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#FAF7F2;opacity:0.9;font-size:15px;margin-bottom:28px;">Timeless pieces for modern women. Effortless style, every day.</p>'}},
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"flex_direction": "row", "flex_gap": {"unit": "px", "size": 16}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "SHOP COLLECTION  →", "link": {"url": "#shop"}, "background_color": "#665549", "button_text_color": "#FFFFFF"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "EXPLORE LOOKS", "link": {"url": "#categories"}, "background_color": "transparent", "border_border": "solid", "border_width": {"unit": "px", "size": 1}, "border_color": "#FFFFFF", "button_text_color": "#FFFFFF"}}
                            ]
                        }
                    ]
                }
            ]
        },
        # 3. Featured Collection
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "padding": {"unit": "px", "top": "80", "bottom": "80", "left": "40", "right": "40"},
                "background_color": "#FAF7F2"
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_justify_content": "space-between", "flex_align_items": "center", "margin": {"unit": "px", "bottom": "40"}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "container",
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "SHOP", "typography_font_size": {"unit": "px", "size": 12}, "title_color": "#948B83"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "FEATURED COLLECTION", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 36}, "title_color": "#221E1C"}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"flex_direction": "row", "flex_gap": {"unit": "px", "size": 8}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "All", "background_color": "#665549", "button_text_color": "#FFF"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "Dresses", "background_color": "transparent", "button_text_color": "#6E6660"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "Tops", "background_color": "transparent", "button_text_color": "#6E6660"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "Bottoms", "background_color": "transparent", "button_text_color": "#6E6660"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "Outerwear", "background_color": "transparent", "button_text_color": "#6E6660"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "Accessories", "background_color": "transparent", "button_text_color": "#6E6660"}}
                            ]
                        }
                    ]
                },
                # Product Grid 6 cards
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": {"unit": "px", "size": 20}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 15.5}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/prod_1.jpg"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Linen Midi Dress", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "₹ 4,990", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C", "typography_font_weight": "bold"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "ADD TO CART", "background_color": "#665549", "button_text_color": "#FFFFFF"}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 15.5}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/prod_2.jpg"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Tailored Warm", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "₹ 5,190", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C", "typography_font_weight": "bold"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "ADD TO CART", "background_color": "#665549", "button_text_color": "#FFFFFF"}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 15.5}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/prod_3.jpg"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Knit Top", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "₹ 2,990", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C", "typography_font_weight": "bold"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "ADD TO CART", "background_color": "#665549", "button_text_color": "#FFFFFF"}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 15.5}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/prod_4.jpg"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Wide Leg Trousers", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "₹ 3,490", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C", "typography_font_weight": "bold"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "ADD TO CART", "background_color": "#665549", "button_text_color": "#FFFFFF"}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 15.5}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/prod_5.jpg"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Shirt Dress", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "₹ 4,490", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C", "typography_font_weight": "bold"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "ADD TO CART", "background_color": "#665549", "button_text_color": "#FFFFFF"}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 15.5}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/prod_6.png"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Knit Sweater", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "₹ 3,990", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C", "typography_font_weight": "bold"}},
                                {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "ADD TO CART", "background_color": "#665549", "button_text_color": "#FFFFFF"}}
                            ]
                        }
                    ]
                }
            ]
        },
        # 4. About Section
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "flex_direction": "row",
                "flex_align_items": "center",
                "padding": {"unit": "px", "top": "80", "bottom": "80", "left": "40", "right": "40"},
                "flex_gap": {"unit": "px", "size": 60}
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"width": {"unit": "%", "size": 48}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/about.png"}}}
                    ]
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"width": {"unit": "%", "size": 48}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "ABOUT US", "typography_font_size": {"unit": "px", "size": 12}, "title_color": "#948B83"}},
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "CRAFTED FOR YOUR<br>SIGNATURE STYLE", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 40}, "title_color": "#221E1C"}},
                        {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#6E6660;line-height:1.75;font-size:15px;margin-bottom:35px;">At Novelle, we believe fashion is more than just what you wear — it\'s how you feel. Our collections are thoughtfully curated for modern women who value quality, comfort and timeless elegance. From everyday essentials to statement pieces, we bring you styles that make you feel confident, effortless and uniquely you.</p>'}},
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"flex_direction": "row", "flex_justify_content": "space-between", "border_border": "solid", "border_width": {"unit": "px", "top": "1", "bottom": "0", "left": "0", "right": "0"}, "border_color": "#E5DFD6", "padding": {"unit": "px", "top": "25"}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "counter", "settings": {"starting_number": 0, "ending_number": 12, "suffix": "+", "title": "Collections", "number_color": "#221E1C", "title_color": "#948B83"}},
                                {"id": uid(), "elType": "widget", "widgetType": "counter", "settings": {"starting_number": 0, "ending_number": 8, "suffix": "K+", "title": "Happy Customers", "number_color": "#221E1C", "title_color": "#948B83"}},
                                {"id": uid(), "elType": "widget", "widgetType": "counter", "settings": {"starting_number": 0, "ending_number": 100, "suffix": "%", "title": "Curated Style", "number_color": "#221E1C", "title_color": "#948B83"}}
                            ]
                        }
                    ]
                }
            ]
        },
        # 5. New Season Banner
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "full",
                "flex_direction": "row",
                "background_color": "#836754",
                "padding": {"unit": "px", "top": "0", "bottom": "0", "left": "0", "right": "0"}
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"width": {"unit": "%", "size": 50}, "padding": {"unit": "px", "top": "70", "bottom": "70", "left": "80", "right": "40"}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "THE NEW SEASON", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 44}, "title_color": "#FFFFFF"}},
                        {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#FFFFFF;opacity:0.9;font-size:15px;margin-bottom:30px;">Fresh styles. Timeless pieces. A new chapter in your wardrobe.</p>'}},
                        {"id": uid(), "elType": "widget", "widgetType": "button", "settings": {"text": "DISCOVER COLLECTION  →", "link": {"url": "#categories"}, "background_color": "transparent", "border_border": "solid", "border_width": {"unit": "px", "size": 1}, "border_color": "#FFFFFF", "button_text_color": "#FFFFFF"}}
                    ]
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"width": {"unit": "%", "size": 50}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/new_season.jpg"}}}
                    ]
                }
            ]
        },
        # 6. Categories
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "padding": {"unit": "px", "top": "80", "bottom": "80", "left": "40", "right": "40"}
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_justify_content": "space-between", "flex_align_items": "center", "margin": {"unit": "px", "bottom": "35"}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "container",
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "SHOP BY", "typography_font_size": {"unit": "px", "size": 12}, "title_color": "#948B83"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "CATEGORIES", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 36}, "title_color": "#221E1C"}}
                            ]
                        },
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": '<a href="#shop" style="color:#221E1C;text-decoration:none;font-size:12px;letter-spacing:2px;">VIEW ALL  →</a>'}}
                    ]
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_gap": {"unit": "px", "size": 24}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 33}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/cat_dresses.png"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "DRESSES", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 22}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#6E6660;font-size:13px;">Grace in every step →</p>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 33}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/cat_tailoring.png"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "TAILORING", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 22}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#6E6660;font-size:13px;">Power in simplicity →</p>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 33}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/cat_essentials.png"}}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "ESSENTIALS", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 22}, "title_color": "#221E1C"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#6E6660;font-size:13px;">Everyday must-haves →</p>'}}
                            ]
                        }
                    ]
                }
            ]
        },
        # 7. Testimonials
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "padding": {"unit": "px", "top": "80", "bottom": "80", "left": "40", "right": "40"}
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_justify_content": "space-between", "flex_align_items": "center", "margin": {"unit": "px", "bottom": "35"}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "container",
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "TESTIMONIALS", "typography_font_size": {"unit": "px", "size": 12}, "title_color": "#948B83"}},
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "WHAT OUR CUSTOMERS SAY", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 36}, "title_color": "#221E1C"}}
                            ]
                        },
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": '<a href="#testimonials" style="color:#221E1C;text-decoration:none;font-size:12px;letter-spacing:2px;">VIEW ALL  →</a>'}}
                    ]
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_gap": {"unit": "px", "size": 24}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 33}, "border_border": "solid", "border_width": {"unit": "px", "size": 1}, "border_color": "#E5DFD6", "padding": {"unit": "px", "size": 28}},
                            "elements": [
                                {
                                    "id": uid(),
                                    "elType": "container",
                                    "settings": {"flex_direction": "row", "flex_align_items": "center", "flex_gap": {"unit": "px", "size": 14}, "margin": {"unit": "px", "bottom": "16"}},
                                    "elements": [
                                        {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/avatar_1.png"}}},
                                        {
                                            "id": uid(),
                                            "elType": "container",
                                            "elements": [
                                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Ananya R.", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C"}},
                                                {"id": uid(), "elType": "widget", "widgetType": "star-rating", "settings": {"rating_scale": 5, "rating": 5, "star_color": "#B99156"}}
                                            ]
                                        }
                                    ]
                                },
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="font-style:italic;color:#6E6660;font-size:14px;line-height:1.6;">“Absolutely in love with the quality and fit! Novelle has become my favourite go-to for elegant and comfortable outfits.”</p>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 33}, "border_border": "solid", "border_width": {"unit": "px", "size": 1}, "border_color": "#E5DFD6", "padding": {"unit": "px", "size": 28}},
                            "elements": [
                                {
                                    "id": uid(),
                                    "elType": "container",
                                    "settings": {"flex_direction": "row", "flex_align_items": "center", "flex_gap": {"unit": "px", "size": 14}, "margin": {"unit": "px", "bottom": "16"}},
                                    "elements": [
                                        {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/avatar_2.png"}}},
                                        {
                                            "id": uid(),
                                            "elType": "container",
                                            "elements": [
                                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Sneha R.", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C"}},
                                                {"id": uid(), "elType": "widget", "widgetType": "star-rating", "settings": {"rating_scale": 5, "rating": 5, "star_color": "#B99156"}}
                                            ]
                                        }
                                    ]
                                },
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="font-style:italic;color:#6E6660;font-size:14px;line-height:1.6;">“The designs are so unique and classy. I always get compliments whenever I wear something from Novelle!”</p>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 33}, "border_border": "solid", "border_width": {"unit": "px", "size": 1}, "border_color": "#E5DFD6", "padding": {"unit": "px", "size": 28}},
                            "elements": [
                                {
                                    "id": uid(),
                                    "elType": "container",
                                    "settings": {"flex_direction": "row", "flex_align_items": "center", "flex_gap": {"unit": "px", "size": 14}, "margin": {"unit": "px", "bottom": "16"}},
                                    "elements": [
                                        {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/avatar_3.png"}}},
                                        {
                                            "id": uid(),
                                            "elType": "container",
                                            "elements": [
                                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Meera S.", "typography_font_size": {"unit": "px", "size": 14}, "title_color": "#221E1C"}},
                                                {"id": uid(), "elType": "widget", "widgetType": "star-rating", "settings": {"rating_scale": 5, "rating": 5, "star_color": "#B99156"}}
                                            ]
                                        }
                                    ]
                                },
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="font-style:italic;color:#6E6660;font-size:14px;line-height:1.6;">“Beautiful collection, excellent customer service and super fast delivery. Highly recommend!”</p>'}}
                            ]
                        }
                    ]
                }
            ]
        },
        # 8. Contact Section
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "flex_direction": "row",
                "flex_align_items": "center",
                "padding": {"unit": "px", "top": "80", "bottom": "80", "left": "40", "right": "40"},
                "flex_gap": {"unit": "px", "size": 40}
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"width": {"unit": "%", "size": 30}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "image", "settings": {"image": {"url": "assets/images/contact.png"}}}
                    ]
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"width": {"unit": "%", "size": 45}},
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "GET IN TOUCH", "typography_font_size": {"unit": "px", "size": 12}, "title_color": "#948B83"}},
                        {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "CONTACT US", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 36}, "title_color": "#221E1C"}},
                        {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#6E6660;font-size:14px;margin-bottom:20px;">We\'d love to hear from you. Whether you have a question, feedback or need assistance, our team is here to help.</p>'}},
                        {
                            "id": uid(),
                            "elType": "widget",
                            "widgetType": "form",
                            "settings": {
                                "form_name": "NOVELLE Contact Form",
                                "form_fields": [
                                    {"field_type": "text", "field_label": "Name", "placeholder": "Name *", "required": "true", "width": "50"},
                                    {"field_type": "email", "field_label": "Email", "placeholder": "Email *", "required": "true", "width": "50"},
                                    {"field_type": "textarea", "field_label": "Message", "placeholder": "Message *", "required": "true", "width": "100"}
                                ],
                                "button_text": "SEND MESSAGE  →",
                                "button_background_color": "#665549",
                                "button_text_color": "#FFFFFF"
                            }
                        }
                    ]
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"width": {"unit": "%", "size": 25}, "flex_direction": "column", "flex_gap": {"unit": "px", "size": 25}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "widget",
                            "widgetType": "icon-box",
                            "settings": {
                                "selected_icon": {"value": "far fa-envelope", "library": "fa-regular"},
                                "title_text": "Email",
                                "description_text": '<a href="mailto:hello@novelle.com" style="color:#6E6660;text-decoration:none;">hello@novelle.com</a>',
                                "primary_color": "#665549"
                            }
                        },
                        {
                            "id": uid(),
                            "elType": "widget",
                            "widgetType": "icon-box",
                            "settings": {
                                "selected_icon": {"value": "fas fa-phone-alt", "library": "fa-solid"},
                                "title_text": "Phone",
                                "description_text": '<a href="tel:+919876543210" style="color:#6E6660;text-decoration:none;">+91 98765 43210</a>',
                                "primary_color": "#665549"
                            }
                        },
                        {
                            "id": uid(),
                            "elType": "widget",
                            "widgetType": "icon-box",
                            "settings": {
                                "selected_icon": {"value": "fas fa-map-marker-alt", "library": "fa-solid"},
                                "title_text": "Location",
                                "description_text": "123 Fashion Street,<br>Bangalore, India - 560001",
                                "primary_color": "#665549"
                            }
                        }
                    ]
                }
            ]
        },
        # 9. Newsletter Section
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "flex_direction": "column",
                "flex_align_items": "center",
                "padding": {"unit": "px", "top": "70", "bottom": "70", "left": "40", "right": "40"},
                "text_align": "center"
            },
            "elements": [
                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "STAY UPDATED", "align": "center", "typography_font_size": {"unit": "px", "size": 12}, "title_color": "#948B83"}},
                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "JOIN THE NOVELLE CIRCLE", "align": "center", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 36}, "title_color": "#221E1C"}},
                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#6E6660;font-size:14px;margin-bottom:25px;text-align:center;">Be the first to know about new collections, exclusive offers and style tips.</p>'}},
                {
                    "id": uid(),
                    "elType": "widget",
                    "widgetType": "form",
                    "settings": {
                        "form_name": "NOVELLE Newsletter",
                        "form_fields": [
                            {"field_type": "email", "placeholder": "Enter your email address", "required": "true", "width": "70"}
                        ],
                        "button_text": "SUBSCRIBE  →",
                        "button_width": "30",
                        "button_background_color": "#221E1C",
                        "button_text_color": "#FFFFFF"
                    }
                }
            ]
        },
        # 10. Footer
        {
            "id": uid(),
            "elType": "container",
            "isInner": False,
            "settings": {
                "content_width": "boxed",
                "background_color": "#221E1C",
                "padding": {"unit": "px", "top": "80", "bottom": "40", "left": "40", "right": "40"}
            },
            "elements": [
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {"flex_direction": "row", "flex_justify_content": "space-between", "margin": {"unit": "px", "bottom": "50"}},
                    "elements": [
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 25}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "NOVELLE", "typography_font_family": "Cormorant Garamond", "typography_font_size": {"unit": "px", "size": 32}, "title_color": "#FAF7F2"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#B8B0A8;font-size:13px;letter-spacing:1px;">Style · Quality · You</p>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 16}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "SHOP", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#FAF7F2"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<ul style="list-style:none;padding:0;line-height:2;font-size:13px;color:#B8B0A8;"><li>New Arrivals</li><li>Dresses</li><li>Tops</li><li>Bottoms</li><li>Accessories</li></ul>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 16}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "ABOUT", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#FAF7F2"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<ul style="list-style:none;padding:0;line-height:2;font-size:13px;color:#B8B0A8;"><li>Our Story</li><li>Sustainability</li><li>Careers</li><li>Blog</li></ul>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 16}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "HELP", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#FAF7F2"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<ul style="list-style:none;padding:0;line-height:2;font-size:13px;color:#B8B0A8;"><li>Shipping</li><li>Returns</li><li>Size Guide</li><li>FAQs</li></ul>'}}
                            ]
                        },
                        {
                            "id": uid(),
                            "elType": "container",
                            "settings": {"width": {"unit": "%", "size": 20}},
                            "elements": [
                                {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {"title": "CONTACT", "typography_font_size": {"unit": "px", "size": 13}, "title_color": "#FAF7F2"}},
                                {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#B8B0A8;font-size:13px;line-height:1.8;">hello@novelle.com<br>+91 98765 43210<br>Bangalore, India</p>'}}
                            ]
                        }
                    ]
                },
                {
                    "id": uid(),
                    "elType": "container",
                    "settings": {
                        "flex_direction": "row",
                        "flex_justify_content": "space-between",
                        "border_border": "solid",
                        "border_width": {"unit": "px", "top": "1", "bottom": "0", "left": "0", "right": "0"},
                        "border_color": "#3D3531",
                        "padding": {"unit": "px", "top": "25"}
                    },
                    "elements": [
                        {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#B8B0A8;font-size:12px;">© 2026 Novelle. All rights reserved.</p>'}},
                        {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color:#FAF7F2;font-size:11px;letter-spacing:1px;font-weight:bold;">VISA &nbsp; MASTERCARD &nbsp; RUPAY &nbsp; PAYPAL</p>'}}
                    ]
                }
            ]
        }
    ]
}

os.makedirs(r'c:\Users\vimit\OneDrive\Desktop\fashion 2\elementor', exist_ok=True)
out_path = r'c:\Users\vimit\OneDrive\Desktop\fashion 2\elementor\novelle-elementor-template.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(elementor_data, f, indent=2)

print('Saved Elementor Template to:', out_path)
