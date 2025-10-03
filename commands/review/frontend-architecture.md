---
description: "Review frontend components, state management, build optimization, and framework patterns"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7", "mcp__playwright__browser_snapshot"]
complexity: "moderate"
github_integration: true
---

# Command: Review Frontend Architecture

## Purpose

Evaluate frontend changes for component architecture, state management patterns, build optimization,
framework-specific best practices, performance, and developer experience.

## Usage

**Local:** `/review:frontend-architecture [feature-branch] [base-branch]`
**GitHub:** Automatically triggered by AI Code Review workflow on PR open/sync

## Process

1. **Fetch latest code:**

   ```bash
   git fetch origin
   git checkout origin/[feature-branch]
   ```

2. **Compute diff:**

   ```bash
   git diff --name-only --diff-filter=M origin/[base-branch]...origin/[feature-branch]
   # Focus on: .jsx, .tsx, .vue, components/, pages/, store/, state/, hooks/
   ```

3. **Parallel Frontend Architecture Analysis:**
   Launch 6 concurrent specialized frontend review tasks:

   ```python
   # Component architecture
   Task("Review component architecture for composition patterns, props design, component hierarchy, reusability, and separation of concerns")

   # State management
   Task("Analyze state management for Redux/Vuex/Pinia patterns, context usage, props drilling, state normalization, and data flow architecture")

   # Build optimization
   Task("Evaluate build optimization including code splitting, lazy loading, bundle size, tree shaking, and dynamic imports")

   # Framework-specific patterns
   Task("Review framework patterns for React hooks/lifecycle, Vue composition API, Angular services, custom hooks, and framework best practices")

   # Frontend performance
   Task("Analyze frontend performance for re-render optimization, memoization, virtual scrolling, image optimization, and runtime performance")

   # Developer experience
   Task("Assess developer experience including TypeScript usage, error boundaries, prop types, dev tools integration, and debugging capabilities")
   ```

4. **Evaluate against frontend criteria:**
   - **Component Architecture:** Composition, props design, smart vs presentational, hooks, lifecycle
   - **State Management:** Store patterns, state normalization, selectors, actions, reducers, context
   - **Build Optimization:** Code splitting, lazy loading, bundle analysis, tree shaking, chunks
   - **Framework Patterns:** Hooks, composition API, services, directives, custom implementations
   - **Performance:** Re-renders, memoization, virtualization, code splitting, asset optimization
   - **Developer Experience:** TypeScript, error handling, prop validation, linting, dev tools
   - Use Context7 MCP for framework-specific best practices (React, Vue, Angular, Svelte)

5. **Report findings with severity and reasoning:**
   - Critical: Performance issues causing poor UX, security vulnerabilities, broken functionality
   - Major: Poor architecture, significant performance impact, maintainability issues
   - Minor: Best practice deviations, optimization opportunities, DX improvements
   - Enhancement: Well-architected components and efficient patterns

6. **Include positive observations:**
   - Highlight clean component composition
   - Acknowledge efficient state management
   - Recognize good build optimization

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for end users
- Engineering approach: Framework, state solution, key architectural patterns

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the frontend architecture problem
  - **Reasoning:** Why this matters (UX impact, performance, maintainability)
  - **Fix:** Concrete suggestion with code snippet if applicable

### Major

[Same structure as Critical]

### Minor

[Same structure as Critical]

### Enhancement

[Positive patterns and optional improvements]

**Highlights:**

- Positive observation 1
- Positive observation 2

## Agent Integration

**Primary Agent:** reviewer - Provides specialized frontend architecture review guidance

**Related Agents:**

- research-analysis-specialist - Can research framework patterns and best practices
- implementation-strategy-specialist - Can suggest refactoring strategies

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested fixes
- Highlights bundle size impacts

### Path-Specific Triggers

Especially valuable for:

- Component files (`components/`, `src/components/`, `app/components/`)
- State management (`store/`, `reducers/`, `actions/`, `state/`)
- Page/route files (`pages/`, `routes/`, `views/`)
- Custom hooks (`hooks/`, `composables/`)

## Examples

### Example 1: React Component Architecture Review

```bash
/review:frontend-architecture feature/product-catalog main
```

**Output:**

