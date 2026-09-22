/**
 * NOVELLE — Luxury Minimalist Fashion SPA Engine
 * Integrates with NovelleStore for persistent Cart, Wishlist, Search routing, and Multi-page navigation.
 */

document.addEventListener('DOMContentLoaded', () => {
  // ==========================================================================
  // 1. DOM Elements
  // ==========================================================================
  const productGrid = document.getElementById('productGrid');
  const productItems = document.querySelectorAll('.product-item');
  const filterTabs = document.querySelectorAll('.filter-tab');
  const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');
  const wishlistBtns = document.querySelectorAll('.wishlist-btn');
  const categoryCards = document.querySelectorAll('.category-card');

  // Cart Drawer Elements
  const cartDrawer = document.getElementById('cartDrawer');
  const cartDrawerBackdrop = document.getElementById('cartDrawerBackdrop');
  const cartDrawerClose = document.getElementById('cartDrawerClose');
  const cartDrawerBadge = document.getElementById('cartDrawerBadge');
  const cartItemsContainer = document.getElementById('cartItemsContainer');
  const cartSubtotal = document.getElementById('cartSubtotal');
  const freeShippingNotice = document.getElementById('freeShippingNotice');

  // Contact & Newsletter Forms
  const contactForm = document.getElementById('contactForm');
  const newsletterForm = document.getElementById('newsletterForm');

  // ==========================================================================
  // 2. Cart Drawer Sync with Persistent NovelleStore
  // ==========================================================================
  function openCartDrawer() {
    if (cartDrawer && cartDrawerBackdrop) {
      cartDrawer.classList.add('open');
      cartDrawerBackdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeCartDrawer() {
    if (cartDrawer && cartDrawerBackdrop) {
      cartDrawer.classList.remove('open');
      cartDrawerBackdrop.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  if (cartDrawerClose) cartDrawerClose.addEventListener('click', closeCartDrawer);
  if (cartDrawerBackdrop) cartDrawerBackdrop.addEventListener('click', closeCartDrawer);

  function renderCartDrawer() {
    const cart = NovelleStore.getCart();
    const count = NovelleStore.getCartCount();
    const subtotal = NovelleStore.getCartSubtotal();

    if (cartDrawerBadge) {
      cartDrawerBadge.textContent = `${count} item${count === 1 ? '' : 's'}`;
    }

    if (cartSubtotal) {
      cartSubtotal.textContent = NovelleStore.formatCurrency(subtotal);
    }

    if (freeShippingNotice) {
      const threshold = 4000;
      if (subtotal >= threshold || count === 0) {
        freeShippingNotice.innerHTML = `Enjoy <strong>Complimentary Express Shipping</strong> across India`;
      } else {
        const remaining = threshold - subtotal;
        freeShippingNotice.innerHTML = `Add <strong>${NovelleStore.formatCurrency(remaining)}</strong> more to unlock <strong>Complimentary Shipping</strong>`;
      }
    }

    if (!cartItemsContainer) return;

    if (cart.length === 0) {
      cartItemsContainer.innerHTML = `
        <div class="h-full flex flex-col items-center justify-center text-center py-12 px-4">
          <div class="w-16 h-16 rounded-full bg-novelle-soft flex items-center justify-center text-novelle-muted mb-4">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24">
              <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <path d="M16 10a4 4 0 0 1-8 0"></path>
            </svg>
          </div>
          <h4 class="font-serif text-xl uppercase tracking-wider text-novelle-charcoal mb-2">Your Bag is Empty</h4>
          <p class="text-xs text-novelle-muted font-light max-w-xs mb-6 leading-relaxed">Discover our timeless collections and find your signature look.</p>
          <a href="#shop" onclick="document.getElementById('cartDrawerClose').click()" class="px-6 py-2.5 bg-novelle-charcoal text-white text-xs uppercase tracking-widest font-medium hover:bg-novelle-taupe transition-colors">
            Explore Collection
          </a>
        </div>
      `;
      return;
    }

    cartItemsContainer.innerHTML = cart.map(item => `
      <div class="flex gap-4 pt-4 first:pt-0" data-id="${item.id}" data-size="${item.size || 'M'}">
        <a href="/product/${item.id}" class="w-20 h-24 bg-novelle-soft overflow-hidden shrink-0 border border-novelle-border/60 block">
          <img src="${item.image}" alt="${item.name}" class="w-full h-full object-cover">
        </a>
        <div class="flex flex-col justify-between flex-grow">
          <div>
            <div class="flex items-start justify-between gap-2">
              <a href="/product/${item.id}" class="text-xs sm:text-sm font-medium text-novelle-charcoal tracking-wide hover:text-novelle-taupe transition-colors">
                ${item.name}
              </a>
              <button class="drawer-remove-item text-novelle-muted hover:text-rose-600 p-0.5 transition-colors" data-id="${item.id}" data-size="${item.size || 'M'}" aria-label="Remove item">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </button>
            </div>
            <p class="text-[11px] text-novelle-muted uppercase tracking-wider mt-0.5">${item.categoryLabel || item.category} &middot; Size: ${item.size || 'M'}</p>
          </div>
          <div class="flex items-center justify-between mt-2">
            <div class="flex items-center border border-novelle-border bg-white">
              <button class="drawer-qty-minus px-2 py-1 text-xs text-novelle-charcoal hover:bg-novelle-soft transition-colors" data-id="${item.id}" data-size="${item.size || 'M'}">&minus;</button>
              <span class="px-2.5 py-1 text-xs font-medium text-novelle-charcoal min-w-[24px] text-center">${item.qty}</span>
              <button class="drawer-qty-plus px-2 py-1 text-xs text-novelle-charcoal hover:bg-novelle-soft transition-colors" data-id="${item.id}" data-size="${item.size || 'M'}">&plus;</button>
            </div>
            <span class="text-xs font-semibold text-novelle-charcoal">${NovelleStore.formatCurrency(item.price * item.qty)}</span>
          </div>
        </div>
      </div>
    `).join('');

    // Attach drawer stepper & remove listeners
    document.querySelectorAll('.drawer-remove-item').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.getAttribute('data-id');
        const size = btn.getAttribute('data-size');
        NovelleStore.removeFromCart(id, size);
      });
    });

    document.querySelectorAll('.drawer-qty-minus').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.getAttribute('data-id');
        const size = btn.getAttribute('data-size');
        NovelleStore.updateCartQty(id, -1, size);
      });
    });

    document.querySelectorAll('.drawer-qty-plus').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.getAttribute('data-id');
        const size = btn.getAttribute('data-size');
        NovelleStore.updateCartQty(id, 1, size);
      });
    });
  }

  // Bind Add to Cart buttons on Homepage Grid
  addToCartBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const id = btn.getAttribute('data-id');
      NovelleStore.addToCart(id);
      openCartDrawer();
    });
  });

  // ==========================================================================
  // 3. Wishlist Interactivity with Persistent Store
  // ==========================================================================
  function syncWishlistCardStates() {
    wishlistBtns.forEach(btn => {
      const id = btn.getAttribute('data-id');
      const inWishlist = NovelleStore.isInWishlist(id);
      const svg = btn.querySelector('svg');

      if (inWishlist) {
        btn.classList.add('active', 'bg-white', 'text-rose-600');
        if (svg) {
          svg.classList.add('fill-rose-600', 'stroke-rose-600');
          svg.setAttribute('fill', '#E11D48');
        }
      } else {
        btn.classList.remove('active', 'bg-white', 'text-rose-600');
        if (svg) {
          svg.classList.remove('fill-rose-600', 'stroke-rose-600');
          svg.setAttribute('fill', 'none');
        }
      }
    });
  }

  wishlistBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const id = btn.getAttribute('data-id');
      NovelleStore.toggleWishlist(id);
      syncWishlistCardStates();
    });
  });

  // ==========================================================================
  // 4. Category Filtering Tabs
  // ==========================================================================
  function filterCategory(category) {
    productItems.forEach(item => {
      const itemCat = item.getAttribute('data-category');
      if (category === 'all' || itemCat === category) {
        item.classList.remove('hidden-filter');
      } else {
        item.classList.add('hidden-filter');
      }
    });
  }

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      filterCategory(tab.getAttribute('data-category'));
    });
  });

  categoryCards.forEach(card => {
    card.addEventListener('click', (e) => {
      const filter = card.getAttribute('data-filter');
      if (filter) {
        const matchingTab = Array.from(filterTabs).find(t => t.getAttribute('data-category') === filter);
        if (matchingTab) {
          filterTabs.forEach(t => t.classList.remove('active'));
          matchingTab.classList.add('active');
          filterCategory(filter);
        }
      }
    });
  });

  // ==========================================================================
  // 5. Working Contact & Newsletter Forms
  // ==========================================================================
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nameInput = document.getElementById('contactName');
      const name = nameInput ? nameInput.value.trim() : 'Guest';
      NovelleStore.showToast(`Thank you, <strong>${name}</strong>! Your message has been received. Our concierge will be in touch within 24 hours.`, 'success');
      contactForm.reset();
    });
  }

  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = document.getElementById('newsletterEmail');
      const email = emailInput ? emailInput.value.trim() : '';
      NovelleStore.showToast(`Welcome to the <strong>Novelle Circle</strong>! Check ${email} for your 10% welcome privilege.`, 'success');
      newsletterForm.reset();
    });
  }

  // Listen to Global Store Events
  window.addEventListener('novelle:cart_updated', renderCartDrawer);
  window.addEventListener('novelle:wishlist_updated', syncWishlistCardStates);

  // Initial Sync
  renderCartDrawer();
  syncWishlistCardStates();
});
