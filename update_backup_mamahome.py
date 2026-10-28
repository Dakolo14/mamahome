import base64
import json
import re

# Read original backup.html
with open('backup_original_hp.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Load logo as base64 data URI so it always renders seamlessly
with open('mamahome_logo-removebg-preview.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')
logo_uri = f'data:image/png;base64,{logo_b64}'

# Load extracted products from Konga
with open('extracted_mamahome_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Group products
blenders = [p for p in products if p['category'] == 'blenders']
kettles = [p for p in products if p['category'] == 'kettles']
pressure_cookers = [p for p in products if p['category'] == 'pressure-cookers']
cooktops = [p for p in products if p['category'] == 'cooktops']
toastie = [p for p in products if p['category'] == 'toastie']

# 1. Update Title and Meta
content = content.replace('<title>Konga HP Shop In Shop</title>', '<title>MAMA HOME Official Store | Konga Nigeria</title>')

# 2. Update brand colors: #a50034 -> #f08228 (Mamahome warm vibrant orange), #85002a -> #d96c14 (hover state)
content = content.replace('#a50034', '#f08228')
content = content.replace('#85002a', '#d96c14')
content = content.replace('rgba(165, 0, 52, 0.5)', 'rgba(240, 130, 40, 0.5)')
content = content.replace('rgba(165, 0, 52,', 'rgba(240, 130, 40,')

# Add slight enhancement to the navbar-logo and overall feel in CSS
custom_css_additions = """
      /* MAMA HOME Header and Badge Refinements */
      .navbar-logo {
        height: 60px !important;
        display: flex;
        align-items: center;
      }
      .navbar-logo img {
        height: 100% !important;
        width: auto !important;
        object-fit: contain;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.08));
      }
      .shop-category-header {
        background: linear-gradient(135deg, #f08228 0%, #e06d12 100%) !important;
        box-shadow: 0 4px 12px rgba(240, 130, 40, 0.25);
      }
      .product-card {
        border: 1px solid #f1f1f1 !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        background: #ffffff;
        position: relative;
      }
      .product-card:hover {
        transform: translateY(-6px) !important;
        box-shadow: 0 12px 28px rgba(240, 130, 40, 0.15) !important;
        border-color: #f08228 !important;
      }
      .product-card h3 {
        font-size: 1rem !important;
        font-weight: 500 !important;
        line-height: 1.35;
        min-height: 2.7em;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }
      .product-btn {
        background-color: #f08228 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em;
        transition: all 0.25s ease !important;
      }
      .product-btn:hover {
        background-color: #d96c14 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(240, 130, 40, 0.35) !important;
      }
      .shop-category-card {
        background: #ffffff !important;
        border: 1.5px solid #f2f2f2 !important;
        transition: all 0.3s ease !important;
      }
      .shop-category-card:hover {
        transform: translateY(-6px) !important;
        border-color: #f08228 !important;
        box-shadow: 0 10px 24px rgba(240, 130, 40, 0.18) !important;
      }
      .shop-category-label {
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        color: #222 !important;
      }
      .cta-button {
        background-color: #f08228 !important;
        border-radius: 6px !important;
      }
      .cta-button:hover {
        background-color: #d96c14 !important;
      }
"""
content = content.replace('</style>', custom_css_additions + '\n    </style>')

# 3. Replace Navigation Header
old_nav_regex = r'<header class="navbar">.*?</header>'
new_nav = f"""<header class="navbar">
      <nav class="navbar-container">
        <a href="https://www.konga.com/merchant/mamahomez" target="_blank" rel="noopener" class="navbar-logo" title="MAMA HOME Official Store on Konga">
          <img src="{logo_uri}" alt="MAMA HOME Logo" />
        </a>
        <div class="nav-wrapper">
          <ul class="nav-items">
            <li><a href="#bestsellers">Best Sellers</a></li>
            <li><a href="#blenders">Blenders & Processors</a></li>
            <li><a href="#kettles">Electric Kettles</a></li>
            <li><a href="#cookers">Luna Pressure Cookers</a></li>
            <li><a href="#cooktops">Stoves & Appliances</a></li>
          </ul>
          <a href="https://www.konga.com/merchant/mamahomez" target="_blank" rel="noopener" class="cta-button" style="text-decoration: none;">View Store</a>
        </div>
      </nav>
    </header>"""
content = re.sub(old_nav_regex, new_nav, content, flags=re.DOTALL)

# 4. Replace Banner Carousel Images with Mamahome Product Showcase Banners
# High impact banners highlighting the Oga/Oba blenders, Aqua kettles, Luna cookers, and tabletop stoves
banner_images = [
    {
        "url": "https://www.konga.com/product/oga-multifunctional-blender-2000w-2-5l-7064781",
        "img": "https://www-konga-com-res.cloudinary.com/media/catalog/product/X/W/251919_1791302248.jpg",
        "alt": "MAMA HOME Heavy Duty 2000W Blenders"
    },
    {
        "url": "https://www.konga.com/product/aqua-plus-electric-kettle-oe-2-5l-7064234",
        "img": "https://www-konga-com-res.cloudinary.com/media/catalog/product/Z/R/251919_1791288738.jpg",
        "alt": "MAMA HOME Rapid Boil Electric Kettles"
    },
    {
        "url": "https://www.konga.com/product/luna-aluminium-pressure-cooker-7-5l-7063970",
        "img": "https://www-konga-com-res.cloudinary.com/media/catalog/product/A/U/251919_1791282604.jpg",
        "alt": "MAMA HOME Luna Aluminium Pressure Cookers"
    },
    {
        "url": "https://www.konga.com/product/infrared-griller-cooktop-7064301",
        "img": "https://www-konga-com-res.cloudinary.com/media/catalog/product/Q/A/251919_1791289950.jpg",
        "alt": "MAMA HOME Infrared Cooktops & Tabletop Stoves"
    },
    {
        "url": "https://www.konga.com/product/eddy-blender-1-5l-300w-black-7064664",
        "img": "https://www-konga-com-res.cloudinary.com/media/catalog/product/D/Z/251919_1791300150.jpg",
        "alt": "MAMA HOME 2-in-1 Multifunctional Grinders"
    },
    {
        "url": "https://www.konga.com/product/mama-home-toastie-sandwich-maker-oe-750w-7063854",
        "img": "https://www-konga-com-res.cloudinary.com/media/catalog/product/L/S/251919_1791277313.jpg",
        "alt": "MAMA HOME Toastie Sandwich Maker"
    }
]

# Build new slides HTML for the banner carousel
new_slides_html = ""
for i, b in enumerate(banner_images, 1):
    new_slides_html += f"""              <a href="{b['url']}" target="_blank" rel="noopener" class="banner-slide" style="background: linear-gradient(135deg, #fff7f0 0%, #ffe9d6 100%); display: flex; align-items: center; justify-content: center; position: relative;">
                <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; height: 100%; padding: 2rem 4rem; box-sizing: border-box; gap: 2rem;">
                  <div style="max-width: 580px; text-align: left; z-index: 2;">
                    <span style="display: inline-block; background-color: #f08228; color: #fff; padding: 4px 14px; border-radius: 50px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0.75rem; letter-spacing: 0.05em;">MAMA HOME OFFICIAL STORE</span>
                    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1a1a1a; line-height: 1.2; margin-bottom: 0.5rem;">{b['alt']}</h2>
                    <p style="font-size: 1rem; color: #555; margin-bottom: 1.25rem;">Quality, energy-saving kitchen appliances built for delicious meals everyday.</p>
                    <span style="display: inline-block; background-color: #1a1a1a; color: #fff; padding: 10px 24px; border-radius: 6px; font-weight: 600; font-size: 0.95rem;">Shop Now &rarr;</span>
                  </div>
                  <div style="height: 100%; max-height: 320px; display: flex; align-items: center; justify-content: center; flex: 1;">
                    <img src="{b['img']}" alt="{b['alt']}" loading="lazy" style="max-height: 280px; max-width: 100%; object-fit: contain; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.12));" />
                  </div>
                </div>
              </a>\n"""

banner_slides_regex = r'<div class="banner-slides-container">.*?</div>\s*<!-- Pagination dots -->'
content = re.sub(
    banner_slides_regex,
    f'<div class="banner-slides-container">\n{new_slides_html}            </div>\n\n            <!-- Pagination dots -->',
    content,
    flags=re.DOTALL
)

# 5. Replace "Shop By Category" Grid
new_category_bento = """    <!-- Shop By Category Section -->
    <section class="shop-by-category-section section-reset" id="categories" style="margin-top: 2rem !important;">
      <div class="shop-by-category-header" style="border-radius: 12px 12px 0 0;">Shop By Category</div>
      <div class="shop-category-container">
        <div class="shop-category-grid" style="grid-template-columns: repeat(5, 1fr);">
          <!-- Category 1 -->
          <a href="#blenders" class="shop-category-item">
            <div class="shop-category-card" style="background-color: #fafafa; padding: 1rem;">
              <img src="https://www-konga-com-res.cloudinary.com/media/catalog/product/X/W/251919_1791302248.jpg" alt="Blenders & Mills" style="max-height: 130px; object-fit: contain;" />
            </div>
            <div class="shop-category-label">Blenders &amp; Mills</div>
          </a>
          <!-- Category 2 -->
          <a href="#kettles" class="shop-category-item">
            <div class="shop-category-card" style="background-color: #fafafa; padding: 1rem;">
              <img src="https://www-konga-com-res.cloudinary.com/media/catalog/product/Z/R/251919_1791288738.jpg" alt="Electric Kettles" style="max-height: 130px; object-fit: contain;" />
            </div>
            <div class="shop-category-label">Electric Kettles</div>
          </a>
          <!-- Category 3 -->
          <a href="#cookers" class="shop-category-item">
            <div class="shop-category-card" style="background-color: #fafafa; padding: 1rem;">
              <img src="https://www-konga-com-res.cloudinary.com/media/catalog/product/W/R/251919_1791281979.jpg" alt="Luna Pressure Cookers" style="max-height: 130px; object-fit: contain;" />
            </div>
            <div class="shop-category-label">Pressure Cookers</div>
          </a>
          <!-- Category 4 -->
          <a href="#cooktops" class="shop-category-item">
            <div class="shop-category-card" style="background-color: #fafafa; padding: 1rem;">
              <img src="https://www-konga-com-res.cloudinary.com/media/catalog/product/Q/A/251919_1791289950.jpg" alt="Cooktops & Stoves" style="max-height: 130px; object-fit: contain;" />
            </div>
            <div class="shop-category-label">Cooktops &amp; Stoves</div>
          </a>
          <!-- Category 5 -->
          <a href="#toastie" class="shop-category-item">
            <div class="shop-category-card" style="background-color: #fafafa; padding: 1rem;">
              <img src="https://www-konga-com-res.cloudinary.com/media/catalog/product/L/S/251919_1791277313.jpg" alt="Sandwich Makers" style="max-height: 130px; object-fit: contain;" />
            </div>
            <div class="shop-category-label">Sandwich Makers</div>
          </a>
        </div>
      </div>
    </section>"""

old_cat_regex = r'<!-- Shop By Category Section -->.*?</section>'
content = re.sub(old_cat_regex, new_category_bento, content, count=1, flags=re.DOTALL)

# 6. Helper to generate a neat product grid
def build_product_card(p, badge_text=None):
    badge_html = f'<span style="position: absolute; top: 12px; left: 12px; background-color: #f08228; color: #fff; font-size: 0.75rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; z-index: 2;">{p["discount"]}</span>' if p.get('discount') else ''
    orig_price_html = f'<span style="font-size: 0.85rem; color: #999; text-decoration: line-through; margin-left: 6px;">{p["orig_price"]}</span>' if p.get('orig_price') and p['orig_price'] != p['price'] else ''
    
    return f"""            <!-- Product -->
            <article class="product-card">
              {badge_html}
              <a href="{p['url']}" target="_blank" rel="noopener" style="display: flex; align-items: center; justify-content: center; width: 100%; height: 180px;">
                <img src="{p['image']}" alt="{p['name']}" loading="lazy" style="max-height: 160px; max-width: 100%; object-fit: contain;" />
              </a>
              <h3 title="{p['name']}">
                <a href="{p['url']}" target="_blank" rel="noopener" style="text-decoration: none; color: inherit;">{p['name']}</a>
              </h3>
              <div style="display: flex; align-items: baseline; justify-content: center; gap: 4px; margin-top: 4px;">
                <span style="font-size: 1.15rem; font-weight: 700; color: #f08228;">{p['price']}</span>
                {orig_price_html}
              </div>
              <a href="{p['url']}" target="_blank" rel="noopener" class="product-btn" style="width: 80%; text-align: center; margin-top: 6px;">Buy Now</a>
            </article>"""

def build_category_section(sec_id, title, items, konga_search_url="https://www.konga.com/merchant/mamahomez"):
    cards_html = "\n".join([build_product_card(it) for it in items])
    return f"""    <!-- {title} Section -->
    <section class="shop-by-category-section section-reset" id="{sec_id}" style="margin-top: 2rem !important;">
      <div class="shop-by-category-header" style="border-radius: 12px 12px 0 0;">
        <div style="display: flex; justify-content: space-between; width: 100%; align-items: center;">
          <span>{title}</span>
          <a href="{konga_search_url}" target="_blank" rel="noopener" class="flash-more" style="color: #ffffff;">
            see more
            <span class="icon-circle" style="background-color: #ffffff;">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 18L15 12L9 6" stroke="#f08228" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </a>
        </div>
      </div>
      <div class="shop-category-container">
        <div style="background-color: #ffffff; border-radius: 0 0 24px 24px; padding: 2rem; width: 100%;">
          <div class="product-grid" style="grid-template-columns: repeat(4, 1fr); gap: 1.5rem; width: 100%;">
{cards_html}
          </div>
        </div>
      </div>
    </section>"""

# Curate Best Sellers (4 top items: Oga Blender, Aqua Plus 2.5L, Infrared Griller, Luna Cooker)
best_sellers_items = [
    next(p for p in products if 'oga' in p['name'].lower()),
    next(p for p in products if 'aqua plus' in p['name'].lower() and '2.5l' in p['name'].lower()),
    next(p for p in products if 'infrared' in p['name'].lower()),
    next(p for p in products if 'luna' in p['name'].lower() and '7.5l' in p['name'].lower()),
]

bestsellers_section_html = build_category_section("bestsellers", "Best Sellers Selection", best_sellers_items)
blenders_section_html = build_category_section("blenders", "High-Power Blenders & Food Processors", blenders[:4])
kettles_section_html = build_category_section("kettles", "Rapid-Boil Electric Kettles", kettles[:4])
cookers_section_html = build_category_section("cookers", "Luna Aluminium Pressure Cookers", pressure_cookers)

# Mixed Appliances Section (Cooktops & Toastie)
appliances_items = cooktops + toastie + [next(p for p in products if 'eddy' in p['name'].lower() and 'black' in p['name'].lower())]
appliances_section_html = build_category_section("cooktops", "Stoves, Grillers & Breakfast Appliances", appliances_items[:4])

all_mamahome_sections = f"""{bestsellers_section_html}

{blenders_section_html}

{kettles_section_html}

{cookers_section_html}

{appliances_section_html}"""

# Replace all old LG product sections (from "<!-- Home Appliances Section -->" down to right before "<!-- YouTube Section -->")
old_sections_regex = r'<!-- Home Appliances Section -->.*?<!-- YouTube Section -->'
content = re.sub(old_sections_regex, all_mamahome_sections + '\n\n    <!-- YouTube Section -->', content, flags=re.DOTALL)

# 7. Update YouTube Section text
content = content.replace(
    'New Product Alert: Discover the latest LG innovation designed to elevate your everyday life. Watch now!',
    'Experience the culinary power, speed, and durability of MAMA HOME kitchen appliances.'
)

# 8. Update "Shop All" link
content = content.replace('https://www.konga.com/search?search=HP', 'https://www.konga.com/merchant/mamahomez')

# 9. Update Promotional Banners Section
new_featured_banners = """    <!-- Featured Banners Section -->
    <section class="shop-by-category-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-category-container">
        <div style="background-color: #ffffff; border-radius: 0 0 24px 24px; padding: 2rem; width: 100%;">
          <div class="banner-grid" style="grid-template-columns: 1fr 1fr; gap: 1.5rem; width: 100%;">
            <!-- Banner 1 -->
            <a href="https://www.konga.com/product/oga-multifunctional-blender-2000w-2-5l-7064781" target="_blank" rel="noopener" style="text-decoration: none; color: inherit; display: block; border-radius: 12px; overflow: hidden; background: linear-gradient(135deg, #fff2e6 0%, #ffe0cc 100%); border: 1px solid #ffd1b3; padding: 2rem; transition: transform 0.3s ease;">
              <span style="background-color: #f08228; color: #fff; padding: 3px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">CHEF'S CHOICE</span>
              <h3 style="font-size: 1.5rem; font-weight: 700; color: #1a1a1a; margin: 0.75rem 0 0.5rem 0;">Oga &amp; Oba 2000W Blenders</h3>
              <p style="font-size: 0.9rem; color: #555; margin-bottom: 1.25rem;">Blend tough beans, nuts, and frozen fruits in seconds with commercial power.</p>
              <span style="font-weight: 600; color: #f08228;">Shop 2000W Range &rarr;</span>
            </a>
            <!-- Banner 2 -->
            <a href="https://www.konga.com/product/luna-aluminium-pressure-cooker-7-5l-7063970" target="_blank" rel="noopener" style="text-decoration: none; color: inherit; display: block; border-radius: 12px; overflow: hidden; background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%); border: 1px solid #fed7aa; padding: 2rem; transition: transform 0.3s ease;">
              <span style="background-color: #1a1a1a; color: #fff; padding: 3px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">SAVE 70% GAS</span>
              <h3 style="font-size: 1.5rem; font-weight: 700; color: #1a1a1a; margin: 0.75rem 0 0.5rem 0;">Luna Aluminium Cookers</h3>
              <p style="font-size: 0.9rem; color: #555; margin-bottom: 1.25rem;">Tenderize tough meats and cook family beans 3x faster with high safety standards.</p>
              <span style="font-weight: 600; color: #f08228;">Explore All Sizes (5L-12L) &rarr;</span>
            </a>
          </div>
        </div>
      </div>
    </section>"""

old_fb_regex = r'<!-- Featured Banners Section -->.*?</section>'
content = re.sub(old_fb_regex, new_featured_banners, content, count=1, flags=re.DOTALL)

# 10. Update SEO Content Section
new_seo_content = """    <!-- SEO Content Section -->
    <section class="seo-content-section">
      <div class="seo-container">
        <h2>Your Trusted Destination for MAMA HOME Kitchen Appliances on Konga Nigeria</h2>
        <div class="seo-content">
          <p>
            Discover the complete range of authentic <strong>MAMA HOME kitchen appliances on Konga Nigeria</strong>. Designed specifically to handle the demands of everyday Nigerian cooking, our appliances combine heavy-duty performance, premium stainless steel craftsmanship, and modern energy efficiency. From high-power commercial blenders to rapid electric kettles and durable pressure cookers, MAMA HOME equips your kitchen with reliable companions for every recipe.
          </p>
          <p>
            Experience extraordinary speed and grinding consistency with the <strong>Oga and Oba 2000W Multifunctional Blenders</strong>. Whether blending soaked beans for fluffy akara and moist moin-moin, pureeing thick pepper soups, or milling dry grains and tigernut milk, MAMA HOME blenders feature hardened multi-blade technology and unbreakable jugs to get the job done effortlessly.
          </p>
          <p>
            Save up to 70% on domestic cooking gas with the <strong>Luna Aluminium Pressure Cooker</strong> collection. Available in versatile sizes from 5 Litres to 12 Litres, Luna pressure cookers feature multi-stage pressure regulator valves and heavy-gauge aluminium alloy that retains heat efficiently while locking in natural nutrients and flavours.
          </p>
          <p>
            Shop with total peace of mind on the official <strong>MAMA HOME Konga Shop in Shop</strong>. All orders are genuine, backed by manufacturer warranties, and fulfilled nationwide with Konga's fast delivery network and secure payment options.
          </p>
        </div>
      </div>
    </section>"""

old_seo_regex = r'<!-- SEO Content Section -->.*?</section>'
content = re.sub(old_seo_regex, new_seo_content, content, count=1, flags=re.DOTALL)

# Write updated content to backup.html
with open('backup.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("backup.html successfully updated to MAMA HOME brand styling and products!")
