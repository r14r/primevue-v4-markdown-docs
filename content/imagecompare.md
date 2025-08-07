# ImageCompare

Compare two images side by side with a slider.

## Import [#](https://primevue.org/imagecompare/#import)

```

import ImageCompare from 'primevue/imagecompare';


```

## Basic [#](https://primevue.org/imagecompare/#basic)

Images are defined using templating with *left* and *right* slots. Use the *style* or *class* properties to define the size of the container.

```

<ImageCompare class="shadow-lg rounded-2xl">
    <template #left>
        <img src="~/assets/images/island1.jpg" />
    </template>
    <template #right>
        <img src="~/assets/images/island2.jpg" />
    </template>
</ImageCompare>


```

## Responsive [#](https://primevue.org/imagecompare/#responsive)

Apply responsive styles to the container element to optimize display per screen size.

```

<ImageCompare class="sm:!w-96 shadow-lg rounded-2xl">
    <template #left>
        <img src="~/assets/images/island1.jpg" />
    </template>
    <template #right>
        <img src="~/assets/images/island2.jpg" />
    </template>
</ImageCompare>


```

## Accessibility [#](https://primevue.org/imagecompare/#accessibility)

### Screen Reader

ImageComponent component uses a native range *slider* internally. Value to describe the component can be defined using *aria-labelledby* and *aria-label* props.

```

<span id="image_label">Compare Images</span>
<ImageCompare class="shadow-lg rounded-2xl" aria-labelledby="image-label">
    ...
</ImageCompare>

<ImageCompare class="shadow-lg rounded-2xl" aria-label="Compare Images">
    ...
</ImageCompare>


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the component. |
| *left arrow**up arrow* | Decrements the value. |
| *right arrow**down arrow* | Increments the value. |
| *home* | Set the minimum value. |
| *end* | Set the maximum value. |
| *page up* | Increments the value by 10 steps. |
| *page down* | Decrements the value by 10 steps. |