```markdown
**High-Level Summary**
This change implements product catalog with filtering and search. Uses React with Redux Toolkit for
state management and React Query for data fetching.

### Critical

- **File:** `src/components/ProductList.tsx:45-85`
  - **Issue:** Component re-renders entire list on every keystroke in search input
  - **Reasoning:** Renders 1000+ products on each keystroke, causes UI lag and poor user experience.
    Users experience 200-500ms delay per keystroke
  - **Fix:** Implement virtualization and debouncing:
    ```typescript
    import { useVirtualizer } from '@tanstack/react-virtual';
    import { useDebouncedValue } from '@/hooks/useDebounce';

    const debouncedSearch = useDebouncedValue(searchTerm, 300);

    const virtualizer = useVirtualizer({
      count: filteredProducts.length,
      getScrollElement: () => parentRef.current,
      estimateSize: () => 100,
    });
    ```

### Major

- **File:** `src/store/productsSlice.ts:120-180`
  - **Issue:** State not normalized, storing nested product categories causing duplication
  - **Reasoning:** Same category data duplicated across products, causes inconsistencies when category
    updates and increases state size unnecessarily
  - **Fix:** Normalize state with entity adapter:
    ```typescript
    import { createEntityAdapter } from '@reduxjs/toolkit';

    const productsAdapter = createEntityAdapter<Product>();
    const categoriesAdapter = createEntityAdapter<Category>();

    // Store categories separately
    const categoriesSlice = createSlice({
      name: 'categories',
      initialState: categoriesAdapter.getInitialState(),
      reducers: {
        categoriesReceived: categoriesAdapter.setAll,
      }
    });

    // Products reference category IDs
    const productsSlice = createSlice({
      name: 'products',
      initialState: productsAdapter.getInitialState(),
      // products store categoryId instead of full category object
    });
    ```

- **File:** `src/components/ProductCard.tsx:34-67`
  - **Issue:** Inline function callbacks in map causing unnecessary re-renders
  - **Reasoning:** Creates new function on every render, breaks React.memo optimization.
    All 1000+ ProductCards re-render on unrelated state changes
  - **Fix:** Use useCallback or move handler to parent:
    ```typescript
    const ProductList = () => {
      const handleProductClick = useCallback((id: string) => {
        navigate(`/products/${id}`);
      }, [navigate]);

      return products.map(product => (
        <ProductCard
          key={product.id}
          product={product}
          onClick={handleProductClick}
        />
      ));
    };

    const ProductCard = React.memo(({ product, onClick }) => {
      return <div onClick={() => onClick(product.id)}>...</div>;
    });
    ```

- **File:** `src/pages/Catalog.tsx:45-50`
  - **Issue:** Loading entire product images upfront without lazy loading
  - **Reasoning:** Loads 1000+ high-res images immediately, causes 10+ seconds initial load time
    and wastes bandwidth for images below fold
  - **Fix:** Implement lazy loading with Intersection Observer:
    ```typescript
    import { LazyLoadImage } from 'react-lazy-load-image-component';

    <LazyLoadImage
      src={product.imageUrl}
      alt={product.name}
      effect="blur"
      threshold={100}
    />
    ```

### Minor

- **File:** `src/hooks/useProductFilter.ts:23-45`
  - **Issue:** Complex filtering logic in component hook, not testable independently
  - **Reasoning:** Makes unit testing difficult, couples filtering logic to React
  - **Fix:** Extract pure function:
    ```typescript
    // utils/productFilters.ts
    export const filterProducts = (products, filters) => {
      // pure function, easily testable
    };

    // hooks/useProductFilter.ts
    export const useProductFilter = (products) => {
      const filters = useSelector(selectFilters);
      return useMemo(
        () => filterProducts(products, filters),
        [products, filters]
      );
    };
    ```

- **File:** `webpack.config.js:0`
  - **Issue:** No code splitting configuration for large dependencies
  - **Reasoning:** Bundles all dependencies into single chunk, increases initial load time
  - **Fix:** Configure splitChunks:
    ```javascript
    optimization: {
      splitChunks: {
        chunks: 'all',
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            priority: -10,
          },
          common: {
            minChunks: 2,
            priority: -20,
          }
        }
      }
    }
    ```

**Highlights:**
- Excellent use of React Query for server state management
- Proper TypeScript types with strict mode enabled
- Clean separation of presentation and container components
- Good error boundary implementation for component tree isolation
```

### Example 2: Vue 3 Composition API Review

```bash
/review:frontend-architecture feature/dashboard-widgets develop
```

**Output:**

