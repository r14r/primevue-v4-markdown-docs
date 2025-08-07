# TreeTable

TreeTable is used to display hierarchical data in tabular format.

## Import [#](https://primevue.org/treetable/#import)

```

import TreeTable from 'primevue/treetable';
import Column from 'primevue/column';


```

## Basic [#](https://primevue.org/treetable/#basic)

TreeTable requires a collection of *TreeNode* instances as a *value* and *Column* components as children for the representation. The column with the element to toggle a node should have *expander* enabled.

```

<TreeTable :value="nodes" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

## Dynamic Columns [#](https://primevue.org/treetable/#dynamic_columns)

Columns can be created programmatically.

```

<TreeTable :value="nodes" tableStyle="min-width: 50rem">
    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" :expander="col.expander"></Column>
</TreeTable>


```

## Controlled [#](https://primevue.org/treetable/#controlled)

Expansion state is controlled with *expandedKeys* property. The *expandedKeys* should be an object whose keys refer to the node key and values represent the expanded state e.g. *{'0-0': true}*.

```

<Button @click="toggleApplications" label="Toggle Applications" />
<TreeTable v-model:expandedKeys="expandedKeys" :value="nodes" class="mt-6" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

## Template [#](https://primevue.org/treetable/#template)

Custom content at *header* and *footer* slots are supported via templating.

```

<TreeTable :value="nodes" tableStyle="min-width: 50rem">
    <template #header>
        <div class="text-xl font-bold">File Viewer</div>
    </template>
    <Column field="name" header="Name" expander style="width: 250px"></Column>
    <Column field="size" header="Size" style="width: 150px"></Column>
    <Column field="type" header="Type" style="width: 150px"></Column>
    <Column style="width: 10rem">
        <template #body>
            <div class="flex flex-wrap gap-2">
                <Button type="button" icon="pi pi-search" rounded />
                <Button type="button" icon="pi pi-pencil" rounded severity="success" />
            </div>
        </template>
    </Column>
    <template #footer>
        <div class="flex justify-start">
            <Button icon="pi pi-refresh" label="Reload" severity="warn" />
        </div>
    </template>
</TreeTable>


```

## Size [#](https://primevue.org/treetable/#size)

In addition to a regular table, alternatives with alternative sizes are available.

```

<TreeTable :value="nodes" :size="size.value" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

## Pagination [#](https://primevue.org/treetable/#pagination)

### Basic [#](https://primevue.org/treetable/#paginator_basic)

Pagination is enabled by adding *paginator* property and defining *rows* per page.

```

<TreeTable :value="nodes" :paginator="true" :rows="5" :rowsPerPageOptions="[5, 10, 25]" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

### Template [#](https://primevue.org/treetable/#paginator_template)

