# Slider

Slider is a component to provide input with a drag handle.

## Import [#](https://primevue.org/slider/#import)

```

import Slider from 'primevue/slider';


```

## Basic [#](https://primevue.org/slider/#basic)

Slider is used with the *v-model* property for two-way value binding.

```

<Slider v-model="value" class="w-56" />


```

## Forms [#](https://primevue.org/slider/#forms)

Slider integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full sm:w-56">
    <div class="flex flex-col gap-4">
        <Slider name="slider" />
        <Message v-if="$form.slider?.invalid" severity="error" size="small" variant="simple">{{ $form.slider.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Input [#](https://primevue.org/slider/#input)

Slider is connected to an input field using two-way binding.

```

<InputText v-model.number="value" />
<Slider v-model="value" />


```

## Step [#](https://primevue.org/slider/#step)

Size of each movement is defined with the *step* property.

```

<Slider v-model="value" :step="20" class="w-56" />


```

## Range [#](https://primevue.org/slider/#range)

When *range* property is present, slider provides two handles to define two values. In range mode, value should be an array instead of a single value.

```

<Slider v-model="value" range class="w-56" />


```

## Filter [#](https://primevue.org/slider/#filter)

Image filter implementation using multiple sliders.

ContrastBrightnessSepia

```

<img alt="user header" class="w-full md:w-80 rounded mb-6" src="https://primefaces.org/cdn/primevue/images/card-vue.jpg" :style="filterStyle" />
<SelectButton v-model="filter" :options="filterOptions" optionLabel="label" optionValue="value" class="mb-4" />
<Slider v-model="filterValues[filter]" class="w-56" :min="0" :max="200" />


```

## Vertical [#](https://primevue.org/slider/#vertical)

Default layout of slider is *horizontal*, use *orientation* property for the alternative *vertical* mode.

```

<Slider v-model="value" orientation="vertical" class="h-56" />


```

## Accessibility [#](https://primevue.org/slider/#accessibility)

### Screen Reader

Slider element component uses *slider* role on the handle in addition to the *aria-orientation*, *aria-valuemin*, *aria-valuemax* and *aria-valuenow* attributes. Value to describe the component can be defined using *aria-labelledby* and *aria-label* props.

```

<span id="label_number">Number</span>
<Slider aria-labelledby="label_number" />

<Slider aria-label="Number" />


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the slider. |
| *left arrow**up arrow* | Decrements the value. |
| *right arrow**down arrow* | Increments the value. |
| *home* | Set the minimum value. |
| *end* | Set the maximum value. |
| *page up* | Increments the value by 10 steps. |
| *page down* | Decrements the value by 10 steps. |