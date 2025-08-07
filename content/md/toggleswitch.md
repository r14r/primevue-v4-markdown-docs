# ToggleSwitch

ToggleSwitch is used to select a boolean value.

## Import [#](https://primevue.org/toggleswitch/#import)

```

import ToggleSwitch from 'primevue/toggleswitch';


```

## Basic [#](https://primevue.org/toggleswitch/#basic)

ToggleSwitch is used with the *v-model* property for two-way value binding.

```

<ToggleSwitch v-model="checked" />


```

## Forms [#](https://primevue.org/toggleswitch/#forms)

ToggleSwitch integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-48">
    <div class="flex flex-col items-center gap-2">
        <ToggleSwitch name="activation" />
        <Message v-if="$form.activation?.invalid" severity="error" size="small" variant="simple">{{ $form.activation.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Preselection [#](https://primevue.org/toggleswitch/#preselection)

Enabling *checked* property displays the component as active initially.

```

<ToggleSwitch v-model="checked" />


```

## Invalid [#](https://primevue.org/toggleswitch/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

```

<ToggleSwitch v-model="checked" :invalid="!checked" />


```

## Template [#](https://primevue.org/toggleswitch/#template)

The *handle* slot is available to display custom content.

```

<ToggleSwitch v-model="checked">
    <template #handle="{ checked }">
        <i :class="['!text-xs pi', { 'pi-check': checked, 'pi-times': !checked }]" />
    </template>
</ToggleSwitch>


```

## Disabled [#](https://primevue.org/toggleswitch/#disabled)

When *disabled* is present, the element cannot be edited and focused.

```

<ToggleSwitch v-model="checked" disabled />


```

## Accessibility [#](https://primevue.org/toggleswitch/#accessibility)

### Screen Reader

ToggleSwitch component uses a hidden native checkbox element with *switch* role internally that is only visible to screen readers. Value to describe the component can either be provided via *label* tag combined with *id* prop or using *aria-labelledby*, *aria-label* props.

```

<label for="switch1">Remember Me</label>
<ToggleSwitch inputId="switch1" />

<span id="switch2">Remember Me</span>
<ToggleSwitch aria-labelledby="switch2" />

<ToggleSwitch aria-label="Remember Me" />


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the switch. |
| *space* | Toggles the checked state. |