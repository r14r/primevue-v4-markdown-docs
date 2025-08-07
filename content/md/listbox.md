# Listbox

Listbox is used to select one or more values from a list of items.

## Import [#](https://primevue.org/listbox/#import)

```

import Listbox from 'primevue/listbox';


```

## Basic [#](https://primevue.org/listbox/#basic)

Listbox is used with the *v-model* property for two-way value binding along with the *options* collection. Label and value of an option are defined with the *optionLabel* and *optionValue* properties respectively. Note that, when options are simple primitive values such as a string array, no *optionLabel* and *optionValue* would be necessary.

* New York
* Rome
* London
* Istanbul
* Paris

No selected item

```

<Listbox v-model="selectedCity" :options="cities" optionLabel="name" class="w-full md:w-56" />


```

## Forms [#](https://primevue.org/listbox/#forms)

Listbox integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

* New York
* Rome
* London
* Istanbul
* Paris

1 items selected

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full sm:w-56">
    <div class="flex flex-col gap-1">
        <Listbox name="city" :options="cities" optionLabel="name" fluid />
        <Message v-if="$form.city?.invalid" severity="error" size="small" variant="simple">{{ $form.city.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Checkmark [#](https://primevue.org/listbox/#checkmark)

An alternative way to highlight the selected option is displaying a checkmark instead.

* New York
* Rome
* London
* Istanbul
* Paris

No selected item

```

<Listbox v-model="selectedCity" :options="cities" optionLabel="name" checkmark :highlightOnSelect="false" class="w-full md:w-56" />


```

## Multiple [#](https://primevue.org/listbox/#multiple)

Listbox allows choosing a single item by default, enable *multiple* property to choose more than one. When the optional *metaKeySelection* is present, behavior is changed in a way that selecting a new item requires meta key to be present.

* New York
* Rome
* London
* Istanbul
* Paris

No selected item

```

<Listbox v-model="selectedCity" :options="cities" multiple optionLabel="name" class="w-full md:w-56" />


```

## Group [#](https://primevue.org/listbox/#group)

Options can be grouped when a nested data structures is provided. To define the label of a group *optionGroupLabel* property is needed and also *optionGroupChildren* is required to define the property that refers to the children of a group.

* Germany
* Berlin
* Frankfurt
* Hamburg
* Munich
* USA
* Chicago
* Los Angeles
* New York
* San Francisco
* Japan
* Kyoto
* Osaka
* Tokyo
* Yokohama

No selected item

```

<Listbox v-model="selectedCity" :options="groupedCities" optionLabel="label" optionGroupLabel="label" optionGroupChildren="items" class="w-full md:w-56" listStyle="max-height:250px">
    <template #optiongroup="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.name" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ slotProps.option.label }}</div>
        </div>
    </template>
</Listbox>


```

## Filter [#](https://primevue.org/listbox/#filter)

Listbox provides built-in filtering that is enabled by adding the *filter* property.

5 results are available

* New York
* Rome
* London
* Istanbul
* Paris

No selected item

```

<Listbox v-model="selectedCity" :options="cities" filter optionLabel="name" class="w-full md:w-56" />


```

## Template [#](https://primevue.org/listbox/#template)

Custom content for an option is displayed with the *option* slot that takes an option as a parameter. Additional available templating sections are *filter* and *optionGroup*.

* Australia
* Brazil
* China
* Egypt
* France
* Germany
* India
* Japan
* Spain
* United States

No selected item

```

<Listbox v-model="selectedCountry" :options="countries" optionLabel="name" class="w-full md:w-56" listStyle="max-height:250px">
    <template #option="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.name" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ slotProps.option.name }}</div>
        </div>
    </template>
</Listbox>


```

## Virtual Scroll [#](https://primevue.org/listbox/#virtualscroll)

VirtualScroller is used to render a long list of options efficiently like 100K records in this demo. The configuration is done with *virtualScrollerOptions* property, refer to the [VirtualScroller](https://primevue.org/virtualscroller) for more information about the available options as it is used internally by Listbox.

No selected item

```

<Listbox v-model="selectedItem" :options="items" optionLabel="label" optionValue="value"
    :virtualScrollerOptions="{ itemSize: 38 }" class="w-full md:w-56" listStyle="height:250px" striped />


```

## Invalid [#](https://primevue.org/listbox/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

* New York
* Rome
* London
* Istanbul
* Paris

No selected item

```

<Listbox v-model="selectedCity" :options="cities" optionLabel="name" :invalid="selectedCity === null"  class="w-full md:w-56" />


```

## Disabled [#](https://primevue.org/listbox/#disabled)

When *disabled* is present, the element cannot be edited and focused.

* New York
* Rome
* London
* Istanbul
* Paris

No selected item

```

<Listbox v-model="selectedCity" disabled :options="cities" optionLabel="name" class="w-full md:w-56" />


```

## Accessibility [#](https://primevue.org/listbox/#accessibility)

### Screen Reader

Value to describe the component can be provided *aria-labelledby* or *aria-label* props. The list element has a *listbox* role with the *aria-multiselectable* attribute that sets to true when multiple selection is enabled. Each list item has an *option* role with *aria-selected* and *aria-disabled* as their attributes.

If filtering is enabled, *filterInputProps* can be defined to give *aria-\** props to the input element. Alternatively *filterPlaceholder* is usually utilized by the screen readers as well.

```

<span id="lb"></span>Options</span>
<Listbox aria-labelledby="lb" />

<Listbox aria-label="City" />


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the first selected option, if there is none then first option receives the focus. |
| *up arrow* | Moves focus to the previous option. |
| *down arrow* | Moves focus to the next option. |
| *enter* | Toggles the selected state of the focused option. |
| *space* | Toggles the selected state of the focused option. |
| *home* | Moves focus to the first option. |
| *end* | Moves focus to the last option. |
| *shift* + *down arrow* | Moves focus to the next option and toggles the selection state. |
| *shift* + *up arrow* | Moves focus to the previous option and toggles the selection state. |
| *shift* + *space* | Selects the items between the most recently selected option and the focused option. |
| *control* + *shift* + *home* | Selects the focused options and all the options up to the first one. |
| *control* + *shift* + *end* | Selects the focused options and all the options down to the last one. |
| *control* + *a* | Selects all options. |
| *pageUp* | Jumps visual focus to first option. |
| *pageDown* | Jumps visual focus to last option. |
| *any printable character* | Moves focus to the option whose label starts with the characters being typed. |

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
| *tab* | Moves focus to the next focusable element in the component. If there is none, moves focus to next element in page. |