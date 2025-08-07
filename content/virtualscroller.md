# VirtualScroller

VirtualScroller is a performant approach to render large amounts of data efficiently.

## Import [#](https://primevue.org/virtualscroller/#import)

```

import VirtualScroller from 'primevue/virtualscroller';


```

## Basic [#](https://primevue.org/virtualscroller/#basic)

VirtualScroller requires *items* as the data to display, *itemSize* for the dimensions of an item and *item* template are required on component. In addition, an initial array is required based on the total number of items to display. Size of the viewport is configured using *scrollWidth*, *scrollHeight* properties directly or with CSS *width* and *height* styles.

```

<VirtualScroller :items="items" :itemSize="50" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">{{ item }}</div>
    </template>
</VirtualScroller>


```

## Horizontal [#](https://primevue.org/virtualscroller/#horizontal)

Setting *orientation* to *horizontal* enables scrolling horizontally. In this case, the *itemSize* should refer to the width of an item.

```

<VirtualScroller :items="items" :itemSize="50" orientation="horizontal" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px" :pt="{ content: 'flex flex-row' }">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="width: 50px; writing-mode: vertical-lr;">{{ item }}</div>
    </template>
</VirtualScroller>


```

## Grid [#](https://primevue.org/virtualscroller/#grid)

Scrolling can be enabled vertically and horizontally when *orientation* is set as *both*. In this mode, *itemSize* should be an array where first value is the height of an item and second is the width.

```

<VirtualScroller :items="items" :itemSize="[50, 100]" orientation="both" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">
            <template v-for="(el, index) of item" :key="index">
                <div style="width: 100px">{{ el }}</div>
            </template>
        </div>
    </template>
</VirtualScroller>


```

## Delay [#](https://primevue.org/virtualscroller/#delay)

The *delay* property adds a threshold to wait in milliseconds during scrolling for render optimization.

No Delay

150ms

500ms

```

<VirtualScroller :items="items" :itemSize="50" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">{{ item }}</div>
    </template>
</VirtualScroller>

<VirtualScroller :items="items" :itemSize="50" :delay="150" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">{{ item }}</div>
    </template>
</VirtualScroller>

<VirtualScroller :items="items" :itemSize="50" :delay="500" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">{{ item }}</div>
    </template>
</VirtualScroller>


```

## Loading [#](https://primevue.org/virtualscroller/#loading)

Busy state is enabled by adding *showLoader* property which blocks the UI with a modal by default. Alternatively, *loader* template can be used to customize items e.g. with [Skeleton](https://primevue.org/skeleton/).

Modal

Skeleton

```

<VirtualScroller :items="items" :itemSize="50" showLoader :delay="250" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">{{ item }}</div>
    </template>
</VirtualScroller>

<VirtualScroller :items="items" :itemSize="50" showLoader :delay="250" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">{{ item }}</div>
    </template>
    <template v-slot:loader="{ options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">
            <Skeleton :width="options.even ? '60%' : '50%'" height="1.3rem" />
        </div>
    </template>
</VirtualScroller>


```

## Lazy [#](https://primevue.org/virtualscroller/#lazy)

Lazy mode is handy to deal with large datasets, instead of loading the entire data, small chunks of data is loaded on demand. To implement lazy loading, enable the *lazy*property and implement *onLazyLoad* callback to return data.

```

<VirtualScroller :items="lazyItems" :itemSize="50" showLoader :delay="250" :loading="lazyLoading" lazy @lazy-load="onLazyLoad" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">{{ item }}</div>
    </template>
</VirtualScroller>


```

## Accessibility [#](https://primevue.org/virtualscroller/#accessibility)

### Screen Reader

VirtualScroller has no specific role is enforced, still you may use any aria role and attributes as any valid attribute is passed to the container element.

### Keyboard Support

Component does not include any built-in interactive elements.