# AutoComplete

AutoComplete is an input component that provides real-time suggestions when being typed.

## Import [#](https://primevue.org/autocomplete/#import)

```

import AutoComplete from 'primevue/autocomplete';


```

## Basic [#](https://primevue.org/autocomplete/#basic)

AutoComplete is used with the *v-model* property for two-way value binding. In addition, *suggestions* property and a *complete* method are required to query the results.

No results found

```

<AutoComplete v-model="value" :suggestions="items" @complete="search" />


```

## Objects [#](https://primevue.org/autocomplete/#objects)

AutoComplete can work with objects using the *optionLabel* property that defines the label to display as a suggestion. The value passed to the model would still be the object instance of a suggestion. Here is an example with a Country object that has name and code fields such as *{name: "United States", code:"USA"}*.

No results found

```

<AutoComplete v-model="selectedCountry" optionLabel="name" :suggestions="filteredCountries" @complete="search" />


```

## Forms [#](https://primevue.org/autocomplete/#forms)

AutoComplete integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

No results found

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex justify-center flex-col gap-4 w-full md:w-56">
    <div class="flex flex-col gap-1">
        <AutoComplete name="country.name" optionLabel="name" :suggestions="filteredCountries" @complete="search" fluid />
        <Message v-if="$form.country?.name?.invalid" severity="error" size="small" variant="simple">{{ $form.country.name.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Dropdown [#](https://primevue.org/autocomplete/#dropdown)

Enabling *dropdown* property displays a button next to the input field where click behavior of the button is defined using *dropdownMode* property that takes **blank** or **current** as possible values. *blank* is the default mode to send a query with an empty string whereas *current* setting sends a query with the current value of the input.

No results found

```

<AutoComplete v-model="value" dropdown :suggestions="items" @complete="search" />


```

## Template [#](https://primevue.org/autocomplete/#template)

AutoComplete offers multiple slots for customization through templating.

No results found

```

<AutoComplete v-model="selectedCountry" optionLabel="name" :suggestions="filteredCountries" @complete="search">
    <template #option="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.name" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ slotProps.option.name }}</div>
        </div>
    </template>
    <template #header>
        <div class="font-medium px-3 py-2">Available Countries</div>
    </template>
    <template #footer>
        <div class="px-3 py-3">
            <Button label="Add New" fluid severity="secondary" text size="small" icon="pi pi-plus" />
        </div>
    </template>
</AutoComplete>


```

## Group [#](https://primevue.org/autocomplete/#group)

Option groups are specified with the *optionGroupLabel* and *optionGroupChildren* properties.

No results found

```

<AutoComplete v-model="selectedCity" :suggestions="filteredCities" @complete="search" optionLabel="label" optionGroupLabel="label" optionGroupChildren="items" placeholder="Hint: type 'a'">
    <template #optiongroup="slotProps">
        <div class="flex items-center country-item">
            <img :alt="slotProps.option.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ slotProps.option.label }}</div>
        </div>
    </template>
</AutoComplete>


```

## Force Selection [#](https://primevue.org/autocomplete/#forceselection)

ForceSelection mode validates the manual input to check whether it also exists in the suggestions list, if not the input value is cleared to make sure the value passed to the model is always one of the suggestions. Simply enable *forceSelection* to enforce that input is always from the suggestion list.

No results found

```

<AutoComplete v-model="selectedCountry" forceSelection optionLabel="name" :suggestions="filteredCountries" @complete="search" />


```

## Virtual Scroll [#](https://primevue.org/autocomplete/#virtualscroll)

Virtual Scrolling is a performant way to render large lists. Configuration of the scroll behavior is defined with *virtualScrollerOptions* that requires *itemSize* as the mandatory value to set the height of an item. Visit [VirtualScroller](https://primevue.org/virtualscroller/) documentation for more information about the configuration API.

No results found

```

<AutoComplete v-model="selectedItem" :suggestions="filteredItems" @complete="searchItems"
    :virtualScrollerOptions="{ itemSize: 38 }" optionLabel="label" dropdown />


```

## Filled [#](https://primevue.org/autocomplete/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

No results found

```

<AutoComplete v-model="value" :suggestions="items" @complete="search" variant="filled" />


```

## Float Label [#](https://primevue.org/autocomplete/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

No results found

Over Label

No results found

In Label

No results found

On Label

```

<FloatLabel>
    <AutoComplete v-model="value1" inputId="over_label" :suggestions="items" @complete="search" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <AutoComplete v-model="value2" inputId="in_label" :suggestions="items" @complete="search" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <AutoComplete v-model="value3" inputId="on_label" :suggestions="items" @complete="search" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/autocomplete/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

No results found

Identifier

```

<IftaLabel>
    <AutoComplete v-model="value" inputId="ac" :suggestions="items" @complete="search" variant="filled" />
    <label for="ac">Identifier</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/autocomplete/#sizes)

AutoComplete provides *small* and *large* sizes as alternatives to the base.

No results found

No results found

No results found

```

<AutoComplete v-model="value1" :suggestions="items" @complete="search" size="small" placeholder="Small" dropdown />
<AutoComplete v-model="value2" :suggestions="items" @complete="search" placeholder="Normal" dropdown />
<AutoComplete v-model="value3" :suggestions="items" @complete="search" size="large" placeholder="Large" dropdown />


```

## Multiple [#](https://primevue.org/autocomplete/#multiple)

Multiple mode is enabled using *multiple* property used to select more than one value from the autocomplete. In this case, value reference should be an array.

With Typeahead

No results found

Without Typeahead

```

<label for="multiple-ac-1" class="font-bold mb-2 block">With Typeahead</label>
<AutoComplete v-model="value1" inputId="multiple-ac-1" multiple fluid :suggestions="items" @complete="search" />

<label for="multiple-ac-2" class="font-bold mt-8 mb-2 block">Without Typeahead</label>
<AutoComplete v-model="value2" inputId="multiple-ac-2" multiple fluid @complete="search" :typeahead="false" />


```

## Invalid [#](https://primevue.org/autocomplete/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

No results found

No results found

```

<AutoComplete v-model="value1" :suggestions="items" @complete="search" :invalid="!value1" placeholder="Code" />
<AutoComplete v-model="value2" :suggestions="items" @complete="search" :invalid="!value2" variant="filled" placeholder="Code" />


```

## Disabled [#](https://primevue.org/autocomplete/#disabled)

When *disabled* is present, the element cannot be edited and focused.

No results found

```

<AutoComplete disabled placeholder="Disabled" />


```

## Accessibility [#](https://primevue.org/autocomplete/#accessibility)

### Screen Reader

Value to describe the component can either be provided via *label* tag combined with *inputId* prop or using *aria-labelledby*, *aria-label* props. The input element has *combobox* role in addition to *aria-autocomplete*, *aria-haspopup* and *aria-expanded* attributes. The relation between the input and the popup is created with *aria-controls* and *aria-activedescendant* attribute is used to instruct screen reader which option to read during keyboard navigation within the popup list.

In multiple mode, chip list uses *listbox* role with *aria-orientation* set to horizontal whereas each chip has the *option* role with *aria-label* set to the label of the chip.

The popup list has an id that refers to the *aria-controls* attribute of the input element and uses *listbox* as the role. Each list item has *option* role and an id to match the *aria-activedescendant* of the input element.

```

<label for="ac1">;Username</label>
<AutoComplete inputId="ac1" />

<span id="ac2">Email</span>
<AutoComplete aria-labelledby="ac2" />

<AutoComplete aria-label="City" />


```

### Closed State Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the autocomplete element. |
| *any printable character* | Opens the popup and moves focus to the first option. |

### Popup Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next focusable element in the popup. If there is none, the focusable option is selected and the overlay is closed then moves focus to next element in page. |
| *shift* + *tab* | Moves focus to the previous focusable element in the popup. If there is none, the focusable option is selected and the overlay is closed then moves focus to next element in page. |
| *enter* | Selects the focused option and closes the popup, then moves focus to the autocomplete element. |
| *space* | Selects the focused option and closes the popup, then moves focus to the autocomplete element. |
| *escape* | Closes the popup, then moves focus to the autocomplete element. |
| *down arrow* | Moves focus to the next option, if there is none then visual focus does not change. |
| *up arrow* | Moves focus to the previous option, if there is none then visual focus does not change. |
| *alt* + *up arrow* | Selects the focused option and closes the popup, then moves focus to the autocomplete element. |
| *left arrow* | Removes the visual focus from the current option and moves input cursor to one character left. |
| *right arrow* | Removes the visual focus from the current option and moves input cursor to one character right. |
| *home* | Moves input cursor at the end, if not then moves focus to the first option. |
| *end* | Moves input cursor at the beginning, if not then moves focus to the last option. |
| *pageUp* | Jumps visual focus to first option. |
| *pageDown* | Jumps visual focus to last option. |
| *shift* + *down arrow* | Moves focus to the next option and toggles the selection state. |
| *shift* + *up arrow* | Moves focus to the previous option and toggles the selection state. |
| *shift* + *space* | Selects the items between the most recently selected option and the focused option. |
| *control* + *shift* + *home* | Selects the focused options and all the options up to the first one. |
| *control* + *shift* + *end* | Selects the focused options and all the options down to the last one. |

### Chips Input Keyboard Support

| Key | Function |
| --- | --- |
| *backspace* | Deletes the previous chip if the input field is empty. |
| *left arrow* | Moves focus to the previous chip if available and input field is empty. |

### Chip Keyboard Support

| Key | Function |
| --- | --- |
| *left arrow* | Moves focus to the previous chip if available. |
| *right arrow* | Moves focus to the next chip, if there is none then input field receives the focus. |
| *backspace* | Deletes the chips and adds focus to the input field. |