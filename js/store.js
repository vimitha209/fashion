/**
 * NOVELLE — Global State Management & Shared Catalog
 * Provides persistent Cart, Wishlist, Order and Navigation state across all pages.
 */

const NOVELLE_CATALOG = {
  '101': {
    id: '101',
    name: 'Linen Midi Dress',
    price: 4990,
    category: 'dresses',
    categoryLabel: 'Dresses',
    image: '/assets/images/prod_1.jpg',
    badge: 'Best Seller',
    tagline: 'Effortless fluid drape for warm daylight',
    description: 'Crafted from 100% natural European flax linen, this midi dress blends quiet luxury with everyday ease. Designed with subtle waist contouring, side pockets, and an elegant scooped neckline that transitions effortlessly from morning gatherings to sunset dinners.',
    fabric: '100% Certified European Flax Linen',
    care: 'Dry clean recommended or gentle cold hand wash. Lay flat to dry.',
    fit: 'True to size with a relaxed, fluid silhouette. Model is 5\'9" wearing size S.',
    sizes: ['XS', 'S', 'M', 'L', 'XL']
  },
  '102': {
    id: '102',
    name: 'Tailored Warm',
    price: 5190,
    category: 'outerwear',
    categoryLabel: 'Outerwear',
    image: '/assets/images/prod_2.jpg',
    badge: 'New Season',
    tagline: 'Structured warmth with architectural tailoring',
    description: 'An impeccably tailored double-breasted coat rendered in a warm biscuit camel tone. Features peaked lapels, natural horn buttons, structured shoulders, and an interior silk-blend lining for smooth layering over cashmere knits.',
    fabric: 'Wool-blend outer with 100% cupro luxury lining',
    care: 'Specialist dry clean only. Store on wide wooden hanger.',
    fit: 'Tailored fit through shoulders with a gentle straight cut body.',
    sizes: ['XS', 'S', 'M', 'L', 'XL']
  },
  '103': {
    id: '103',
    name: 'Knit Top',
    price: 2990,
    category: 'tops',
    categoryLabel: 'Tops',
    image: '/assets/images/prod_3.jpg',
    badge: 'Essentials',
    tagline: 'Ultra-fine ribbing for a second-skin feel',
    description: 'A minimalist wardrobe staple woven from extra-fine compact spun cotton yarns. Featuring a clean neckline, delicate micro-ribbing, and subtle stretch that retains shape through every wash.',
    fabric: '95% Compact Spun Organic Cotton, 5% Elastane',
    care: 'Machine wash cold on gentle cycle. Do not tumble dry.',
    fit: 'Fitted cut. For a more relaxed drape, we recommend sizing up.',
    sizes: ['XS', 'S', 'M', 'L']
  },
  '104': {
    id: '104',
    name: 'Wide Leg Trousers',
    price: 3490,
    category: 'bottoms',
    categoryLabel: 'Bottoms',
    image: '/assets/images/prod_4.jpg',
    badge: 'Popular',
    tagline: 'Elongated silhouette with sharp double pleats',
    description: 'High-waisted fluid trousers engineered with sharp front knife pleats, side slash pockets, and a clean hook-and-bar closure. Cut from a lightweight seasonless drape cloth that sways gracefully with each step.',
    fabric: '70% Viscose, 26% Linen, 4% Spandex',
    care: 'Dry clean or steam refresh. Iron low on reverse.',
    fit: 'High rise with a generous wide-leg profile.',
    sizes: ['XS', 'S', 'M', 'L', 'XL']
  },
  '105': {
    id: '105',
    name: 'Shirt Dress',
    price: 4490,
    category: 'dresses',
    categoryLabel: 'Dresses',
    image: '/assets/images/prod_5.jpg',
    badge: 'Editorial Pick',
    tagline: 'Crisp utilitarian charm with feminine restraint',
    description: 'A contemporary take on the classic shirt dress, cut in an olive sage hue with a concealed button placket, cuffed sleeves, side seam slits, and a matching self-tie sash to define the waistline.',
    fabric: '100% High-Density Poplin Cotton',
    care: 'Gentle machine wash at 30°C. Warm iron while damp.',
    fit: 'Regular fit. Can be worn cinched or unbelted as an open duster coat.',
    sizes: ['XS', 'S', 'M', 'L']
  },
  '106': {
    id: '106',
    name: 'Knit Sweater',
    price: 3990,
    category: 'tops',
    categoryLabel: 'Tops',
    image: '/assets/images/prod_6.png',
    badge: 'Autumn Essential',
    tagline: 'Sumptuous tactile warmth in oatmeal melange',
    description: 'A cozy drop-shoulder crewneck knit crafted in a chunky textured fisherman stitch. Features relaxed ribbed trims at the collar, cuffs, and hem for an unhurried, comfortable weekend silhouette.',
    fabric: '60% Merino Wool, 40% Recycled Cotton',
    care: 'Hand wash cold with wool detergent. Dry flat away from direct sun.',
    fit: 'Oversized relaxed fit.',
    sizes: ['S', 'M', 'L']
  }
};

