# ColorPicker

ColorPicker is an input component to select a color.

## Import [#](https://primevue.org/colorpicker/#import)

```

import ColorPicker from 'primevue/colorpicker';


```

## Basic [#](https://primevue.org/colorpicker/#basic)

ColorPicker is used with the *v-model* property for two-way value binding.

```

<ColorPicker v-model="color" />


```

## Forms [#](https://primevue.org/colorpicker/#forms)

ColorPicker integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col items-center gap-2">
        <ColorPicker name="color" />
        <Message v-if="$form.color?.invalid" severity="error" size="small" variant="simple">{{ $form.color.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Inline [#](https://primevue.org/colorpicker/#inline)

ColorPicker is displayed as a popup by default, add *inline* property to customize this behavior.

```

<ColorPicker v-model="color" inline />


```

## Format [#](https://primevue.org/colorpicker/#format)

Default color format to use in value binding is *hex* and other possible values can be *rgb* and *hsb* using the *format* property.

HEX 6466f1

RGB {"r":100,"g":102,"b":241}

HSB {"h":239,"s":59,"b":95}

```

<ColorPicker v-model="colorHEX" inputId="cp-hex" format="hex" class="mb-4" />
<ColorPicker v-model="colorRGB" inputId="cp-rgb" format="rgb" class="mb-4" />
<ColorPicker v-model="colorHSB" inputId="cp-hsb" format="hsb" class="mb-4" />


```

## Disabled [#](https://primevue.org/colorpicker/#disabled)

When *disabled* is present, the element cannot be edited and focused.

```

<ColorPicker v-model="color" disabled />


```

## Accessibility [#](https://primevue.org/colorpicker/#accessibility)

### Screen Reader

Specification does not cover a color picker [yet](https://github.com/w3c/aria/issues/930) and using a semantic native color picker is not consistent across browsers so currently component is not compatible with screen readers. In the upcoming versions, text fields will be introduced below the slider section to be able to pick a color using accessible text boxes in hsl, rgba and hex formats.

### Closed State Keyboard Support of Popup ColorPicker

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the color picker button. |
| *space* | Opens the popup and moves focus to the color slider. |

### Popup Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Selects the color and closes the popup. |
| *space* | Selects the color and closes the popup. |
| *escape* | Closes the popup, moves focus to the input. |

### Color Picker Slider

| Key | Function |
| --- | --- |
| *arrow keys* | Changes color. |

### Hue Slider

| Key | Function |
| --- | --- |
| *up arrow**down arrow* | Changes hue. |