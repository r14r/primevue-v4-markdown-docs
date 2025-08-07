# TreeSelect

TreeSelect is a form component to choose from hierarchical data.

## Import [#](https://primevue.org/treeselect/#import)

```

import TreeSelect from 'primevue/treeselect';


```

## Basic [#](https://primevue.org/treeselect/#basic)

TreeSelect is used with the *v-model* property for two-way value binding along with the *options* collection. Internally [Tree](https://primevue.org/tree/) component is used so the options model is based on TreeNode API.

In single selection mode, value binding should be the *key* value of a node.

Select Item

```

<TreeSelect v-model="selectedValue" :options="nodes" placeholder="Select Item" class="md:w-80 w-full" />


```

## Forms [#](https://primevue.org/treeselect/#forms)

TreeSelect is used with the *v-model* property.

Select Item

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full md:w-80">
    <div class="flex flex-col gap-1">
        <TreeSelect name="node" :options="nodes" placeholder="Select Item" fluid />
        <Message v-if="$form.node?.invalid" severity="error" size="small" variant="simple">{{ $form.node.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## Multiple [#](https://primevue.org/treeselect/#multiple)

More than one node is selectable by setting *selectionMode* to *multiple*. By default in multiple selection mode, metaKey press (e.g. *⌘*) is not necessary to add to existing selections. When the optional *metaKeySelection* is present, behavior is changed in a way that selecting a new node requires meta key to be present. Note that in touch enabled devices, TreeSelect always ignores metaKey.

In multiple selection mode, value binding should be a key-value pair where key is the node key and value is a boolean to indicate selection.

```

{
    '0-0': true,
    '0-1-0': true
}


```

Select Items

```

<TreeSelect v-model="selectedValue" :options="nodes" selectionMode="multiple" display="chip" :maxSelectedLabels="3" placeholder="Select Items" class="md:w-80 w-full" />


```

## Checkbox [#](https://primevue.org/treeselect/#checkbox)

Selection of multiple nodes via checkboxes is enabled by configuring *selectionMode* as *checkbox*.

In checkbox selection mode, value binding should be a key-value pair where key is the node key and value is an object that has *checked* and *partialChecked* properties to represent the checked state of a node object to indicate selection.

```

{
    '0-0': {
        partialChecked: false,
        checked: true
    }
}


```

Select Items

```

<TreeSelect v-model="selectedValue" :options="nodes" selectionMode="checkbox" placeholder="Select Item" class="md:w-80 w-full" />


```

## Lazy [#](https://primevue.org/treeselect/#lazy)

Lazy loading is useful when dealing with huge datasets, in this example nodes are dynamically loaded on demand using *loading* property and *node-expand* method. Default value of *loadingMode* is *mask* and also *icon* is available.

Select Item

Select Item

```

<TreeSelect v-model="selectedValue" :loading="loading" :options="nodes" @node-expand="onNodeExpand" placeholder="Select Item" class="md:w-80 w-full" />
<TreeSelect v-model="selectedValue2" loadingMode="icon" :options="nodes2" @node-expand="onNodeExpand2" placeholder="Select Item" class="md:w-80 w-full" />


```

## Filter [#](https://primevue.org/treeselect/#filter)

Filtering is enabled by adding the *filter* property, by default label property of a node is used to compare against the value in the text field, in order to customize which field(s) should be used during search define *filterBy* property. In addition *filterMode* specifies the filtering strategy. In *lenient* mode when the query matches a node, children of the node are not searched further as all descendants of the node are included. On the other hand, in *strict* mode when the query matches a node, filtering continues on all descendants.

Select Item

Select Item

```

<TreeSelect v-model="selectedValue" filter filterMode="lenient" :options="nodes" placeholder="Select Item" class="md:w-80 w-full" />
<TreeSelect v-model="selectedValue" filter filterMode="strict" :options="nodes" placeholder="Select Item" class="md:w-80 w-full" />


```

## Clear Icon [#](https://primevue.org/treeselect/#clearicon)

When *showClear* is enabled, a clear icon is added to reset the TreeSelect.

Select Item

```

<TreeSelect v-model="selectedValue" :options="nodes" placeholder="Select Item" class="md:w-80 w-full" />


```

## Template [#](https://primevue.org/treeselect/#template)

TreeSelect offers multiple slots for customization through templating.

Select Item

```

<TreeSelect v-model="selectedValue" :options="nodes" placeholder="Select Item" class="md:w-80 w-full">
    <template #dropdownicon>
        <i class="pi pi-search" />
    </template>
    <template #header>
        <div class="font-medium px-3 py-2">Available Files</div>
    </template>
    <template #footer>
        <div class="px-3 pt-1 pb-2 flex justify-between">
            <Button label="Add New" severity="secondary" text size="small" icon="pi pi-plus" />
            <Button label="Remove All" severity="danger" text size="small" icon="pi pi-plus" />
        </div>
    </template>
</TreeSelect>


```

## Filled [#](https://primevue.org/treeselect/#filled)

Specify the *variant* property as *filled* to display the component with a higher visual emphasis than the default *outlined* style.

Select Item

```

<TreeSelect v-model="selectedValue" variant="filled" :options="nodes" placeholder="Select Item" class="md:w-80 w-full" />


```

## Float Label [#](https://primevue.org/treeselect/#floatlabel)

A floating label appears on top of the input field when focused. Visit [FloatLabel](https://primevue.org/floatlabel/) documentation for more information.

empty

Over Label

empty

In Label

empty

On Label

```

<FloatLabel class="w-full md:w-80">
    <TreeSelect v-model="value1" inputId="over_label" :options="nodes" class="w-full" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="in">
    <TreeSelect v-model="value2" inputId="in_label" :options="nodes" class="w-full" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="on">
    <TreeSelect v-model="value3" inputId="on_label" :options="nodes" class="w-full" />
    <label for="on_label">On Label</label>
</FloatLabel>


```

## Ifta Label [#](https://primevue.org/treeselect/#iftalabel)

IftaLabel is used to create infield top aligned labels. Visit [IftaLabel](https://primevue.org/iftalabel/) documentation for more information.

empty

File

```

<IftaLabel class="w-full md:w-80">
    <TreeSelect v-model="selectedValue" inputId="t_file" :options="nodes" class="w-full" variant="filled" />
    <label for="t_file">File</label>
</IftaLabel>


```

## Sizes [#](https://primevue.org/treeselect/#sizes)

TreeSelect provides *small* and *large* sizes as alternatives to the base.

Small

Normal

Large

```

<TreeSelect v-model="value1" :options="nodes" size="small" placeholder="Small" class="md:w-80 w-full" />
<TreeSelect v-model="value2" :options="nodes" placeholder="Normal" class="md:w-80 w-full" />
<TreeSelect v-model="value3" :options="nodes" size="large" placeholder="Large" class="md:w-80 w-full" />


```

## Invalid [#](https://primevue.org/treeselect/#invalid)

Invalid state is displayed using the *invalid* prop to indicate a failed validation. You can use this style when integrating with form validation libraries.

TreeSelect

TreeSelect

```

<TreeSelect v-model="selectedValue1" :invalid="Object.keys(selectedValue1).length === 0" class="md:w-80 w-full" :options="nodes" placeholder="TreeSelect" />
<TreeSelect v-model="selectedValue2" :invalid="Object.keys(selectedValue2).length === 0" class="md:w-80 w-full" :options="nodes" placeholder="TreeSelect" variant="filled" />


```

## Disabled [#](https://primevue.org/treeselect/#disabled)

When *disabled* is present, the element cannot be edited and focused.

TreeSelect

```

<TreeSelect v-model="selectedValue" disabled class="md:w-80 w-full" :options="nodes" placeholder="TreeSelect" />


```

## Accessibility [#](https://primevue.org/treeselect/#accessibility)

### Screen Reader

Value to describe the component can either be provided with *aria-labelledby* or *aria-label* props. The treeselect element has a *combobox* role in addition to *aria-haspopup* and *aria-expanded* attributes. The relation between the combobox and the popup is created with *aria-controls* that refers to the id of the popup.

The popup list has an id that refers to the *aria-controls* attribute of the *combobox* element and uses *tree* as the role. Each list item has a *treeitem* role along with *aria-label*, *aria-selected* and *aria-expanded* attributes. In checkbox selection, *aria-checked* is used instead of *aria-selected*. Checkbox and toggle icons are hidden from screen readers as their parent element with *treeitem* role and attributes are used instead for readers and keyboard support. The container element of a treenode has the *group* role. The *aria-setsize*, *aria-posinset* and *aria-level* attributes are calculated implicitly and added to each treeitem.

```

<span id="dd1">Options</span>
<TreeSelect aria-labelledby="dd1" />

<TreeSelect aria-label="Options" />


```

### Closed State Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the treeselect element. |
| *space* | Opens the popup and moves visual focus to the selected treenode, if there is none then first treenode receives the focus. |
| *down arrow* | Opens the popup and moves visual focus to the selected option, if there is none then first option receives the focus. |

### Popup Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next focusable element in the page tab sequence. |
| *shift* + *tab* | Moves focus to the previous focusable element in the page tab sequence. |
| *enter* | Selects the focused option, closes the popup if selection mode is single. |
| *space* | Selects the focused option, closes the popup if selection mode is single. |
| *escape* | Closes the popup, moves focus to the treeselect element. |
| *down arrow* | Moves focus to the next treenode. |
| *up arrow* | Moves focus to the previous treenode. |
| *right arrow* | If node is closed, opens the node otherwise moves focus to the first child node. |
| *left arrow* | If node is open, closes the node otherwise moves focus to the parent node. |