Paginator UI is customized using the *paginatorTemplate* property. Each element can also be customized further with your own UI to replace the default one, refer to the [Paginator](https://primevue.org/paginator/) component for more information about the advanced customization options.

```

<TreeTable
    :value="nodes"
    :paginator="true"
    :rows="5"
    :rowsPerPageOptions="[5, 10, 25, 50]"
    paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
    currentPageReportTemplate="{first} to {last} of {totalRecords}"
    tableStyle="min-width: 50rem"
>
    <template #paginatorstart>
        <Button type="button" icon="pi pi-refresh" text />
    </template>
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
    <template #paginatorend>
        <Button type="button" icon="pi pi-download" text />
    </template>
</TreeTable>


```

### Headless [#](https://primevue.org/treetable/#paginator_headless)

Pagination is enabled by adding *paginator* property and defining *rows* per page.

```

<TreeTable :value="nodes" :paginator="true" :rows="5" :rowsPerPageOptions="[5, 10, 25]" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
    <template #paginatorcontainer="{ first, last, page, pageCount, prevPageCallback, nextPageCallback, totalRecords }">
        <div class="flex items-center gap-4 border border-primary bg-transparent rounded-full w-full py-1 px-2 justify-between">
            <Button icon="pi pi-chevron-left" rounded text @click="prevPageCallback" :disabled="page === 0" />
            <div class="text-color font-medium">
                <span class="hidden sm:block">Showing {{ first }} to {{ last }} of {{ totalRecords }}</span>
                <span class="block sm:hidden">Page {{ page + 1 }} of {{ pageCount }}</span>
            </div>
            <Button icon="pi pi-chevron-right" rounded text @click="nextPageCallback" :disabled="page === pageCount - 1" />
        </div>
    </template>
</TreeTable>


```

## Sort [#](https://primevue.org/treetable/#sort)

### Single Column [#](https://primevue.org/treetable/#single_sort)

Sorting on a column is enabled by adding the *sortable* property.

```

<TreeTable :value="nodes" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" sortable expander style="width: 34%"></Column>
    <Column field="size" header="Size" sortable style="width: 33%"></Column>
    <Column field="type" header="Type" sortable style="width: 33%"></Column>
</TreeTable>


```

### Multiple Columns [#](https://primevue.org/treetable/#multiple_sort)

Multiple columns can be sorted by defining *sortMode* as *multiple*. This mode requires metaKey (e.g. *⌘*) to be pressed when clicking a header.

```

<TreeTable :value="nodes" sortMode="multiple" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" sortable expander style="width: 34%"></Column>
    <Column field="size" header="Size" sortable style="width: 33%"></Column>
    <Column field="type" header="Type" sortable style="width: 33%"></Column>
</TreeTable>


```

### Removable Sort [#](https://primevue.org/treetable/#removable_sort)

When *removableSort* is present, the third click removes the sorting from the column.

```

<TreeTable :value="nodes" sortMode="multiple" removableSort tableStyle="min-width: 50rem">
    <Column field="name" header="Name" sortable expander style="width: 34%"></Column>
    <Column field="size" header="Size" sortable style="width: 33%"></Column>
    <Column field="type" header="Type" sortable style="width: 33%"></Column>
</TreeTable>


```

## Filter [#](https://primevue.org/treetable/#filter)

Filtering is enabled by adding the *filter* property to a Column. The *filterMode* specifies the filtering strategy, in *lenient* mode when the query matches a node, children of the node are not searched further as all descendants of the node are included. On the other hand, in *strict* mode when the query matches a node, filtering continues on all descendants. A general filled called *globalFilter* is also provided to search all columns that support filtering.

```

<SelectButton v-model="filterMode" optionLabel="label" dataKey="label" :options="filterOptions" />
<TreeTable :value="nodes" :filters="filters" :filterMode="filterMode.value">
    <template #header>
        <div class="flex justify-end">
            <IconField>
                <InputIcon class="pi pi-search" />
                <InputText v-model="filters['global']" placeholder="Global Search" />
            </IconField>
        </div>
    </template>
    <Column field="name" header="Name" expander style="min-width: 12rem">
        <template #filter>
            <InputText v-model="filters['name']" type="text" placeholder="Filter by name" />
        </template>
    </Column>
    <Column field="size" header="Size" style="min-width: 12rem">
        <template #filter>
            <InputText v-model="filters['size']" type="text" placeholder="Filter by size" />
        </template>
    </Column>
    <Column field="type" header="Type" style="min-width: 12rem">
        <template #filter>
            <InputText v-model="filters['type']" type="text" placeholder="Filter by type" />
        </template>
    </Column>
</TreeTable>


```

## Selection [#](https://primevue.org/treetable/#selection)

### Single [#](https://primevue.org/treetable/#single_row_selection)

Single node selection is configured by setting *selectionMode* as *single* along with *selectionKeys* property to manage the selection value binding.

By default, metaKey press (e.g. *⌘*) is necessary to unselect a node however this can be configured with disabling the *metaKeySelection* property. In touch enabled devices this option has no effect and behavior is same as setting it to false.

```

<ToggleSwitch v-model="metaKey" inputId="input-metakey" />

<TreeTable v-model:selectionKeys="selectedKey" :value="nodes" selectionMode="single" :metaKeySelection="metaKey" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

### Multiple [#](https://primevue.org/treetable/#multiple_rows_selection)

More than one node is selectable by setting *selectionMode* to *multiple*. By default in multiple selection mode, metaKey press (e.g. *⌘*) is not necessary to add to existing selections. When the optional *metaKeySelection* is present, behavior is changed in a way that selecting a new node requires meta key to be present. Note that in touch enabled devices, TreeTable always ignores metaKey.

In multiple selection mode, value binding should be a key-value pair where key is the node key and value is a boolean to indicate selection.

```

<ToggleSwitch v-model="metaKey" inputId="input-metakey" />

<TreeTable v-model:selectionKeys="selectedKey" :value="nodes" selectionMode="multiple" :metaKeySelection="metaKey" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

### Checkbox [#](https://primevue.org/treetable/#checkbox_row_selection)

Selection of multiple nodes via checkboxes is enabled by configuring *selectionMode* as *checkbox*.

In checkbox selection mode, value binding should be a key-value pair where key (or the dataKey) is the node key and value is an object that has *checked* and *partialChecked* properties to represent the checked state of a node.

```

{
    '0-0': {
        partialChecked: false,
        checked: true
    }
}


```

```

<TreeTable v-model:selectionKeys="selectedKey" :value="nodes" selectionMode="checkbox" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

### Events [#](https://primevue.org/treetable/#row_selection_events)

TreeTable provides *nodeSelect* and *nodeUnselect* events to listen selection events.

```

<TreeTable v-model:selectionKeys="selectedKey" :value="nodes" selectionMode="single" @nodeSelect="onNodeSelect" @nodeUnselect="onNodeUnselect" :metaKeySelection="false" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

## Lazy Load [#](https://primevue.org/treetable/#lazy_load)

Lazy mode is handy to deal with large datasets, instead of loading the entire data, small chunks of data is loaded by invoking corresponding callbacks everytime *paging*, *sorting* and *filtering* occurs. Sample below imitates lazy loading data from a remote datasource using an in-memory list and timeouts to mimic network connection.

Enabling the *lazy* property and assigning the logical number of rows to *totalRecords* by doing a projection query are the key elements of the implementation so that paginator displays the UI assuming there are actually records of totalRecords size although in reality they are not present on page, only the records that are displayed on the current page exist.

In addition, only the root elements should be loaded, children can be loaded on demand using *nodeExpand* callback.

```

<TreeTable :value="nodes" :lazy="true" :paginator="true" :rows="rows" :loading="loading"
    @nodeExpand="onExpand" @page="onPage" :totalRecords="totalRecords" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander></Column>
    <Column field="size" header="Size"></Column>
    <Column field="type" header="Type"></Column>
</TreeTable>


```

## Scroll [#](https://primevue.org/treetable/#scroll)

### Vertical [#](https://primevue.org/treetable/#vertical_scroll)

Adding *scrollable* property along with a *scrollHeight* for the data viewport enables vertical scrolling with fixed headers.

```

<TreeTable :value="nodes" scrollable scrollHeight="270px" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

### Flexible [#](https://primevue.org/treetable/#flex_scroll)

Flex scroll feature makes the scrollable viewport section dynamic instead of a fixed value so that it can grow or shrink relative to the parent size of the table. Click the button below to display a maximizable Dialog where data viewport adjusts itself according to the size changes.

```

<Button label="Show" icon="pi pi-external-link" @click="dialogVisible = true" />
<Dialog v-model:visible="dialogVisible" header="Flex Scroll" :style="{ width: '75vw' }" maximizable modal :contentStyle="{ height: '300px' }">
    <TreeTable :value="nodes" :scrollable="true" scrollHeight="flex" tableStyle="min-width: 50rem">
        <Column field="name" header="Name" :expander="true" style="min-width: 200px"></Column>
        <Column field="size" header="Size" style="min-width: 200px"></Column>
        <Column field="type" header="Type" style="min-width: 200px"></Column>
    </TreeTable>
    <template #footer>
        <Button label="Ok" icon="pi pi-check" @click="dialogVisible = false" />
    </template>
</Dialog>


```

### Horizontal [#](https://primevue.org/treetable/#horizontal_scroll)

Horizontal scrollbar is displayed when table width exceeds the parent width.

```

<TreeTable :value="nodes" scrollable scrollHeight="300px">
    <Column field="name" header="Name" expander style="min-width: 250px"></Column>
    <Column field="size" header="Size" style="min-width: 200px"></Column>
    <Column field="type" header="Type 2" style="min-width: 200px"></Column>
    <Column field="size" header="Size 2" style="min-width: 200px"></Column>
    <Column field="type" header="Type 3" style="min-width: 200px"></Column>
    <Column field="size" header="Size 3" style="min-width: 200px"></Column>
</TreeTable>


```

### Frozen Columns [#](https://primevue.org/treetable/#frozen_columns)

A column can be fixed during horizontal scrolling by enabling the *frozen* property on a Column. The location is defined with the *alignFrozen* that can be *left* or *right*.

```

<TreeTable :value="nodes" scrollable scrollHeight="300px">
    <Column field="name" header="Name" expander frozen style="min-width: 250px" class="font-bold"></Column>
    <Column field="size" header="Size" style="min-width: 200px"></Column>
    <Column field="type" header="Type 2" style="min-width: 200px"></Column>
    <Column field="size" header="Size 2" style="min-width: 200px"></Column>
    <Column field="type" header="Type 3" style="min-width: 200px"></Column>
    <Column field="size" header="Size 3" style="min-width: 200px"></Column>
</TreeTable>


```

## Column Resize [#](https://primevue.org/treetable/#column_resize)

### Fit Mode [#](https://primevue.org/treetable/#resize_fitmode)

Columns can be resized with drag and drop when *resizableColumns* is enabled. Default resize mode is *fit* that does not change the overall table width.

```

<TreeTable :value="nodes" :resizableColumns="true" showGridlines tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander></Column>
    <Column field="size" header="Size"></Column>
    <Column field="type" header="Type"></Column>
</TreeTable>


```

### Expand Mode [#](https://primevue.org/treetable/#resize_expandmode)

Setting *columnResizeMode* as *expand* changes the table width as well.

```

<TreeTable :value="nodes" :resizableColumns="true" columnResizeMode="expand" showGridlines tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander></Column>
    <Column field="size" header="Size"></Column>
    <Column field="type" header="Type"></Column>
</TreeTable>


```

## Column Toggle [#](https://primevue.org/treetable/#column_toggle)

Column visibility based on a condition can be implemented with dynamic columns, in this sample a MultiSelect is used to manage the visible columns.

```

<TreeTable :value="nodes" tableStyle="min-width: 50rem">
    <template #header>
        <div style="text-align:left">
            <MultiSelect :modelValue="selectedColumns" @update:modelValue="onToggle" :options="columns" optionLabel="header" class="w-full sm:w-64" display="chip"/>
        </div>
    </template>
    <Column field="name" header="Name" :expander="true"></Column>
    <Column v-for="col of selectedColumns" :field="col.field" :header="col.header" :key="col.field"></Column>
</TreeTable>


```

## ContextMenu [#](https://primevue.org/treetable/#contextmenu)

TreeTable has exclusive integration with ContextMenu using the *contextMenu* event to open a menu on right click along with *contextMenuSelection* property and *row-contextmenu* event to control the selection via the menu.

```

<ContextMenu ref="cm" :model="menuModel" @hide="selectedNode = null" />
<TreeTable v-model:contextMenuSelection="selectedNode" :value="nodes" contextMenu @row-contextmenu="onRowContextMenu" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>


```

## Accessibility [#](https://primevue.org/treetable/#accessibility)

### Screen Reader

DataTable uses a *treegrid* element whose attributes can be extended with the *tableProps* option. This property allows passing aria roles and attributes like *aria-label* and *aria-describedby* to define the table for readers. Default role of the table is *table*. Header, body and footer elements use *rowgroup*, rows use *row* role, header cells have *columnheader* and body cells use *cell* roles. Sortable headers utilizer *aria-sort* attribute either set to "ascending" or "descending".

Row elements manage *aria-expanded* for state along with *aria-posinset*, *aria-setsize* and *aria-level* attribute to define the hierachy.

When selection is enabled, *aria-selected* is set to true on a row. In checkbox mode, TreeTable component uses a hidden native checkbox element.

Editable cells use custom templating so you need to manage aria roles and attributes manually if required.

Paginator is a standalone component used inside the DataTable, refer to the [paginator](https://primevue.org/paginator/) for more information about the accessibility features.

### Sortable Headers Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves through the headers. |
| *enter* | Sorts the column. |
| *space* | Sorts the column. |

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
| *home* | Moves focus to the first same-level node. |
| *end* | Moves focus to the last same-level node. |