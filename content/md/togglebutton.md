# ToggleButton

ToggleButton is used to select a boolean value using a button.

## Import [#](https://primevue.org/togglebutton/#import)

```

import ToggleButton from 'primevue/togglebutton';


```

## Basic [#](https://primevue.org/togglebutton/#basic)

ToggleButton is used with the *v-model* property for two-way value binding.

Off

```

<ToggleButton v-model="checked" onLabel="On" offLabel="Off" />


```

## Forms [#](https://primevue.org/togglebutton/#forms)

ToggleButton integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Reject All

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col items-center gap-1">
        <ToggleButton name="consent" class="w-48" onLabel="Accept All" offLabel="Reject All" />
        <Message v-if="$form.consent?.invalid" severity="error" variant="simple">{{ $form.consent.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Customized [#](https://primevue.org/togglebutton/#customized)

Icons and Labels can be customized using *onLabel*, *offLabel*, *onIcon* and *offIcon* properties.

Unlocked

```

<ToggleButton v-model="checked" onLabel="Locked" offLabel="Unlocked" onIcon="pi pi-lock" 
    offIcon="pi pi-lock-open" class="w-36" aria-label="Do you confirm" />


```

## Sizes [#](https://primevue.org/togglebutton/#sizes)

ToggleButton provides *small* and *large* sizes as alternatives to the base.

OffOffOff

```

<ToggleButton v-model="value1" onLabel="On" offLabel="Off" size="small" class="min-w-16" />
<ToggleButton v-model="value2" onLabel="On" offLabel="Off" class="min-w-20" />
<ToggleButton v-model="value3" onLabel="On" offLabel="Off" size="large" class="min-w-24" />


```

## Invalid [#](https://primevue.org/togglebutton/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

No

```

<ToggleButton v-model="checked" onIcon="pi pi-check" offIcon="pi pi-times" :invalid="!checked" class="w-full sm:w-40" aria-label="Confirmation" />


```

## Disabled [#](https://primevue.org/togglebutton/#disabled)

When *disabled* is present, the element cannot be edited and focused.

No

```

<ToggleButton v-model="checked" disabled onIcon="pi pi-check" offIcon="pi pi-times"
    class="w-full sm:w-40" aria-label="Confirmation" />


```

## Accessibility [#](https://primevue.org/togglebutton/#accessibility)

### Screen Reader

ToggleButton component uses a native button element as the switch element internally that is only visible to screen readers. Value to describe the component can be defined with *aria-labelledby* or *aria-label* props, it is highly suggested to use either of these props as the component changes the label displayed which will result in screen readers to read different labels when the component receives focus. To prevent this, always provide an aria label that does not change related to state.

```

<span id="rememberme">Remember Me</span>
<ToggleButton aria-labelledby="rememberme" />

<ToggleButton aria-label="Remember Me" />


```

### Keyboard Support

Keyboard interaction is derived from the native browser handling of checkboxs in a group.

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the button. |
| *space* | Toggles the checked state. |