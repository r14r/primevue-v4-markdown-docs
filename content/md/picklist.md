# PickList

PickList is used to reorder items between different lists.

## Import [#](https://primevue.org/picklist/#import)

```

import PickList from 'primevue/picklist';


```

## Basic [#](https://primevue.org/picklist/#basic)

PickList requires a multidimensional array as its value bound with the *v-model* directive and a template for its content that gets the *option* instance and the index via slotProps.

* No available options

No available optionsNo selected item

* No available options

No available optionsNo selected item

```

<PickList v-model="products" dataKey="id" breakpoint="1400px">
    <template #option="{ option  }">
        {{ option.name }}
    </template>
</PickList>


```

## Template [#](https://primevue.org/picklist/#template)

For custom content support define an *option* template that gets the item instance as a parameter. In addition *sourceheader* and *targetheader* slots are provided for further customization.

* No available options

No available optionsNo selected item

* No available options

No available optionsNo selected item

```

<PickList v-model="products" dataKey="id" breakpoint="1400px" scrollHeight="20rem">
    <template #option="{ option , selected }">
        <div class="flex flex-wrap p-1 items-center gap-4 w-full">
            <img class="w-12 shrink-0 rounded" :src="'https://primefaces.org/cdn/primevue/images/product/' + option.image" :alt="option.name" />
            <div class="flex-1 flex flex-col">
                <span class="font-medium text-sm">{{ option.name }}</span>
                <span :class="['text-sm', { 'text-surface-500 dark:text-surface-400': !selected, 'text-inherit': selected }]">{{ option.category }}</span>
            </div>
            <span class="font-bold">${{ option.price }}</span>
        </div>
    </template>
</PickList>


```

## Accessibility [#](https://primevue.org/picklist/#accessibility)

### Screen Reader

Value to describe the source listbox and target listbox can be provided with *sourceListProps* and *targetListProps* by passing *aria-labelledby* or *aria-label* props. The list elements has a *listbox* role with the *aria-multiselectable* attribute. Each list item has an *option* role with *aria-selected* as their attributes.

Controls buttons are *button* elements with an *aria-label* that refers to the *aria.moveTop*, *aria.moveUp*, *aria.moveDown*, *aria.moveBottom*,*aria.moveToTarget*, *aria.moveAllToTarget*, *aria.moveToSource* and *aria.moveAllToSource* properties of the [locale](https://primevue.org/configuration/#locale) API by default, alternatively you may use *moveTopButtonProps*, *moveUpButtonProps*, *moveDownButtonProps*, *moveToButtonProps*, *moveAllToButtonProps*, *moveFromButtonProps*, *moveFromButtonProps* *moveAllFromButtonProps* *moveToTargetProps*, *moveAllToTargetProps*, *moveToSourceProps* and *moveAllToSourceProps* to customize the buttons like overriding the default *aria-label* attributes.

```

<span id="lb">Options</span>
<PickList aria-labelledby="lb" />

<PickList aria-label="City" />


```

### ListBox Keyboard Support

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
| *control* + *shift* + *end* | Selects the focused options and all the options down to the first one. |
| *control* + *a* | Selects all options. |

### Buttons Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Executes button action. |
| *space* | Executes button action. |