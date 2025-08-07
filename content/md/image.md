# Image

Displays a single image with preview and tranformation options.

## Import [#](https://primevue.org/image/#import)

```

import Image from 'primevue/image';


```

## Basic [#](https://primevue.org/image/#basic)

Image is used similar to the standard *img* element.

```

<Image src="/image.jpg" alt="Image" width="250" />


```

## Preview [#](https://primevue.org/image/#preview)

Enabling *preview* mode displays a modal layer when the image is clicked to provide transformation options such as rotating and zooming.

```

<Image src="/image.jpg" alt="Image" width="250" preview />


```

## Template [#](https://primevue.org/image/#template)

An eye icon is displayed by default when the image is hovered in preview mode, use the *previewicon* slot for custom content. In addition, the *image* and *preview* slots are available to define the thumbnail and detailed image respectively.

```

<Image alt="Image" preview>
    <template #previewicon>
        <i class="pi pi-search"></i>
    </template>
    <template #image>
        <img src="/thumbnail.jpg" alt="image" />
    </template>
    <template #preview="slotProps">
        <img src="/image.jpg" alt="preview" :style="slotProps.style" @click="slotProps.onClick" />
    </template>
</Image>


```

## Accessibility [#](https://primevue.org/image/#accessibility)

### Screen Reader

The preview button is a native *button* element with an *aria-label* that refers to the *aria.zoomImage* property of the [locale](https://primevue.org/configuration/#locale) API by default, with *previewButtonProps* you may use your own aria roles and attributes as any valid attribute is passed to the button element implicitly.

When preview is active, *dialog* role with *aria-modal* is applied to the overlay image container.

Button controls use *aria.rotateRight*, *aria.rotateLeft*, *aria.zoomIn*, *aria.zoomOut* and *aria.close* from the [locale](https://primevue.org/configuration/#locale) API as *aria-label*.

### ButtonBar Keyboard Support

When preview is activated, close button receives the initial focus.

| Key | Function |
| --- | --- |
| *tab* | Moves focus through button bar. |
| *enter* | Activates the button. |
| *space* | Activates the button. |
| *esc* | Closes the image preview. |