const NovelleStore = {
  // --------------------------------------------------------------------------
  // Cart API (Persistent in localStorage)
  // --------------------------------------------------------------------------
  getCart() {
    try {
      const data = localStorage.getItem('novelle_cart');
      const cart = data ? JSON.parse(data) : [];
      return cart.map(item => {
        if (item.image && !item.image.startsWith('/') && !item.image.startsWith('http')) {
          item.image = '/' + item.image;
        }
        return item;
      });
    } catch (e) {
      console.error('Error loading cart', e);
      return [];
    }
  },

  saveCart(cart) {
    try {
      localStorage.setItem('novelle_cart', JSON.stringify(cart));
      this.updateHeaderBadges();
      window.dispatchEvent(new CustomEvent('novelle:cart_updated', { detail: { cart } }));
    } catch (e) {
      console.error('Error saving cart', e);
    }
  },

  addToCart(productId, qty = 1, size = 'M') {
    const product = NOVELLE_CATALOG[productId];
    if (!product) return null;

    const cart = this.getCart();
    const existingIndex = cart.findIndex(item => item.id === productId && item.size === size);

    if (existingIndex > -1) {
      cart[existingIndex].qty += qty;
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        price: product.price,
        category: product.category,
        categoryLabel: product.categoryLabel,
        image: product.image,
        size: size,
        qty: qty
      });
    }

    this.saveCart(cart);
    this.showToast(`Added <strong>${product.name}</strong> (${size}) to your bag.`, 'success');
    return cart;
  },

  updateCartQty(productId, delta, size = null) {
    let cart = this.getCart();
    const item = cart.find(i => i.id === productId && (size === null || i.size === size));
    if (!item) return cart;

    item.qty += delta;
    if (item.qty <= 0) {
      cart = cart.filter(i => !(i.id === productId && (size === null || i.size === size)));
      this.showToast(`Removed <strong>${item.name}</strong> from your bag.`, 'info');
    }

    this.saveCart(cart);
    return cart;
  },

  removeFromCart(productId, size = null) {
    let cart = this.getCart();
    const item = cart.find(i => i.id === productId && (size === null || i.size === size));
    const name = item ? item.name : 'Item';

    cart = cart.filter(i => !(i.id === productId && (size === null || i.size === size)));
    this.saveCart(cart);
    this.showToast(`Removed <strong>${name}</strong> from your bag.`, 'info');
    return cart;
  },

  clearCart() {
    this.saveCart([]);
  },

  getCartCount() {
    return this.getCart().reduce((sum, item) => sum + (item.qty || 1), 0);
  },

  getCartSubtotal() {
    return this.getCart().reduce((sum, item) => sum + (item.price * (item.qty || 1)), 0);
  },

  // --------------------------------------------------------------------------
  // Wishlist API (Persistent in localStorage)
  // --------------------------------------------------------------------------
  getWishlist() {
    try {
      const data = localStorage.getItem('novelle_wishlist');
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error('Error loading wishlist', e);
      return [];
    }
  },

  saveWishlist(wishlist) {
    try {
      localStorage.setItem('novelle_wishlist', JSON.stringify(wishlist));
      this.updateHeaderBadges();
      window.dispatchEvent(new CustomEvent('novelle:wishlist_updated', { detail: { wishlist } }));
    } catch (e) {
      console.error('Error saving wishlist', e);
    }
  },

  isInWishlist(productId) {
    const list = this.getWishlist();
    return list.includes(String(productId));
  },

  toggleWishlist(productId) {
    const id = String(productId);
    let list = this.getWishlist();
    const product = NOVELLE_CATALOG[id];
    const name = product ? product.name : 'Item';

    if (list.includes(id)) {
      list = list.filter(item => item !== id);
      this.saveWishlist(list);
      this.showToast(`Removed <strong>${name}</strong> from your Wishlist.`, 'info');
      return false;
    } else {
      list.push(id);
      this.saveWishlist(list);
      this.showToast(`Saved <strong>${name}</strong> to your Wishlist.`, 'wishlist');
      return true;
    }
  },

  getWishlistCount() {
    return this.getWishlist().length;
  },

  // --------------------------------------------------------------------------
  // Delivery & Order Management
  // --------------------------------------------------------------------------
  saveDeliveryInfo(info) {
    try {
      localStorage.setItem('novelle_delivery', JSON.stringify(info));
    } catch (e) {
      console.error(e);
    }
  },

  getDeliveryInfo() {
    try {
      const data = localStorage.getItem('novelle_delivery');
      return data ? JSON.parse(data) : null;
    } catch (e) {
      return null;
    }
  },

  saveLastOrder(order) {
    try {
      localStorage.setItem('novelle_last_order', JSON.stringify(order));
    } catch (e) {
      console.error(e);
    }
  },

  getLastOrder() {
    try {
      const data = localStorage.getItem('novelle_last_order');
      return data ? JSON.parse(data) : null;
    } catch (e) {
      return null;
    }
  },

  // --------------------------------------------------------------------------
  // Formatting & UI Feedback
  // --------------------------------------------------------------------------
  formatCurrency(amount) {
    return '₹ ' + Number(amount || 0).toLocaleString('en-IN');
  },

  showToast(message, type = 'info') {
    let container = document.getElementById('toastContainer');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toastContainer';
      container.className = 'fixed bottom-6 right-6 z-50 flex flex-col gap-3 pointer-events-none';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `flex items-center gap-3 px-5 py-3.5 bg-[#1A1A1A] text-white text-xs rounded shadow-2xl border-l-4 transition-all duration-300 transform translate-y-3 opacity-0 max-w-sm pointer-events-auto ${
      type === 'wishlist' ? 'border-rose-500' : type === 'success' ? 'border-emerald-500' : 'border-[#C5A880]'
    }`;

    let iconHtml = '';
    if (type === 'wishlist') {
      iconHtml = `<svg class="w-4 h-4 text-rose-500 shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>`;
    } else if (type === 'success') {
      iconHtml = `<svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
    } else {
      iconHtml = `<svg class="w-4 h-4 text-[#C5A880] shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>`;
    }

    toast.innerHTML = `
      ${iconHtml}
      <div class="leading-relaxed font-light">${message}</div>
    `;

    container.appendChild(toast);

    requestAnimationFrame(() => {
      toast.classList.remove('translate-y-3', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
    });

    setTimeout(() => {
      toast.classList.remove('translate-y-0', 'opacity-100');
      toast.classList.add('translate-y-3', 'opacity-0');
      setTimeout(() => toast.remove(), 320);
    }, 3200);
  },

  updateHeaderBadges() {
    const cartCount = this.getCartCount();
    const wishlistCount = this.getWishlistCount();

    const cartBadge = document.getElementById('cartCountBadge');
    if (cartBadge) {
      cartBadge.textContent = cartCount;
      if (cartCount > 0) {
        cartBadge.classList.remove('scale-0');
        cartBadge.classList.add('scale-100');
      } else {
        cartBadge.textContent = '0';
      }
    }

    const wishlistBadge = document.getElementById('wishlistCountBadge');
    if (wishlistBadge) {
      wishlistBadge.textContent = wishlistCount;
      if (wishlistCount > 0) {
        wishlistBadge.classList.remove('scale-0');
        wishlistBadge.classList.add('scale-100');
      } else {
        wishlistBadge.classList.remove('scale-100');
        wishlistBadge.classList.add('scale-0');
      }
    }
  },

  searchProducts(query) {
    const q = (query || '').toLowerCase().trim();
    if (!q) return [];
    return Object.values(NOVELLE_CATALOG).filter(item => {
      return (
        (item.name && item.name.toLowerCase().includes(q)) ||
        (item.category && item.category.toLowerCase().includes(q)) ||
        (item.categoryLabel && item.categoryLabel.toLowerCase().includes(q)) ||
        (item.fabric && item.fabric.toLowerCase().includes(q)) ||
        (item.description && item.description.toLowerCase().includes(q)) ||
        (item.fit && item.fit.toLowerCase().includes(q)) ||
        (item.tagline && item.tagline.toLowerCase().includes(q)) ||
        (item.badge && item.badge.toLowerCase().includes(q))
      );
    });
  },

  // --------------------------------------------------------------------------
  // Header Navigation & Modal Handlers (Runs on every page)
  // --------------------------------------------------------------------------
  initCommonHeader() {
    this.updateHeaderBadges();

    // Mobile Drawer navigation
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileNavDrawer = document.getElementById('mobileNavDrawer');
    const mobileNavClose = document.getElementById('mobileNavClose');
    const mobileNavBackdrop = document.getElementById('mobileNavBackdrop');

    const openMobile = () => {
      if (mobileNavDrawer && mobileNavBackdrop) {
        mobileNavDrawer.classList.add('open');
        mobileNavBackdrop.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    };

    const closeMobile = () => {
      if (mobileNavDrawer && mobileNavBackdrop) {
        mobileNavDrawer.classList.remove('open');
        mobileNavBackdrop.classList.remove('open');
        document.body.style.overflow = '';
      }
    };

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMobile);
    if (mobileNavClose) mobileNavClose.addEventListener('click', closeMobile);
    if (mobileNavBackdrop) mobileNavBackdrop.addEventListener('click', closeMobile);

    document.querySelectorAll('.mobile-link').forEach(link => {
      link.addEventListener('click', closeMobile);
    });

    // Ensure search modal exists across all pages (if not already on /search)
    let searchModal = document.getElementById('searchModal');
    const isSearchPage = window.location.pathname.startsWith('/search');

    if (!searchModal && !isSearchPage) {
      const modalWrapper = document.createElement('div');
      modalWrapper.id = 'searchModal';
      modalWrapper.className = 'fixed inset-0 bg-black/60 backdrop-blur-xs z-50 opacity-0 pointer-events-none transition-opacity duration-300 flex items-start justify-center pt-24 px-6';
      modalWrapper.innerHTML = `
        <div class="bg-white w-full max-w-2xl p-6 sm:p-8 shadow-2xl border border-novelle-border transform -translate-y-6 transition-transform duration-300">
          <div class="flex items-center justify-between pb-4 border-b border-novelle-border mb-6">
            <span class="text-xs uppercase tracking-[0.2em] text-novelle-muted font-medium">Search Collection</span>
            <button id="searchCloseBtn" class="text-novelle-charcoal hover:text-novelle-taupe p-1" aria-label="Close search">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
          <div class="relative border-b-2 border-novelle-charcoal flex items-center">
            <input type="text" id="searchInput" placeholder="Search by keyword (e.g., dress, linen, tailored, sweater)..." class="w-full pb-3 pr-10 text-base sm:text-lg focus:outline-none text-novelle-charcoal bg-transparent font-serif placeholder:font-sans placeholder:text-xs placeholder:text-novelle-muted">
            <button id="searchSubmitBtn" type="button" class="absolute right-0 top-1/2 -translate-y-1/2 pb-3 text-novelle-charcoal hover:text-novelle-taupe transition-colors p-1" aria-label="Submit search">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
            </button>
          </div>
          <!-- Live Search Results Dropdown -->
          <div id="searchLiveResults" class="hidden mt-4 max-h-72 overflow-y-auto divide-y divide-novelle-border/60"></div>
          <div id="searchQuickSuggestions" class="mt-6">
            <p class="text-[11px] uppercase tracking-wider text-novelle-muted mb-3 font-medium">Quick Suggestions:</p>
            <div class="flex flex-wrap gap-2 text-xs">
              <button class="search-tag px-3 py-1 bg-novelle-soft hover:bg-novelle-sand transition-colors text-novelle-charcoal">Linen Dress</button>
              <button class="search-tag px-3 py-1 bg-novelle-soft hover:bg-novelle-sand transition-colors text-novelle-charcoal">Tailored Warm</button>
              <button class="search-tag px-3 py-1 bg-novelle-soft hover:bg-novelle-sand transition-colors text-novelle-charcoal">Knit Tops</button>
              <button class="search-tag px-3 py-1 bg-novelle-soft hover:bg-novelle-sand transition-colors text-novelle-charcoal">Trousers</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modalWrapper);
      searchModal = modalWrapper;
    }

    const searchCloseBtn = document.getElementById('searchCloseBtn');
    const searchInput = document.getElementById('searchInput');
    const searchSubmitBtn = document.getElementById('searchSubmitBtn');
    const searchLiveResults = document.getElementById('searchLiveResults');
    const searchQuickSuggestions = document.getElementById('searchQuickSuggestions');

    const openSearch = () => {
      if (searchModal) {
        searchModal.classList.add('open');
        if (searchInput) {
          setTimeout(() => searchInput.focus(), 150);
        }
        document.body.style.overflow = 'hidden';
      } else {
        window.location.href = '/search';
      }
    };

    const closeSearch = () => {
      if (searchModal) {
        searchModal.classList.remove('open');
        document.body.style.overflow = '';
      }
    };

    // Attach search triggers
    const searchOpenBtn = document.getElementById('searchOpenBtn');
    if (searchOpenBtn) {
      searchOpenBtn.addEventListener('click', (e) => {
        e.preventDefault();
        openSearch();
      });
    }

    // Also support any link targeting search if on non-search pages
    if (!isSearchPage) {
      document.querySelectorAll('a[href="/search"]').forEach(link => {
        // Exclude footer links if desired, or let header search icon open modal
        if (link.closest('header') || link.closest('#mobileNavDrawer')) {
          link.addEventListener('click', (e) => {
            e.preventDefault();
            if (mobileNavDrawer && mobileNavBackdrop) closeMobile();
            openSearch();
          });
        }
      });
    }

    if (searchCloseBtn) searchCloseBtn.addEventListener('click', closeSearch);
    if (searchModal) {
      searchModal.addEventListener('click', (e) => {
        if (e.target === searchModal) closeSearch();
      });
    }

    const executeSearch = () => {
      const q = searchInput ? searchInput.value.trim() : '';
      closeSearch();
      window.location.href = q ? `/search?q=${encodeURIComponent(q)}` : '/search';
    };

    if (searchSubmitBtn) {
      searchSubmitBtn.addEventListener('click', (e) => {
        e.preventDefault();
        executeSearch();
      });
    }

    if (searchInput) {
      searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          executeSearch();
        }
      });

      // Live search suggestions as user types
      searchInput.addEventListener('input', () => {
        const q = searchInput.value.trim();
        if (!searchLiveResults) return;

        if (!q) {
          searchLiveResults.classList.add('hidden');
          searchLiveResults.innerHTML = '';
          if (searchQuickSuggestions) searchQuickSuggestions.classList.remove('hidden');
          return;
        }

        if (searchQuickSuggestions) searchQuickSuggestions.classList.add('hidden');
        searchLiveResults.classList.remove('hidden');

        const matches = this.searchProducts(q);

        if (matches.length > 0) {
          searchLiveResults.innerHTML = `
            <div class="py-2.5 px-1 text-[11px] uppercase tracking-wider text-novelle-muted font-medium flex justify-between items-center border-b border-novelle-border/60 mb-1">
              <span>Matching Pieces (${matches.length})</span>
              <a href="/search?q=${encodeURIComponent(q)}" class="text-novelle-taupe hover:underline normal-case tracking-normal">View all in Search &rarr;</a>
            </div>
            <div class="divide-y divide-novelle-border/50">
              ${matches.slice(0, 5).map(p => `
                <a href="/product/${p.id}" class="flex items-center gap-3.5 py-2.5 px-2 hover:bg-novelle-soft/80 transition-colors group">
                  <img src="${p.image}" alt="${p.name}" class="w-11 h-14 object-cover shrink-0 bg-novelle-soft border border-novelle-border/40">
                  <div class="flex-grow min-w-0">
                    <p class="text-xs sm:text-sm font-medium text-novelle-charcoal truncate group-hover:text-novelle-taupe transition-colors">${p.name}</p>
                    <p class="text-[11px] text-novelle-muted truncate mt-0.5">${p.categoryLabel || p.category} &middot; ${p.fabric || ''}</p>
                  </div>
                  <div class="text-right shrink-0">
                    <span class="text-xs font-semibold text-novelle-charcoal">${this.formatCurrency(p.price)}</span>
                  </div>
                </a>
              `).join('')}
            </div>
            <div class="pt-3 pb-1">
              <a href="/search?q=${encodeURIComponent(q)}" class="block w-full py-2.5 bg-novelle-charcoal hover:bg-novelle-taupe text-white text-[11px] uppercase tracking-[0.18em] font-medium transition-colors text-center">
                Open Full Search Results (${matches.length}) &rarr;
              </a>
            </div>
          `;
        } else {
          searchLiveResults.innerHTML = `
            <div class="py-8 px-4 text-center">
              <div class="w-12 h-12 rounded-full bg-novelle-soft flex items-center justify-center text-novelle-muted mx-auto mb-3">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </div>
              <h4 class="font-serif text-lg text-novelle-charcoal mb-1">No products found</h4>
              <p class="text-xs text-novelle-muted font-light max-w-sm mx-auto leading-relaxed">
                No pieces matched "<strong>${q.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c])}</strong>". Try searching for dresses, linen, tops, or trousers.
              </p>
            </div>
          `;
        }
      });
    }

    // Attach quick tags
    document.querySelectorAll('.search-tag').forEach(tag => {
      tag.addEventListener('click', () => {
        const q = tag.textContent.trim();
        closeSearch();
        window.location.href = `/search?q=${encodeURIComponent(q)}`;
      });
    });

    // Account trigger
    const accountBtn = document.getElementById('accountModalBtn');
    if (accountBtn) {
      accountBtn.addEventListener('click', (e) => {
        e.preventDefault();
        this.showToast('NOVELLE Member Portal: Concierge privileges are active. Welcome back.', 'info');
      });
    }

    // ESC key closes any open drawer / modal
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeMobile();
        closeSearch();
      }
    });
  }
};

// Auto-initialize when loaded
document.addEventListener('DOMContentLoaded', () => {
  NovelleStore.initCommonHeader();
});
