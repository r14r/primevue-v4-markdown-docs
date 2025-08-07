# Select

Select is used to choose an item from a collection of options.

## Import [#](https://primevue.org/select/#import)

```

import Select from 'primevue/select';


```

## Basic [#](https://primevue.org/select/#basic)

Select is used with the *v-model* property for two-way value binding along with the *options* collection. Label and value of an option are defined with the *optionLabel* and *optionValue* properties respectively. Note that, when options are simple primitive values such as a string array, no *optionLabel* and *optionValue* would be necessary.

Select a City

```

<Select v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Select a City" class="w-full md:w-56" />


```

## Forms [#](https://primevue.org/select/#forms)

Select a City

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full md:w-56">
    <div class="flex flex-col gap-1">
        <Select name="city.name" :options="cities" optionLabel="name" placeholder="Select a City" fluid />
        <Message v-if="$form.city?.name?.invalid" severity="error" size="small" variant="simple">{{ $form.city.name.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Checkmark [#](https://primevue.org/select/#checkmark)

An alternative way to highlight the selected option is displaying a checkmark instead.

Select a City

```

<Select v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Select a City" checkmark :highlightOnSelect="false" class="w-full md:w-56" />


```

## Editable [#](https://primevue.org/select/#editable)

When *editable* is present, the input can also be entered with typing.

```

<Select v-model="selectedCity" editable :options="cities" optionLabel="name" placeholder="Select a City" class="w-full md:w-56" />


```

## Group [#](https://primevue.org/select/#group)

Options can be grouped when a nested data structures is provided. To define the label of a group *optionGroupLabel* property is needed and also *optionGroupChildren* is required to define the property that refers to the children of a group.

Select a City

```

<Select v-model="selectedCity" :options="groupedCities" optionLabel="label" optionGroupLabel="label" optionGroupChildren="items" placeholder="Select a City" class="w-full md:w-56">
    <template #optiongroup="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`mr-2 flag flag-${slotProps.option.code.toLowerCase()}`" style="width: 18px" />
            <div>{{ slotProps.option.label }}</div>
        </div>
    </template>
</Select>


```

## Template [#](https://primevue.org/select/#template)

Select offers multiple slots for customization through templating.

Select a Country

```

<Select v-model="selectedCountry" :options="countries" optionLabel="name" placeholder="Select a Country" class="w-full md:w-56">
    <template #value="slotProps">
        <div v-if="slotProps.value" class="flex items-center">
            <img :alt="slotProps.value.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`mr-2 flag flag-${slotProps.value.code.toLowerCase()}`" style="width: 18px" />
            <div>{{ slotProps.value.name }}</div>
        </div>
        <span v-else>
            {{ slotProps.placeholder }}
        </span>
    </template>
    <template #option="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`mr-2 flag flag-${slotProps.option.code.toLowerCase()}`" style="width: 18px" />
            <div>{{ slotProps.option.name }}</div>
        </div>
    </template>
    <template #dropdownicon>
        <i class="pi pi-map" />
    </template>
    <template #header>
        <div class="font-medium p-3">Available Countries</div>
    </template>
    <template #footer>
        <div class="p-3">
            <Button label="Add New" fluid severity="secondary" variant="text" size="small" icon="pi pi-plus" />
        </div>
    </template>
</Select>


```

## Filter [#](https://primevue.org/select/#filter)

Select provides built-in filtering that is enabled by adding the *filter* property.

Select a Country

```

<Select v-model="selectedCountry" :options="countries" filter optionLabel="name" placeholder="Select a Country" class="w-full md:w-56">
    <template #value="slotProps">
        <div v-if="slotProps.value" class="flex items-center">
            <img :alt="slotProps.value.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`mr-2 flag flag-${slotProps.value.code.toLowerCase()}`" style="width: 18px" />
            <div>{{ slotProps.value.name }}</div>
        </div>
        <span v-else>
            {{ slotProps.placeholder }}
        </span>
    </template>
    <template #option="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`mr-2 flag flag-${slotProps.option.code.toLowerCase()}`" style="width: 18px" />
            <div>{{ slotProps.option.name }}</div>
        </div>
    </template>
</Select>


```

## Clear Icon [#](https://primevue.org/select/#clearicon)

When *showClear* is enabled, a clear icon is added to reset the Select.

Select a City

```

<Select v-model="selectedCity" :options="cities" showClear optionLabel="name" placeholder="Select a City" class="w-full md:w-56" />


```

## Loading State [#](https://primevue.org/select/#loadingstate)

Loading state is enabled with the *loading* property.

Loading...

```

<Select placeholder="Loading..." loading class="w-full md:w-56" />


```

## Virtual Scroll [#](https://primevue.org/select/#virtualscroll)

VirtualScroller is used to render a long list of options efficiently like 100K records in this demo. The configuration is done with *virtualScrollerOptions* property, refer to the [VirtualScroller](https://primevue.org/virtualscroller) for more information about the available options as it is used internally by Select.

Select Item

```

<Select v-model="selectedItem" :options="items" optionLabel="label" optionValue="value"
    :virtualScrollerOptions="{ itemSize: 38 }" placeholder="Select Item" class="w-full md:w-56" />


```

## Lazy Virtual Scroll [#](https://primevue.org/select/#lazyvirtualscroll)

The virtual scrolling also supports dynamically loading items on demand.

Select Item

```

<Select v-model="selectedItem" :options="items" optionLabel="label" optionValue="value" class="w-full md:w-56"
    :virtualScrollerOptions="{ lazy: true, onLazyLoad: onLazyLoad, itemSize: 38, showLoader: true, loading: loading, delay: 250 }" placeholder="Select Item" />


```

## Filled [#](https://primevue.org/select/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

Select a City

```

<Select v-model="selectedCity" variant="filled" :options="cities" optionLabel="name" placeholder="Select a City" class="w-full md:w-56" />


```

## Float Label [#](https://primevue.org/select/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

Over LabelIn LabelOn Label

```

<FloatLabel class="w-full md:w-56">
    <Select v-model="value1" inputId="over_label" :options="cities" optionLabel="name" class="w-full" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-56" variant="in">
    <Select v-model="value2" inputId="in_label" :options="cities" optionLabel="name" class="w-full" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-56" variant="on">
    <Select v-model="value3" inputId="on_label" :options="cities" optionLabel="name" class="w-full" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/select/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

City

```

<IftaLabel>
    <Select v-model="selectedCity" inputId="dd-city" :options="cities" optionLabel="name" class="w-full" variant="filled" />
    <label for="dd-city">City</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/select/#sizes)

Select provides *small* and *large* sizes as alternatives to the base.

Small

Normal

Large

```

<Select v-model="value1" :options="cities" optionLabel="name" size="small" placeholder="Small" class="w-full md:w-56" />
<Select v-model="value2" :options="cities" optionLabel="name" placeholder="Normal" class="w-full md:w-56" />
<Select v-model="value3" :options="cities" optionLabel="name" size="large" placeholder="Large" class="w-full md:w-56" />


```

## Invalid [#](https://primevue.org/select/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

Select a City

Select a City

```

<Select v-model="selectedCity1" :options="cities" optionLabel="name" placeholder="Select a City" :invalid="!selectedCity1" class="w-full md:w-56" />
<Select v-model="selectedCity2" :options="cities" optionLabel="name" placeholder="Select a City" :invalid="!selectedCity2" class="w-full md:w-56" variant="filled" />


```

## Disabled [#](https://primevue.org/select/#disabled)

When *disabled* is present, the element cannot be edited and focused.

Select a City

```

<Select disabled placeholder="Select a City" class="w-full md:w-56" />


```

## Accessibility [#](https://primevue.org/select/#accessibility)

### Screen Reader

Value to describe the component can either be provided with *aria-labelledby* or *aria-label* props. The select element has a *combobox* role in addition to *aria-haspopup* and *aria-expanded* attributes. If the editable option is enabled *aria-autocomplete* is also added. The relation between the combobox and the popup is created with *aria-controls* and *aria-activedescendant* attribute is used to instruct screen reader which option to read during keyboard navigation within the popup list.

The popup list has an id that refers to the *aria-controls* attribute of the *combobox* element and uses *listbox* as the role. Each list item has an *option* role, an id to match the *aria-activedescendant* of the input element along with *aria-label*, *aria-selected* and *aria-disabled* attributes.

If filtering is enabled, *filterInputProps* can be defined to give *aria-\** props to the filter input element.

```

<span id="dd1"></span>Options</span>
<select aria-labelledby="dd1" />

<select aria-label="Options" />


```

### Closed State Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the select element. |
| *space* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *enter* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *down arrow* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *up arrow* | Opens the popup and moves visual focus to the selected option, if there is none then last option receives the focus. |
| *any printable character* | Opens the popup and moves focus to the option whose label starts with the characters being typed, if there is none and select is not editable then first option receives the focus. |

### Popup Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next focusable element in the popup. If there is none, the focusable option is selected and the overlay is closed then moves focus to next element in page. |
| *shift* + *tab* | Moves focus to the previous focusable element in the popup. If there is none, the focusable option is selected and the overlay is closed then moves focus to next element in page. |
| *enter* | Selects the focused option and closes the popup, then moves focus to the select element. |
| *space* | Selects the focused option and closes the popup, then moves focus to the select element. |
| *escape* | Closes the popup, then moves focus to the select element. |
| *down arrow* | Moves focus to the next option, if there is none then visual focus does not change. |
| *up arrow* | Moves focus to the previous option, if there is none then visual focus does not change. |
| *alt* + *up arrow* | Selects the focused option and closes the popup, then moves focus to the select element. |
| *left arrow* | If the select is editable, removes the visual focus from the current option and moves input cursor to one character left. |
| *right arrow* | If the select is editable, removes the visual focus from the current option and moves input cursor to one character right. |
| *home* | If the select is editable, moves input cursor at the end, if not then moves focus to the first option. |
| *end* | If the select is editable, moves input cursor at the beginning, if not then moves focus to the last option. |
| *pageUp* | Jumps visual focus to first option. |
| *pageDown* | Jumps visual focus to last option. |
| *any printable character* | Moves focus to the option whose label starts with the characters being typed if select is not editable. |

### Filter Input Keyboard Support

| Key | Function |
| --- | --- |
| *down arrow* | Moves focus to the next option, if there is none then visual focus does not change. |
| *up arrow* | Moves focus to the previous option, if there is none then visual focus does not change. |
| *left arrow* | Removes the visual focus from the current option and moves input cursor to one character left. |
| *right arrow* | Removes the visual focus from the current option and moves input cursor to one character right. |
| *home* | Moves input cursor at the end, if not then moves focus to the first option. |
| *end* | Moves input cursor at the beginning, if not then moves focus to the last option. |
| *enter* | Closes the popup and moves focus to the select element. |
| *escape* | Closes the popup and moves focus to the select element. |
| *tab* | Moves focus to the next focusable element in the popup. If there is none, the focusable option is selected and the overlay is closed then moves focus to next element in page. |