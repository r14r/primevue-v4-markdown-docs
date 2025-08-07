# Carousel

Carousel is a content slider featuring various customization options.

## Import [#](https://primevue.org/carousel/#import)

```

import Carousel from 'primevue/carousel';


```

## Basic [#](https://primevue.org/carousel/#basic)

Carousel requires a collection of items as its value along with a template to render each item.

No available options

```

<Carousel :value="products" :numVisible="3" :numScroll="3" :responsiveOptions="responsiveOptions">
    <template #item="slotProps">
        <div class="border border-surface-200 dark:border-surface-700 rounded m-2  p-4">
            <div class="mb-4">
                <div class="relative mx-auto">
                    <img :src="'https://primefaces.org/cdn/primevue/images/product/' + slotProps.data.image" :alt="slotProps.data.name" class="w-full rounded" />
                    <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data.inventoryStatus)" class="absolute" style="left:5px; top: 5px"/>
                </div>
            </div>
            <div class="mb-4 font-medium">{{ slotProps.data.name }}</div>
            <div class="flex justify-between items-center">
                <div class="mt-0 font-semibold text-xl">${{ slotProps.data.price }}</div>
                <span>
                    <Button icon="pi pi-heart" severity="secondary" variant="outlined" />
                    <Button icon="pi pi-shopping-cart" class="ml-2"/>
                </span>
            </div>
        </div>
    </template>
</Carousel>


```

## Circular [#](https://primevue.org/carousel/#circular)

When *autoplayInterval* is defined in milliseconds, items are scrolled automatically. In addition, for infinite scrolling *circular* property needs to be added which is enabled automatically in auto play mode.

No available options

```

<Carousel :value="products" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions" circular :autoplayInterval="3000">
    <template #item="slotProps">
        <div class="border border-surface-200 dark:border-surface-700 rounded m-2  p-4">
            <div class="mb-4">
                <div class="relative mx-auto">
                    <img :src="'https://primefaces.org/cdn/primevue/images/product/' + slotProps.data.image" :alt="slotProps.data.name" class="w-full rounded" />
                    <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data.inventoryStatus)" class="absolute" style="left:5px; top: 5px"/>
                </div>
            </div>
            <div class="mb-4 font-medium">{{ slotProps.data.name }}</div>
            <div class="flex justify-between items-center">
                <div class="mt-0 font-semibold text-xl">${{ slotProps.data.price }}</div>
                <span>
                    <Button icon="pi pi-heart" severity="secondary" variant="outlined" />
                    <Button icon="pi pi-shopping-cart" class="ml-2"/>
                </span>
            </div>
        </div>
    </template>
</Carousel>


```

## Responsive [#](https://primevue.org/carousel/#responsive)

Carousel supports specific configuration per screen size with the *responsiveOptions* property that takes an array of objects where each object defines the max-width *breakpoint*, *numVisible* for the number of items items per page and *numScroll* for number of items to scroll. When *responsiveOptions* is defined, the *numScroll* and *numVisible* properties of the Carousel are used as default when there is breakpoint that applies.

No available options

```

<Carousel :value="products" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions">
    <template #item="slotProps">
        <div class="border border-surface-200 dark:border-surface-700 rounded m-2  p-4">
            <div class="mb-4">
                <div class="relative mx-auto">
                    <img :src="'https://primefaces.org/cdn/primevue/images/product/' + slotProps.data.image" :alt="slotProps.data.name" class="w-full rounded" />
                    <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data.inventoryStatus)" class="absolute" style="left:5px; top: 5px"/>
                </div>
            </div>
            <div class="mb-4 font-medium">{{ slotProps.data.name }}</div>
            <div class="flex justify-between items-center">
                <div class="mt-0 font-semibold text-xl">${{ slotProps.data.price }}</div>
                <span>
                    <Button icon="pi pi-heart" severity="secondary" variant="outlined" />
                    <Button icon="pi pi-shopping-cart" class="ml-2"/>
                </span>
            </div>
        </div>
    </template>
</Carousel>


```

## Vertical [#](https://primevue.org/carousel/#vertical)

To create a vertical Carousel, *orientation* needs to be set to *vertical* along with a *verticalViewPortHeight*.

No available options

```

<Carousel :value="products" :numVisible="1" :numScroll="1" orientation="vertical" verticalViewPortHeight="330px" containerClass="flex items-center">
    <template #item="slotProps">
        <div class="border border-surface-200 dark:border-surface-700 rounded m-2  p-4">
            <div class="mb-4">
                <div class="relative mx-auto">
                    <img :src="'https://primefaces.org/cdn/primevue/images/product/' + slotProps.data.image" :alt="slotProps.data.name" class="w-full rounded" />
                    <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data.inventoryStatus)" class="absolute" style="left:5px; top: 5px"/>
                </div>
            </div>
            <div class="mb-4 font-medium">{{ slotProps.data.name }}</div>
            <div class="flex justify-between items-center">
                <div class="mt-0 font-semibold text-xl">${{ slotProps.data.price }}</div>
                <span>
                    <Button icon="pi pi-heart" severity="secondary" variant="outlined" />
                    <Button icon="pi pi-shopping-cart" class="ml-2"/>
                </span>
            </div>
        </div>
    </template>
</Carousel>


```

## Accessibility [#](https://primevue.org/carousel/#accessibility)

### Screen Reader

Carousel uses *region* role and since any attribute is passed to the main container element, attributes such as *aria-label* and *aria-roledescription* can be used as well. The slides container has *aria-live* attribute set as "polite" if carousel is not in autoplay mode, otherwise "off" would be the value in autoplay.

A slide has a *group* role with an aria-label that refers to the *aria.slideNumber* property of the [locale](https://primevue.org/configuration/#locale) API. Similarly *aria.slide* is used as the *aria-roledescription* of the item. Inactive slides are hidden from the readers with *aria-hidden*.

Next and Previous navigators are button elements with *aria-label* attributes referring to the *aria.prevPageLabel* and *aria.nextPageLabel* properties of the [locale](https://primevue.org/configuration/#locale) API by default respectively, you may still use your own aria roles and attributes as any valid attribute is passed to the button elements implicitly by using *nextButtonProps* and *prevButtonProps*.

Quick navigation elements are button elements with an *aria-label* attribute referring to the *aria.pageLabel* of the [locale](https://primevue.org/configuration/#locale) API. Current page is marked with *aria-current*.

### Next/Prev Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through interactive elements in the carousel. |
| *enter* | Activates navigation. |
| *space* | Activates navigation. |

### Quick Navigation Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through the active slide link. |
| *enter* | Activates the focused slide link. |
| *space* | Activates the focused slide link. |
| *right arrow* | Moves focus to the next slide link. |
| *left arrow* | Moves focus to the previous slide link. |
| *home* | Moves focus to the first slide link. |
| *end* | Moves focus to the last slide link. |