```markdown
**High-Level Summary**
This change implements dashboard widgets with real-time updates. Uses Vue 3 Composition API with
Pinia for state management and WebSocket for live data.

### Critical

- **File:** `src/components/AnalyticsWidget.vue:67-95`
  - **Issue:** WebSocket connection not cleaned up on component unmount
  - **Reasoning:** Creates memory leak, opens new connection on every mount without closing previous.
    After navigation, accumulates connections causing performance degradation
  - **Fix:** Add cleanup in onUnmounted:
    ```typescript
    import { onMounted, onUnmounted } from 'vue';

    const socket = ref<WebSocket | null>(null);

    onMounted(() => {
      socket.value = new WebSocket(WS_URL);
      socket.value.onmessage = handleMessage;
    });

    onUnmounted(() => {
      socket.value?.close();
      socket.value = null;
    });
    ```

### Major

- **File:** `src/stores/analytics.ts:45-89`
  - **Issue:** Using reactive() for large arrays instead of ref(), causing deep reactivity overhead
  - **Reasoning:** Vue deep-watches every object in 10,000+ item array, causes severe performance
    degradation on updates (500ms+ freeze on data changes)
  - **Fix:** Use shallowRef for large arrays:
    ```typescript
    import { shallowRef, triggerRef } from 'vue';

    // Instead of: const data = reactive({ items: [] })
    const items = shallowRef<AnalyticsData[]>([]);

    // Trigger updates manually after modifications
    items.value = [...items.value, newItem];
    triggerRef(items);
    ```

- **File:** `src/composables/useRealTimeData.ts:34-67`
  - **Issue:** Composable returns reactive objects instead of readonly refs
  - **Reasoning:** Allows components to accidentally mutate state directly, bypassing Pinia store
    actions and breaking reactivity patterns
  - **Fix:** Return readonly refs:
    ```typescript
    import { readonly, toRefs } from 'vue';

    export function useRealTimeData() {
      const store = useAnalyticsStore();

      return {
        ...toRefs(readonly(store.state)),
        // expose only actions, not state mutations
        subscribe: store.subscribe,
        unsubscribe: store.unsubscribe
      };
    }
    ```

**Highlights:**
- Excellent use of provide/inject for theme context
- Proper TypeScript integration with defineComponent
- Smart use of computed properties for derived state
- Good composable structure following Vue 3 patterns
```

### Example 3: Build Optimization Review

```bash
/review:frontend-architecture feature/improve-load-time main
```

**Output:**

```markdown
**High-Level Summary**
This change optimizes application load time through code splitting and asset optimization. Uses
Vite with lazy-loaded routes and optimized chunks.

### Major

- **File:** `vite.config.ts:45-60`
  - **Issue:** No manual chunk splitting for large vendor libraries
  - **Reasoning:** Moment.js (500KB) and lodash (300KB) bundled in main chunk, slows initial load.
    Users wait 3+ seconds for libraries they don't immediately need
  - **Fix:** Manual chunk configuration:
    ```typescript
    export default defineConfig({
      build: {
        rollupOptions: {
          output: {
            manualChunks: {
              'vendor-heavy': ['moment', 'lodash'],
              'charts': ['chart.js', 'recharts'],
              'ui': ['@mui/material', '@emotion/react'],
            }
          }
        }
      }
    });
    ```

- **File:** `src/routes/index.ts:12-45`
  - **Issue:** All routes imported synchronously, no lazy loading
  - **Reasoning:** Loads code for all pages upfront, increases initial bundle from 50KB to 500KB
  - **Fix:** Lazy load route components:
    ```typescript
    const routes = [
      {
        path: '/',
        component: () => import('@/pages/Home.vue')
      },
      {
        path: '/dashboard',
        component: () => import('@/pages/Dashboard.vue')
      }
    ];
    ```

**Highlights:**
- Excellent use of dynamic imports for feature modules
- Smart preloading strategy for likely-next routes
- Optimized asset pipeline with image compression
```

## Integration Points

- **Input:** Git branches (feature vs base)
- **Dependencies:** Context7 for framework best practices, Playwright for runtime analysis
- **Output:** Frontend architecture review findings
- **Related Reviews:** design, performance, readability, architecture
- **Follow-up:**
  - Use `/review:design` for UI/UX compliance
  - Use `/review:performance` for runtime performance deep dive
  - Use `/fix:bug-quickly` for critical issues

## Quality Standards

- **Architecture Quality:** Enforce composition patterns and separation of concerns
- **State Management:** Validate state normalization and data flow patterns
- **Build Efficiency:** Identify bundle optimization opportunities
- **Framework Compliance:** Follow framework-specific best practices
- **Performance Focus:** Prioritize re-render optimization and asset loading

## Frontend Technology Coverage

**Supported Frameworks:**

- React (with hooks, class components)
- Vue 3 (Composition API, Options API)
- Angular (modern versions)
- Svelte
- Next.js (React framework)
- Nuxt (Vue framework)

**State Management:**

- Redux / Redux Toolkit
- Zustand
- Pinia (Vue)
- Vuex (Vue)
- NgRx (Angular)
- MobX
- Context API (React)

**Build Tools:**

- Vite
- Webpack
- Rollup
- esbuild
- Turbopack

**Framework Integration:**

- Uses Context7 to fetch latest framework documentation
- Adapts recommendations based on detected framework and version
- Provides framework-specific code examples
