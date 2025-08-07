# CascadeSelect

CascadeSelect is a form component to select a value from a nested structure of options.

## Import [#](https://primevue.org/cascadeselect/#import)

```

import CascadeSelect from 'primevue/cascadeselect';


```

## Basic [#](https://primevue.org/cascadeselect/#basic)

CascadeSelect is used with the *v-model* property for two-way value binding along with the *options* collection. To define the label of a group *optionGroupLabel* property is needed and also *optionGroupChildren* is required to define the property that refers to the children of a group. Note that order of the *optionGroupChildren* matters as it should correspond to the data hierarchy.

Select a City3 results are available

```

<CascadeSelect v-model="selectedCity" :options="countries" optionLabel="cname" optionGroupLabel="name"
    :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City" />


```

## Forms [#](https://primevue.org/cascadeselect/#forms)

CascadeSelect integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

Select a City3 results are available

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex justify-center flex-col gap-4">
    <div class="flex flex-col gap-1">
        <CascadeSelect name="city" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City" />
        <Message v-if="$form.city?.invalid" severity="error" size="small" variant="simple">{{ $form.city.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Template [#](https://primevue.org/cascadeselect/#template)

CascadeSelect offers multiple slots for customization through templating.

Select a City3 results are available

```

<CascadeSelect v-model="selectedCity" :options="countries" optionLabel="cname" optionGroupLabel="name"
    :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City">
    <template #option="slotProps">
        <div class="flex items-center">
            <img v-if="slotProps.option.states" :alt="slotProps.option.name" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px"  />
            <i v-if="slotProps.option.cities" class="pi pi-compass mr-2"></i>
            <i v-if="slotProps.option.cname" class="pi pi-map-marker mr-2"></i>
            <span>{{ slotProps.option.cname || slotProps.option.name }}</span>
        </div>
    </template>
    <template #dropdownicon>
        <i class="pi pi-map" />
    </template>
    <template #header>
        <div class="font-medium px-3 py-2">Available Countries</div>
    </template>
    <template #footer>
        <div class="px-3 py-1">
            <Button label="Add New" fluid severity="secondary" variant="text" size="small" icon="pi pi-plus" />
        </div>
    </template>
</CascadeSelect>


```

## Loading State [#](https://primevue.org/cascadeselect/#loadingstate)

Loading state can be used *loading* property.

Loading...No results found

```

<CascadeSelect loading placeholder="Loading..." class="w-56" />


```

## Clear Icon [#](https://primevue.org/cascadeselect/#clearicon)

When *showClear* is enabled, a clear icon is added to reset the CascadeSelect.

Select a City3 results are available

```

<CascadeSelect v-model="selectedCity" :options="countries" optionLabel="cname" optionGroupLabel="name"
    :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City" />


```

## Filled [#](https://primevue.org/cascadeselect/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

Select a City3 results are available

```

<CascadeSelect v-model="selectedCity" variant="filled" :options="countries" optionLabel="cname" optionGroupLabel="name"
    :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City" />


```

## Float Label [#](https://primevue.org/cascadeselect/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

p-emptylabel3 results are available

Over Label

p-emptylabel3 results are available

In Label

p-emptylabel3 results are available

On Label

```

<FloatLabel class="w-full md:w-56">
    <CascadeSelect v-model="value1" inputId="over_label" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" class="w-full" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-56">
    <CascadeSelect v-model="value2" inputId="in_label" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" class="w-full" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-56">
    <CascadeSelect v-model="value3" inputId="on_label" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" class="w-full" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/cascadeselect/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

p-emptylabel3 results are available

City

```

<IftaLabel class="w-full md:w-56">
    <CascadeSelect v-model="selectedCity" inputId="cs_city" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" class="w-full" variant="filled" />
    <label for="cs_city">City</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/cascadeselect/#sizes)

CascadeSelect provides *small* and *large* sizes as alternatives to the base.

Small3 results are available

Normal3 results are available

Large3 results are available

```

<CascadeSelect v-model="value1" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" 
    class="w-56" size="small" placeholder="Small" />
<CascadeSelect v-model="value2" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" 
    class="w-56" placeholder="Normal" />
<CascadeSelect v-model="value3" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" 
    class="w-56" size="large" placeholder="Large" />


```

## Invalid [#](https://primevue.org/cascadeselect/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

Select a City3 results are available

Select a City3 results are available

```

<div class="card flex flex-wrap justify-center gap-4">
    <CascadeSelect v-model="selectedCity1" :invalid="!selectedCity1" :options="countries" optionLabel="cname" optionGroupLabel="name" 
        :optionGroupChildren="['states', 'cities']" class="w-full sm:w-56" placeholder="Select a City" />
    <CascadeSelect v-model="selectedCity2" :invalid="!selectedCity2" :options="countries" optionLabel="cname" optionGroupLabel="name" 
        :optionGroupChildren="['states', 'cities']" class="w-full sm:w-56" placeholder="Select a City" variant="filled" />
</div>


```

## Disabled [#](https://primevue.org/cascadeselect/#disabled)

When *disabled* is present, the element cannot be edited and focused.

DisabledNo results found

```

<CascadeSelect disabled placeholder="Disabled" class="w-56" />


```

## Accessibility [#](https://primevue.org/cascadeselect/#accessibility)

### Screen Reader

Value to describe the component can either be provided with *aria-labelledby* or *aria-label* props. The cascadeselect element has a *combobox* role in addition to *aria-haspopup* and *aria-expanded* attributes. The relation between the combobox and the popup is created with *aria-controls* that refers to the id of the popup.

The popup list has an id that refers to the *aria-controls* attribute of the *combobox* element and uses *tree* as the role. Each list item has a *treeitem* role along with *aria-label*, *aria-selected* and *aria-expanded* attributes. The container element of a treenode has the *group* role. The *aria-setsize*, *aria-posinset* and *aria-level* attributes are calculated implicitly and added to each treeitem.

```

<span id="dd1"></span>Options</span>
<CascadeSelect aria-labelledby="dd1" />

<CascadeSelect aria-label="Options" />


```

### Closed State Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the cascadeselect element. |
| *space* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *enter* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *down arrow* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |
| *up arrow* | Opens the popup and moves visual focus to the selected option, if there is none then last option receives the focus. |
| *any printable character* | Opens the popup and moves focus to the option whose label starts with the characters being typed, if there is none then first option receives the focus. |

### Popup Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Hides the popup and moves focus to the next tabbable element. If there is none, the focusable option is selected and the overlay is closed then moves focus to next element in page. |
| *shift* + *tab* | Hides the popup and moves focus to the previous tabbable element. |
| *enter* | Selects the focused option and closes the popup. |
| *space* | Selects the focused option and closes the popup. |
| *escape* | Closes the popup, moves focus to the cascadeselect element. |
| *down arrow* | Moves focus to the next option. |
| *up arrow* | Moves focus to the previous option. |
| *alt* + *up arrow* | Selects the focused option and closes the popup, then moves focus to the cascadeselect element. |
| *right arrow* | If option is closed, opens the option otherwise moves focus to the first child option. |
| *left arrow* | If option is open, closes the option otherwise moves focus to the parent option. |
| *home* | Moves input cursor at the end, if not then moves focus to the first option. |
| *end* | Moves input cursor at the beginning, if not then moves focus to the last option. |
| *any printable character* | Moves focus to the option whose label starts with the characters being typed. |