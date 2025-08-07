# MultiSelect

MultiSelect is used to select multiple items from a collection.

## Import [#](https://primevue.org/multiselect/#import)

```

import MultiSelect from 'primevue/multiselect';


```

## Basic [#](https://primevue.org/multiselect/#basic)

MultiSelect is used with the *v-model* property for two-way value binding along with the *options* collection. Label and value of an option are defined with the *optionLabel* and *optionValue* properties respectively. Note that, when options are simple primitive values such as a string array, no *optionLabel* and *optionValue* would be necessary.

Select Cities

```

<MultiSelect v-model="selectedCities" :options="cities" optionLabel="name" filter placeholder="Select Cities"
    :maxSelectedLabels="3" class="w-full md:w-80" />


```

## Forms [#](https://primevue.org/multiselect/#forms)

Select Cities

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex justify-center flex-col gap-4">
    <div class="flex flex-col gap-1">
        <MultiSelect name="city" :options="cities" optionLabel="name" filter placeholder="Select Cities" :maxSelectedLabels="3" class="w-full md:w-80" />
        <Message v-if="$form.city?.invalid" severity="error" size="small" variant="simple">{{ $form.city.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Chips [#](https://primevue.org/multiselect/#chips)

Selected values are displayed as a comma separated list by default, setting *display* as *chip* displays them as chips.

Select Cities

```

<MultiSelect v-model="selectedCities" display="chip" :options="cities" optionLabel="name" filter placeholder="Select Cities"
    :maxSelectedLabels="3" class="w-full md:w-80" />


```

## Group [#](https://primevue.org/multiselect/#group)

Options can be grouped when a nested data structures is provided. To define the label of a group *optionGroupLabel* property is needed and also *optionGroupChildren* is required to define the property that refers to the children of a group.

Select Cities

```

<MultiSelect v-model="selectedCities" :options="groupedCities" optionLabel="label" filter optionGroupLabel="label" optionGroupChildren="items" display="chip" placeholder="Select Cities" class="w-full md:w-80">
    <template #optiongroup="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ slotProps.option.label }}</div>
        </div>
    </template>
</MultiSelect>


```

## Template [#](https://primevue.org/multiselect/#template)

MultiSelect offers multiple slots for customization through templating.

Select Countries

```

<MultiSelect v-model="selectedCountries" :options="countries" optionLabel="name" filter placeholder="Select Countries" display="chip" class="w-full md:w-80">
    <template #option="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.name" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ slotProps.option.name }}</div>
        </div>
    </template>
    <template #dropdownicon>
        <i class="pi pi-map" />
    </template>
    <template #filtericon>
        <i class="pi pi-map-marker" />
    </template>
    <template #header>
        <div class="font-medium px-3 py-2">Available Countries</div>
    </template>
    <template #footer>
        <div class="p-3 flex justify-between">
            <Button label="Add New" severity="secondary" variant="text" size="small" icon="pi pi-plus" />
            <Button label="Remove All" severity="danger" variant="text" size="small" icon="pi pi-times" />
        </div>
    </template>
</MultiSelect>


```

## Filter [#](https://primevue.org/multiselect/#filter)

Filtering allows searching items in the list using an input field at the header. In order to use filtering, enable *filter* property. By default, optionLabel is used when searching and *filterFields* can be used to customize the fields being utilized. Furthermore, *filterMatchMode* is available to define the search algorithm. Valid values are "contains" (default), "startsWith" and "endsWith".

Select Cities

```

<MultiSelect v-model="selectedCities" :options="cities" filter optionLabel="name" placeholder="Select Cities"
    :maxSelectedLabels="3" class="w-full md:w-80" />


```

## Clear Icon [#](https://primevue.org/multiselect/#clearicon)

When *showClear* is enabled, a clear icon is added to reset the MultiSelect.

Select Cities

```

<MultiSelect v-model="selectedCities" showClear :options="cities" optionLabel="name" filter placeholder="Select Cities" :maxSelectedLabels="3" class="w-full md:w-80" />


```

## Loading State [#](https://primevue.org/multiselect/#loadingstate)

Loading state can be used *loading* property.

Loading...

```

<MultiSelect placeholder="Loading..." loading class="w-full md:w-80"></MultiSelect>


```

## VirtualScroll [#](https://primevue.org/multiselect/#virtualscroll)

VirtualScroller is used to render a long list of options efficiently like 100K records in this demo. The configuration is done with *virtualScrollerOptions* property, refer to the [VirtualScroller](https://primevue.org/virtualscroller) for more information about the available options as it is used internally by MultiSelect.

Select Item

```

<MultiSelect v-model="selectedItems" :options="items" :maxSelectedLabels="3" :selectAll="selectAll" optionLabel="label" optionValue="value"
    @selectall-change="onSelectAllChange($event)" @change="onChange($event)" :virtualScrollerOptions="{ itemSize: 44 }" filter placeholder="Select Item" class="w-full md:w-80" />


```

## Filled [#](https://primevue.org/multiselect/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

Select Cities

```

<MultiSelect v-model="selectedCities" variant="filled" :options="cities" optionLabel="name" filter placeholder="Select Cities"
    :maxSelectedLabels="3" class="w-full md:w-80" />


```

## Float Label [#](https://primevue.org/multiselect/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

empty

Over Label

empty

In Label

empty

On Label

```

<FloatLabel class="w-full md:w-80">
    <MultiSelect id="over_label" v-model="value1" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="in">
    <MultiSelect id="in_label" v-model="value2" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="on">
    <MultiSelect id="on_label" v-model="value3" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/multiselect/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

empty

Cities

```

<IftaLabel>
    <MultiSelect v-model="selectedCities" inputId="ms_cities" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" variant="filled" />
    <label for="ms_cities">Cities</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/multiselect/#sizes)

MultiSelect provides *small* and *large* sizes as alternatives to the base.

Small

Normal

Large

```

<MultiSelect v-model="value1" :options="cities" optionLabel="name" :maxSelectedLabels="3" class="w-full md:w-80" size="small" placeholder="Small" />
<MultiSelect v-model="value2" :options="cities" optionLabel="name" :maxSelectedLabels="3" class="w-full md:w-80" placeholder="Normal" />
<MultiSelect v-model="value3" :options="cities" optionLabel="name" :maxSelectedLabels="3" class="w-full md:w-80" size="large" placeholder="Large" />


```

## Invalid [#](https://primevue.org/multiselect/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

Select Cities

Select Cities

```

<MultiSelect v-model="selectedCities1" :options="cities" optionLabel="name" filter placeholder="Select Cities" 
        :maxSelectedLabels="3" :invalid="selectedCities1?.length === 0" class="w-full md:w-80" />
<MultiSelect v-model="selectedCities2" :options="cities" optionLabel="name" filter placeholder="Select Cities" 
        :maxSelectedLabels="3" :invalid="selectedCities2?.length === 0" class="w-full md:w-80" variant="filled" />


```

## Disabled [#](https://primevue.org/multiselect/#disabled)

When *disabled* is present, the element cannot be edited and focused.

Select Cities

```

<MultiSelect disabled placeholder="Select Cities" class="w-full md:w-80" />


```

## Accessibility [#](https://primevue.org/multiselect/#accessibility)

### Screen Reader

Value to describe the component can either be provided with *aria-labelledby* or *aria-label* props. The multiselect component has a *combobox* role in addition to *aria-haspopup* and *aria-expanded* attributes. The relation between the combobox and the popup is created with *aria-controls* attribute that refers to the id of the popup listbox.

The popup listbox uses *listbox* as the role with *aria-multiselectable* enabled. Each list item has an *option* role along with *aria-label*, *aria-selected* and *aria-disabled* attributes.

Checkbox component at the header uses a hidden native checkbox element internally that is only visible to screen readers. Value to read is defined with the *selectAll* and *unselectAll* keys of the *aria* property from the [locale](https://primevue.org/configuration/#locale) API.

If filtering is enabled, *filterInputProps* can be defined to give *aria-\** props to the input element.

Close button uses *close* key of the *aria* property from the [locale](https://primevue.org/configuration/#locale) API as the *aria-label* by default, this can be overridden with the *closeButtonProps*.

```

<span id="dd1"></span>Options</span>
<MultiSelect aria-labelledby="dd1" />

<MultiSelect aria-label="Options" />


```

### Closed State Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the multiselect element. |
| *space* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *enter* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *down arrow* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *up arrow* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *any printable character* | Opens the popup and moves focus to the option whose label starts with the characters being typed, if there is none then first option receives the focus. |

### Popup Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next focusable element in the popup, if there is none then first focusable element receives the focus. |
| *shift* + *tab* | Moves focus to the previous focusable element in the popup, if there is none then last focusable element receives the focus. |
| *enter* | Toggles the selection state of the focused option, then moves focus to the multiselect element. |
| *space* | Toggles the selection state of the focused option, then moves focus to the multiselect element. |
| *escape* | Closes the popup, moves focus to the multiselect element. |
| *down arrow* | Moves focus to the next option, if there is none then visual focus does not change. |
| *up arrow* | Moves focus to the previous option, if there is none then visual focus does not change. |
| *alt* + *up arrow* | Selects the focused option and closes the popup, then moves focus to the multiselect element. |
| *shift* + *down arrow* | Moves focus to the next option and toggles the selection state. |
| *shift* + *up arrow* | Moves focus to the previous option and toggles the selection state. |
| *shift* + *space* | Selects the items between the most recently selected option and the focused option. |
| *home* | Moves focus to the first option. |
| *end* | Moves focus to the last option. |
| *control* + *shift* + *home* | Selects the focused options and all the options up to the first one. |
| *control* + *shift* + *end* | Selects the focused options and all the options down to the last one. |
| *control* + *a* | Selects all options. |
| *pageUp* | Jumps visual focus to first option. |
| *pageDown* | Jumps visual focus to last option. |
| *any printable character* | Moves focus to the option whose label starts with the characters being typed. |

### Toggle All Checkbox Keyboard Support

| Key | Function |
| --- | --- |
| *space* | Toggles the checked state. |
| *escape* | Closes the popup and moves focus to the multiselect element. |

### Filter Input Keyboard Support

| Key | Function |
| --- | --- |
| *down arrow* | Moves focus to the next option, if there is none then visual focus does not change. |
| *up arrow* | Moves focus to the previous option, if there is none then visual focus does not change. |
| *left arrow* | Removes the visual focus from the current option and moves input cursor to one character left. |
| *right arrow* | Removes the visual focus from the current option and moves input cursor to one character right. |
| *home* | Moves input cursor at the end, if not then moves focus to the first option. |
| *end* | Moves input cursor at the beginning, if not then moves focus to the last option. |
| *enter* | Closes the popup and moves focus to the multiselect element. |
| *escape* | Closes the popup and moves focus to the multiselect element. |
| *tab* | Moves focus to the next focusable element in the popup. If there is none, the focusable option is selected and the overlay is closed then moves focus to next element in page. |