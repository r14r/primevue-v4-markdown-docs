# Galleria

Galleria is a content gallery component.

## Import [#](https://primevue.org/galleria/#import)

```

import Galleria from 'primevue/galleria';


```

## Basic [#](https://primevue.org/galleria/#basic)

Galleria requires a *value* as a collection of images, *item* template for the higher resolution image and *thumbnail* template to display as a thumbnail.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" />
    </template>
</Galleria>


```

## Controlled [#](https://primevue.org/galleria/#controlled)

Galleria can be controlled programmatically using a binding to *activeIndex*.

```

<div>
    <Button icon="pi pi-minus" @click="prev" />
    <Button icon="pi pi-plus" @click="next" severity="secondary" class="ml-2" />
</div>

<Galleria v-model:activeIndex="activeIndex" :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" />
    </template>
</Galleria>


```

## Indicator [#](https://primevue.org/galleria/#indicator)

Indicators allow quick navigation between the items.

### Click Event [#](https://primevue.org/galleria/#indicatorbasic)

Indicators are displayed at the bottom by enabling *showIndicators* property and interacted with the click event by default.

```

<Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px"
    :showThumbnails="false" :showIndicators="true">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
</Galleria>


```

### Hover Event [#](https://primevue.org/galleria/#indicatorhoverevent)

Indicators can be activated on hover instead of click if *changeItemOnIndicatorHover* is added.

```

<Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px"
    :showThumbnails="false" :showIndicators="true" :changeItemOnIndicatorHover="true">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
</Galleria>


```

### Position [#](https://primevue.org/galleria/#indicatorposition)

Indicators can be placed at four different sides using the *indicatorsPosition* property. In addition, enabling *showIndicatorsOnItem* moves the indicators inside the image section.

```

<Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px" :showThumbnails="false"
    :showIndicators="true" :changeItemOnIndicatorHover="true" :showIndicatorsOnItem="inside" :indicatorsPosition="position">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
</Galleria>


```

### Template [#](https://primevue.org/galleria/#indicatortemplate)

Indicator content can be customized with the *indicator* property that takes an index as a parameter and expects content.

```

<Galleria :value="images" :numVisible="5" containerStyle="max-width: 640px" :showThumbnails="false"
    :showIndicators="true" :changeItemOnIndicatorHover="true" :showIndicatorsOnItem="true" indicatorsPosition="left">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #indicator="{ index }">
        <span style="color: '#ffffff', cursor: pointer">{{ index + 1 }}</span>
    </template>
</Galleria>


```

## Thumbnail [#](https://primevue.org/galleria/#thumbnail)

Thumbnails represent a smaller version of the actual content.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :thumbnailsPosition="position" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <div class="grid gap-4 justify-center">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block;" />
        </div>
    </template>
</Galleria>


```

## Responsive [#](https://primevue.org/galleria/#responsive)

Settings per screen size is defined via the *responsiveOptions* property.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :circular="true" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
</Galleria>


```

## Full Screen [#](https://primevue.org/galleria/#fullscreen)

In fullscreen mode content covers the whole page over a modal layer.

### With Thumbnails [#](https://primevue.org/galleria/#fullscreenwiththumbnail)

Full screen mode is enabled by adding *fullScreen* property and and visibility is controlled with a binding to *visible* property.

```

<Galleria v-model:visible="displayBasic" :value="images" :responsiveOptions="responsiveOptions" :numVisible="9" containerStyle="max-width: 50%" :circular="true" :fullScreen="true" :showItemNavigators="true">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
    </template>
</Galleria>

<Button label="Show" icon="pi pi-external-link" @click="displayBasic = true" />


```

### Without Thumbnails [#](https://primevue.org/galleria/#fullscreenwithoutthumnails)

Thumbnails can also be hidden in full screen mode.

```

<Galleria v-model:visible="displayBasic" :value="images" :responsiveOptions="responsiveOptions" :numVisible="9" containerStyle="max-width: 50%" :circular="true" :fullScreen="true" :showItemNavigators="true"  :showThumbnails="false">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
    </template>
</Galleria>

<Button label="Show" icon="pi pi-external-link" @click="displayBasic = true" />


```

### Custom Content [#](https://primevue.org/galleria/#fullscreencustom)

Using *activeIndex*, Galleria is displayed with a specific initial image.

```

<Galleria v-model:activeIndex="activeIndex" v-model:visible="displayCustom" :value="images" :responsiveOptions="responsiveOptions" :numVisible="7"
    containerStyle="max-width: 850px" :circular="true" :fullScreen="true" :showItemNavigators="true" :showThumbnails="false">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
    </template>
</Galleria>


```

## Navigator [#](https://primevue.org/galleria/#navigator)

Navigators are used to move back and forth between the images.

### With Thumbnails [#](https://primevue.org/galleria/#itemthumbnails)

Add *showItemNavigators* to display navigator elements and the left and right side.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :circular="true" containerStyle="max-width: 640px"
    :showItemNavigators="true">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block;" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block;" />
    </template>
</Galleria>


```

### Without Thumbnails [#](https://primevue.org/galleria/#itemwithouthumbnails)

Simple example with navigators only.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :circular="true" containerStyle="max-width: 640px"
    :showItemNavigators="true" :showThumbnails="false">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block;" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block;" />
    </template>
