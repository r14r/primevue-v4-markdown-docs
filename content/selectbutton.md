# SelectButton

SelectButton is used to choose single or multiple items from a list using buttons.

## Import [#](https://primevue.org/selectbutton/#import)

```

import SelectButton from 'primevue/selectbutton';


```

## Basic [#](https://primevue.org/selectbutton/#basic)

SelectButton is used with the *v-model* property for two-way value binding along with the *options* collection. Label and value of an option are defined with the *optionLabel* and *optionValue* properties respectively. Note that, when options are simple primitive values such as a string array, no *optionLabel* and *optionValue* would be necessary.

One-WayReturn

```

<SelectButton v-model="value" :options="options" />


```

## Forms [#](https://primevue.org/selectbutton/#forms)

SelectButton integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

One-WayReturn

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <SelectButton name="selection" :options="options" />
        <Message v-if="$form.selection?.invalid" severity="error">{{ $form.selection.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Multiple [#](https://primevue.org/selectbutton/#multiple)

SelectButton allows selecting only one item by default and setting *multiple* option enables choosing more than one item. In multiple case, model property should be an array.

Option 1Option 2Option 3

```

<SelectButton v-model="value" :options="options" optionLabel="name" multiple aria-labelledby="multiple" />


```

## Template [#](https://primevue.org/selectbutton/#template)

Label of an option is used as the display text of an item by default, for custom content support define an *option* template that gets the option instance as a parameter.

```

<SelectButton v-model="value" :options="options" optionLabel="value" dataKey="value" aria-labelledby="custom">
    <template #option="slotProps">
        <i :class="slotProps.option.icon"></i>
    </template>
</SelectButton>


```

## Sizes [#](https://primevue.org/selectbutton/#sizes)

SelectButton provides *small* and *large* sizes as alternatives to the base.

BeginnerExpert

BeginnerExpert

BeginnerExpert

```

<SelectButton v-model="value1" :options="options" size="small" />
<SelectButton v-model="value2" :options="options" />
<SelectButton v-model="value3" :options="options" size="large" />


```

## Invalid [#](https://primevue.org/selectbutton/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

One-WayReturn

```

<SelectButton v-model="value" :options="options" aria-labelledby="basic" allowEmpty :invalid="value === null"  />


```

## Disabled [#](https://primevue.org/selectbutton/#disabled)

When *disabled* is present, the element cannot be edited and focused entirely. Certain options can also be disabled using the *optionDisabled* property.

OffOn

Option 1Option 2

```

<SelectButton v-model="value" :options="options" disabled />
<SelectButton v-model="value" :options="options2" optionDisabled="constant" optionLabel="name" />


```

## Accessibility [#](https://primevue.org/selectbutton/#accessibility)

### Screen Reader

SelectButton component uses ToggleButton internally and has *group* role. Value to describe the component can be provided via *aria-labelledby* property.

### Keyboard Support

Keyboard interaction is derived from the native browser handling of checkboxs in a group.

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next the focusable element in the page tab sequence. |
| *shift* + *tab* | Moves focus to the previous the focusable element in the page tab sequence. |
| *space* | Toggles the checked state of a button. |