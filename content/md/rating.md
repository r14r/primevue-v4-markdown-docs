# Rating

Rating component is a star based selection input.

## Import [#](https://primevue.org/rating/#import)

```

import Rating from 'primevue/rating';


```

## Basic [#](https://primevue.org/rating/#basic)

Rating is used with the *v-model* property for two-way value binding.

```

<Rating v-model="value" />


```

## Forms [#](https://primevue.org/rating/#forms)

Rating integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-40">
    <div class="flex flex-col items-center gap-2">
        <Rating name="rating" />
        <Message v-if="$form.rating?.invalid" severity="error" size="small" variant="simple">{{ $form.rating.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Number of Stars [#](https://primevue.org/rating/#numberofstars)

Number of stars to display is defined with *stars* property.

```

<Rating v-model="value" :stars="10" />


```

## Template [#](https://primevue.org/rating/#template)

Custom icons are used to override the default icons with *onicon*, *officon* and *cancelicon* slots.

```

<Rating v-model="value">
    <template #onicon>
        <img src="/images/rating/custom-onicon.png" height="24" width="24" />
    </template>
    <template #officon>
        <img src="/images/rating/custom-officon.png" height="24" width="24" />
    </template>
</Rating>


```

## ReadOnly [#](https://primevue.org/rating/#readonly)

When *readOnly* present, value cannot be edited.

```

<Rating v-model="value" readonly />


```

## Disabled [#](https://primevue.org/rating/#disabled)

When *disabled* is present, a visual hint is applied to indicate that the Knob cannot be interacted with.

```

<Rating v-model="value" disabled />


```

## Accessibility [#](https://primevue.org/rating/#accessibility)

### Screen Reader

Rating component internally uses radio buttons that are only visible to screen readers. The value to read for item is retrieved from the [locale](https://primevue.org/configuration/#locale) API via *star* and *stars* of the *aria* property.

### Keyboard Support

Keyboard interaction is derived from the native browser handling of radio buttons in a group.

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the star representing the value, if there is none then first star receives the focus. |
| *left arrow**up arrow* | Moves focus to the previous star, if there is none then last radio button receives the focus. |
| *right arrow**down arrow* | Moves focus to the next star, if there is none then first star receives the focus. |
| *space* | If the focused star does not represent the value, changes the value to the star value. |