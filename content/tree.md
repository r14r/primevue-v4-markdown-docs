# Tree

Tree is used to display hierarchical data.

## Import [#](https://primevue.org/tree/#import)

```

import Tree from 'primevue/tree';


```

## Basic [#](https://primevue.org/tree/#basic)

Tree component requires an array of TreeNode objects as its *value*.

```

<Tree :value="nodes" class="w-full md:w-[30rem]"></Tree>


```

## Controlled [#](https://primevue.org/tree/#controlled)

Tree state can be controlled programmatically with the *expandedKeys* property that defines the keys that are expanded. This property is a Map instance whose key is the key of a node and value is a boolean. Note that *expandedKeys* also supports two-way binding with the v-model directive.

Expand AllCollapse All

```

<div class="flex flex-wrap gap-2 mb-6">
    <Button type="button" icon="pi pi-plus" label="Expand All" @click="expandAll" />
    <Button type="button" icon="pi pi-minus" label="Collapse All" @click="collapseAll" />
</div>
<Tree v-model:expandedKeys="expandedKeys" :value="nodes" class="w-full md:w-[30rem]"></Tree>


```

## Selection [#](https://primevue.org/tree/#selection)

### Single [#](https://primevue.org/tree/#single)

Single node selection is configured by setting *selectionMode* as *single* along with *selectionKeys* property to manage the selection value binding.

```

<Tree v-model:selectionKeys="selectedKey" :value="nodes" selectionMode="single" class="w-full md:w-[30rem]"></Tree>


```

### Multiple [#](https://primevue.org/tree/#multiple)

More than one node is selectable by setting *selectionMode* to *multiple*. By default in multiple selection mode, metaKey press (e.g. *⌘*) is not necessary to add to existing selections. When the optional *metaKeySelection* is present, behavior is changed in a way that selecting a new node requires meta key to be present. Note that in touch enabled devices, Tree always ignores metaKey.

In multiple selection mode, value binding should be a key-value pair where key is the node key and value is a boolean to indicate selection.

MetaKey

```

<Tree v-model:selectionKeys="selectedKeys" :value="nodes"
    selectionMode="multiple" :metaKeySelection="checked"></Tree>


```

### Checkbox [#](https://primevue.org/tree/#checkbox)

Selection of multiple nodes via checkboxes is enabled by configuring *selectionMode* as *checkbox*.

In checkbox selection mode, value binding should be a key-value pair where key is the node key and value is an object that has *checked* and *partialChecked* properties to represent the checked state of a node object to indicate selection.

```

<Tree v-model:selectionKeys="selectedKey" :value="nodes" selectionMode="checkbox" class="w-full md:w-[30rem]"></Tree>


```

## Events [#](https://primevue.org/tree/#events)

An event is provided for each type of user interaction such as expand, collapse and selection.

```

<Tree v-model:selectionKeys="selectedKey" :value="nodes" selectionMode="single" :metaKeySelection="false"
    @nodeSelect="onNodeSelect" @nodeUnselect="onNodeUnselect" @nodeExpand="onNodeExpand" @nodeCollapse="onNodeCollapse" class="w-full md:w-[30rem]"></Tree>


```

## Lazy [#](https://primevue.org/tree/#lazy)

Lazy loading is useful when dealing with huge datasets, in this example nodes are dynamically loaded on demand using *loading* property and *node-expand* method. Default value of *loadingMode* is *mask* and also *icon* is available.

Mask Mode

Icon Mode

```

<Tree :value="nodes" @node-expand="onNodeExpand" :loading="loading" class="w-full md:w-[30rem]"></Tree>
<Tree :value="nodes2" @node-expand="onNodeExpand2" loadingMode="icon" class="w-full md:w-[30rem]"></Tree>


```

## Template [#](https://primevue.org/tree/#template)

Each node can have a distinct template by matching the *type* property to the slot name.

* **Introduction**
* **Components In-Depth**

```

<Tree :value="nodes" class="w-full md:w-[30rem]">
    <template #default="slotProps">
        <b>{{ slotProps.node.label }}</b>
    </template>
    <template #url="slotProps">
        <a :href="slotProps.node.data">{{ slotProps.node.label }}</a>
    </template>
</Tree>


```

## Filter [#](https://primevue.org/tree/#filter)

Filtering is enabled by adding the *filter* property, by default label property of a node is used to compare against the value in the text field, in order to customize which field(s) should be used during search define *filterBy* property. In addition *filterMode* specifies the filtering strategy. In *lenient* mode when the query matches a node, children of the node are not searched further as all descendants of the node are included. On the other hand, in *strict* mode when the query matches a node, filtering continues on all descendants.

```

<Tree :value="nodes" :filter="true" filterMode="lenient" class="w-full md:w-[30rem]"></Tree>
<Tree :value="nodes" :filter="true" filterMode="strict" class="w-full md:w-[30rem]"></Tree>


```

## Accessibility [#](https://primevue.org/tree/#accessibility)

### Screen Reader

Value to describe the component can either be provided with *aria-labelledby* or *aria-label* props. The root list element has a *tree* role whereas each list item has a *treeitem* role along with *aria-label*, *aria-selected* and *aria-expanded* attributes. In checkbox selection, *aria-checked* is used instead of *aria-selected*. The container element of a treenode has the *group* role. Checkbox and toggle icons are hidden from screen readers as their parent element with *treeitem* role and attributes are used instead for readers and keyboard support. The *aria-setsize*, *aria-posinset* and *aria-level* attributes are calculated implicitly and added to each treeitem.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the first selected node when focus enters the component, if there is none then first element receives the focus. If focus is already inside the component, moves focus to the next focusable element in the page tab sequence. |
| *shift* + *tab* | Moves focus to the last selected node when focus enters the component, if there is none then first element receives the focus. If focus is already inside the component, moves focus to the previous focusable element in the page tab sequence. |
| *enter* | Selects the focused treenode. |
| *space* | Selects the focused treenode. |
| *down arrow* | Moves focus to the next treenode. |
| *up arrow* | Moves focus to the previous treenode. |
| *right arrow* | If node is closed, opens the node otherwise moves focus to the first child node. |
| *left arrow* | If node is open, closes the node otherwise moves focus to the parent node. |