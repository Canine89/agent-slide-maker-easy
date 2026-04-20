# Design System Inspired by Airbnb

## 1. Visual Theme & Atmosphere

Airbnb's website is a warm, photography-forward marketplace that feels like flipping through a travel magazine where every page invites you to book. The design operates on a foundation of pure white (`#ffffff`) with the iconic Rausch Red (`#ff385c`) — named after Airbnb's first street address — serving as the singular brand accent. The result is a clean, airy canvas where listing photography, category icons, and the red CTA button are the only sources of color.

The typography uses Airbnb Cereal VF — a custom variable font that's warm and approachable, with rounded terminals that echo the brand's "belong anywhere" philosophy. The font operates in a tight weight range: 500 (medium) for most UI, 600 (semibold) for emphasis, and 700 (bold) for primary headings. Slight negative letter-spacing (-0.18px to -0.44px) on headings creates a cozy, intimate reading experience rather than the compressed efficiency of tech companies.

What distinguishes Airbnb is its palette-based token system (`--palette-*`) and multi-layered shadow approach. The primary card shadow uses a three-layer stack (`rgba(0,0,0,0.02) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 6px, rgba(0,0,0,0.1) 0px 4px 8px`) that creates a subtle, warm lift. Combined with generous border-radius (8px–32px), circular navigation controls (50%), and a category pill bar with horizontal scrolling, the interface feels tactile and inviting — designed for browsing, not commanding.

**Key Characteristics:**
- Pure white canvas with Rausch Red (`#ff385c`) as singular brand accent
- Airbnb Cereal VF — custom variable font with warm, rounded terminals
- Palette-based token system (`--palette-*`) for systematic color management
- Three-layer card shadows: border ring + soft blur + stronger blur
- Generous border-radius: 8px buttons, 14px badges, 20px cards, 32px large elements
- Circular navigation controls (50% radius)
- Photography-first listing cards — images are the hero content
- Near-black text (`#222222`) — warm, not cold
- Luxe Purple (`#460479`) and Plus Magenta (`#92174d`) for premium tiers

## 2. Color Palette & Roles

### Primary Brand
- **Rausch Red** (`#ff385c`): `--palette-bg-primary-core`, primary CTA, brand accent, active states
- **Deep Rausch** (`#e00b41`): `--palette-bg-tertiary-core`, pressed/dark variant of brand red
- **Error Red** (`#c13515`): `--palette-text-primary-error`, error text on light
- **Error Dark** (`#b32505`): `--palette-text-secondary-error-hover`, error hover

### Premium Tiers
- **Luxe Purple** (`#460479`): `--palette-bg-primary-luxe`, Airbnb Luxe tier branding
- **Plus Magenta** (`#92174d`): `--palette-bg-primary-plus`, Airbnb Plus tier branding

### Text Scale
- **Near Black** (`#222222`): `--palette-text-primary`, primary text — warm, not cold
- **Focused Gray** (`#3f3f3f`): `--palette-text-focused`, focused state text
- **Secondary Gray** (`#6a6a6a`): Secondary text, descriptions
- **Disabled** (`rgba(0,0,0,0.24)`): `--palette-text-material-disabled`, disabled state
- **Link Disabled** (`#929292`): `--palette-text-link-disabled`, disabled links

### Interactive
- **Legal Blue** (`#428bff`): `--palette-text-legal`, legal links, informational
- **Border Gray** (`#c1c1c1`): Border color for cards and dividers
- **Light Surface** (`#f2f2f2`): Circular navigation buttons, secondary surfaces

### Surface & Shadows
- **Pure White** (`#ffffff`): Page background, card surfaces
- **Card Shadow** (`rgba(0,0,0,0.02) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 6px, rgba(0,0,0,0.1) 0px 4px 8px`): Three-layer warm lift
- **Hover Shadow** (`rgba(0,0,0,0.08) 0px 4px 12px`): Button hover elevation

## 3. Typography Rules

### Font Family
- **Primary**: `Airbnb Cereal VF`, fallbacks: `Circular, -apple-system, system-ui, Roboto, Helvetica Neue`
- **OpenType Features**: `"salt"` (stylistic alternates) on specific caption elements

### Hierarchy (web baseline — scale up 3–4x for 1920x1080 video slides)

| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| Section Heading | 28px | 700 | 1.43 | normal |
| Card Heading | 22px | 600 | 1.18 | -0.44px |
| Feature Title | 20px | 600 | 1.20 | -0.18px |
| UI Medium | 16px | 500 | 1.25 | normal |
| Button | 16px | 500 | 1.25 | normal |
| Body | 14px | 400 | 1.43 | normal |
| Tag | 12px | 400–700 | 1.33 | normal |
| Badge | 11px | 600 | 1.18 | normal |
| Micro Uppercase | 8px | 700 | 1.25 | 0.32px |

### Principles
- **Warm weight range**: 500–700 dominate. No weight 300/400 for headings.
- **Negative tracking on headings**: -0.18px ~ -0.44px for intimacy.
- **"salt" OpenType feature**: stylistic alternates on badges/captions.

## 4. Component Stylings

### Buttons
- **Primary Dark**: `#222222` bg, `#ffffff` text, 8px radius, 0px 24px padding
- **Circular Nav**: `#f2f2f2` bg, `#222222` text, 50% radius

### Cards
- Background: `#ffffff`
- Radius: 14px (badges), 20px (cards), 32px (large)
- Shadow: `rgba(0,0,0,0.02) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 6px, rgba(0,0,0,0.1) 0px 4px 8px`
- Listing cards: photo on top, details below

### Image Treatment
- Photography fills card top with generous height
- 8–14px radius on contained images

## 5. Layout Principles

- Base spacing: 8px, scale 2/3/4/6/8/10/11/12/15/16/22/24/32
- Generous whitespace ("travel-magazine spacing")
- Border radius scale: 4 / 8 / 14 / 20 / 32 / 50%

## 6. Depth & Elevation

| Level | Treatment |
|-------|-----------|
| Flat | No shadow |
| Card | 3-layer warm stack (border + soft + lift) |
| Hover | `rgba(0,0,0,0.08) 0px 4px 12px` |
| Focus | `rgb(255,255,255) 0px 0px 0px 4px` ring |

## 7. Do's and Don'ts

### Do
- `#222222` (warm near-black) for text — never pure `#000000`
- Rausch Red only for primary CTAs/brand moments — singular accent
- Cereal VF weight 500–700 — warm range is intentional
- 3-layer card shadow for all elevated surfaces
- Generous border-radius: 8px buttons, 20px cards, 50% controls
- Photography as primary visual content
- Negative letter-spacing (-0.18px ~ -0.44px) on headings

### Don't
- Pure black `#000000` for text
- Rausch Red on backgrounds or large surfaces
- Thin weights (300/400) for headings
- Heavy shadows (>0.1 primary layer)
- Sharp corners (0–4px) on cards
- Additional brand colors beyond Rausch/Luxe/Plus

## 9. Agent Prompt Guide

### Quick Reference
- Background: Pure White (`#ffffff`)
- Text: Near Black (`#222222`)
- Brand accent: Rausch Red (`#ff385c`)
- Secondary text: `#6a6a6a`
- Card border ring: `rgba(0,0,0,0.02) 0px 0px 0px 1px`
- Card shadow: full three-layer stack
- Button surface: `#f2f2f2`
