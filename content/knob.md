# Knob

Knob is a form component to define number inputs with a dial.

## Import [#](https://primevue.org/knob/#import)

```

import Knob from 'primevue/knob';


```

## Basic [#](https://primevue.org/knob/#basic)

Knob is used with the *v-model* property for two-way value binding.

0

```

<Knob v-model="value" />


```

## Forms [#](https://primevue.org/knob/#forms)

Knob integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

15

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col items-center gap-1">
        <Knob name="knob" />
        <Message v-if="$form.knob?.invalid" severity="error" size="small" variant="simple">{{ $form.knob.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Min/Max [#](https://primevue.org/knob/#minmax)

Boundaries are configured with the *min* and *max* values whose defaults are 0 and 100 respectively.

10

```

<Knob v-model="value" :min="-50" :max="50" />


```

## Step [#](https://primevue.org/knob/#step)

Step factor is 1 by default and can be customized with *step* option.

40

```

<Knob v-model="value5" :step="10" />


```

## Template [#](https://primevue.org/knob/#template)

The label can be customized with the *valueTemplate* property using either a template string or a function.

60%

```

<Knob v-model="value" valueTemplate="{value}%" />


```

## Stroke [#](https://primevue.org/knob/#stroke)

The border size is specified with the *stroke* property as a number in pixels.

40

```

<Knob v-model="value" :strokeWidth="5" />


```

## Size [#](https://primevue.org/knob/#size)

Diameter of the knob is defined in pixels using the *size* property.

60

```

<Knob v-model="value" :size="200" />


```

## Color [#](https://primevue.org/knob/#color)

*valueColor* defines the value color, *rangeColor* defines the range background and similarly *textColor* configures the color of the value text. In addition, *strokeWidth* is used to determine the width of the stroke of range and value sections.

50

```

<Knob v-model="value" valueColor="SlateGray" rangeColor="MediumTurquoise" />


```

## Reactive [#](https://primevue.org/knob/#reactive)

Knob can be controlled with custom controls as well.

0

```

<Knob v-model="value" :size="150" readonly />
<div class="flex gap-2">
    <Button icon="pi pi-plus" @click="value++" :disabled="value >= 100" />
    <Button icon="pi pi-minus" @click="value--" :disabled="value <= 0" />
</div>


```

## ReadOnly [#](https://primevue.org/knob/#readonly)

When *readonly* present, value cannot be edited.

50

```

<Knob v-model="value" readonly />


```

## Disabled [#](https://primevue.org/knob/#disabled)

When *disabled* is present, a visual hint is applied to indicate that the Knob cannot be interacted with.

50

```

<Knob v-model="value" disabled />


```

## Accessibility [#](https://primevue.org/knob/#accessibility)

### Screen Reader

Knob element component uses *slider* role in addition to the *aria-valuemin*, *aria-valuemax* and *aria-valuenow* attributes. Value to describe the component can be defined using *aria-labelledby* and *aria-label* props.

```

<span id="label_number">Number</span>
<Knob aria-labelledby="label_number" />

<Knob aria-label="Number" />


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the slider. |
| *left arrow**down arrow* | Decrements the value. |
| *right arrow**up arrow* | Increments the value. |
| *home* | Set the minimum value. |
| *end* | Set the maximum value. |
| *page up* | Increments the value by 10 steps. |
| *page down* | Decrements the value by 10 steps. |