</Galleria>


```

### Display on Hover [#](https://primevue.org/galleria/#itemhover)

Navigators are displayed on hover only if *showItemNavigatorsOnHover* is enabled.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :circular="true" containerStyle="max-width: 640px" :showItemNavigators="true" :showItemNavigatorsOnHover="true">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
    </template>
</Galleria>


```

### With Indicators [#](https://primevue.org/galleria/#indicators)

Navigators and Indicators can be combined as well.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :circular="true" containerStyle="max-width: 640px"
    :showItemNavigators="true" :showThumbnails="false" :showItemNavigatorsOnHover="true" :showIndicators="true">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block;" />
    </template>
    <template #thumbnail="slotProps">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block;" />
    </template>
</Galleria>


```

## AutoPlay [#](https://primevue.org/galleria/#autoplay)

A slideshow implementation is defined by adding *circular* and *autoPlay* properties.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" containerStyle="max-width: 640px"
    :circular="true" :autoPlay="true" :transitionInterval="2000">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
    </template>
</Galleria>


```

## Caption [#](https://primevue.org/galleria/#caption)

Description of an image is specified with the *caption* property that takes the displayed object and returns content.

```

<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
    </template>
    <template #caption="slotProps">
        <div class="text-xl mb-2 font-bold">{{ slotProps.item.title }}</div>
        <p class="text-white">{{ slotProps.item.alt }}</p>
    </template>
</Galleria>


```

## Advanced [#](https://primevue.org/galleria/#advanced)

Advanced Galleria implementation with a custom UI.

```

<Galleria
    ref="galleria"
    v-model:activeIndex="activeIndex"
    :value="images"
    :numVisible="5"
    containerStyle="max-width: 640px"
    :showThumbnails="showThumbnails"
    :showItemNavigators="true"
    :showItemNavigatorsOnHover="true"
    :circular="true"
    :autoPlay="isAutoPlay"
    :transitionInterval="3000"
    :responsiveOptions="responsiveOptions"
    :pt="{
        root: {
            class: [{ 'flex flex-col': fullScreen }]
        },
        content: {
            class: ['relative', { 'flex-1 justify-center': fullScreen }]
        },
        thumbnails: 'absolute w-full left-0 bottom-0'
    }"
>
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" :style="[{ width: !fullScreen ? '100%' : '', display: !fullScreen ? 'block' : '' }]" />
    </template>
    <template #thumbnail="slotProps">
        <div class="grid gap-4 justify-center">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
        </div>
    </template>
    <template #footer>
        <div class="flex items-stretch bg-surface-950 text-white h-10">
            <button type="button" @click="onThumbnailButtonClick" class="bg-transparent border-none rounded-none hover:bg-white/10 text-white inline-flex justify-center items-center cursor-pointer px-3">
                <i class="pi pi-th-large"></i>
            </button>
            <button type="button" @click="toggleAutoSlide" class="bg-transparent border-none rounded-none hover:bg-white/10 text-white inline-flex justify-center items-center cursor-pointer px-3"><i :class="slideButtonIcon"></i></button>
            <span v-if="images" class="flex items-center gap-4 ml-3">
                <span class="text-sm">{{ activeIndex + 1 }}/{{ images.length }}</span>
                <span class="font-bold text-sm">{{ images[activeIndex].title }}</span>
                <span class="text-sm">{{ images[activeIndex].alt }}</span>
            </span>
            <button type="button" @click="toggleFullScreen" class="bg-transparent border-none rounded-none hover:bg-white/10 text-white inline-flex justify-center items-center cursor-pointer px-3 ml-auto">
                <i :class="fullScreenIcon"></i>
            </button>
        </div>
    </template>
</Galleria>


```

## Accessibility [#](https://primevue.org/galleria/#accessibility)

### Screen Reader

Galleria uses *region* role and since any attribute is passed to the main container element, attributes such as *aria-label* and *aria-roledescription* can be used as well. The slides container has *aria-live* attribute set as "polite" if galleria is not in autoplay mode, otherwise "off" would be the value in autoplay.

A slide has a *group* role with an aria-label that refers to the *aria.slideNumber* property of the [locale](https://primevue.org/configuration/#locale) API. Similarly *aria.slide* is used as the *aria-roledescription* of the item. Inactive slides are hidden from the readers with *aria-hidden*.

Next and Previous navigators are button elements with *aria-label* attributes referring to the *aria.prevPageLabel* and *aria.nextPageLabel* properties of the [locale](https://primevue.org/configuration/#locale) API by default respectively, you may still use your own aria roles and attributes as any valid attribute is passed to the button elements implicitly by using *nextButtonProps* and *prevButtonProps*.

Quick navigation elements and thumnbails follow the tab pattern. They are placed inside an element with a *tablist* role whereas each item has a *tab* role with *aria-selected* and *aria-controls* attributes. The *aria-label* attribute of a quick navigation item refers to the *aria.pageLabel* of the [locale](https://primevue.org/configuration/#locale) API. Current page is marked with *aria-current*.

In full screen mode, modal element uses *dialog* role with *aria-modal* enabled. The close button retrieves *aria-label* from the *aria.close* property of the [locale](https://primevue.org/configuration/#locale) API.

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