# DataTable

DataTable displays data in tabular format.

## Import [#](https://primevue.org/datatable/#import)

```

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';                   // optional


```

## Basic [#](https://primevue.org/datatable/#basic)

DataTable requires a *value* as data to display and *Column* components as children for the representation.

```

<DataTable :value="products" tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

## Dynamic Columns [#](https://primevue.org/datatable/#dynamic_columns)

Columns can be created programmatically.

```

<DataTable :value="products" tableStyle="min-width: 50rem">
    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header"></Column>
</DataTable>


```

## Template [#](https://primevue.org/datatable/#template)

Custom content at *header* and *footer* sections are supported via templating.

```

<DataTable :value="products" tableStyle="min-width: 50rem">
    <template #header>
        <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="text-xl font-bold">Products</span>
            <Button icon="pi pi-refresh" rounded raised />
        </div>
    </template>
    <Column field="name" header="Name"></Column>
    <Column header="Image">
        <template #body="slotProps">
            <img :src="`https://primefaces.org/cdn/primevue/images/product/${slotProps.data.image}`" :alt="slotProps.data.image" class="w-24 rounded" />
        </template>
    </Column>
    <Column field="price" header="Price">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.price) }}
        </template>
    </Column>
    <Column field="category" header="Category"></Column>
    <Column field="rating" header="Reviews">
        <template #body="slotProps">
            <Rating :modelValue="slotProps.data.rating" readonly />
        </template>
    </Column>
    <Column header="Status">
        <template #body="slotProps">
            <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data)" />
        </template>
    </Column>
    <template #footer> In total there are {{ products ? products.length : 0 }} products. </template>
</DataTable>


```

## Size [#](https://primevue.org/datatable/#size)

In addition to a regular table, alternatives with alternative sizes are available.

```

<SelectButton v-model="size" :options="sizeOptions" optionLabel="label" dataKey="label" />
<DataTable :value="products" :size="size.value" tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

## Grid Lines [#](https://primevue.org/datatable/#gridlines)

Enabling *showGridlines* displays borders between cells.

```

<DataTable :value="products" showGridlines tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

## Striped Rows [#](https://primevue.org/datatable/#striped)

Alternating rows are displayed when *stripedRows* property is present.

```

<DataTable :value="products" stripedRows tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

## Pagination [#](https://primevue.org/datatable/#pagination)

### Basic [#](https://primevue.org/datatable/#paginator_basic)

Pagination is enabled by adding *paginator* property and defining *rows* per page.

```

<DataTable :value="customers" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" style="width: 25%"></Column>
    <Column field="country.name" header="Country" style="width: 25%"></Column>
    <Column field="company" header="Company" style="width: 25%"></Column>
    <Column field="representative.name" header="Representative" style="width: 25%"></Column>
</DataTable>


```

### Template [#](https://primevue.org/datatable/#paginator_template)

Paginator UI is customized using the *paginatorTemplate* property. Each element can also be customized further with your own UI to replace the default one, refer to the [Paginator](https://primevue.org/paginator/) component for more information about the advanced customization options.

```

<DataTable :value="customers" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem"
        paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
        currentPageReportTemplate="{first} to {last} of {totalRecords}">
    <template #paginatorstart>
        <Button type="button" icon="pi pi-refresh" text />
    </template>
    <template #paginatorend>
        <Button type="button" icon="pi pi-download" text />
    </template>
    <Column field="name" header="Name" style="width: 25%"></Column>
    <Column field="country.name" header="Country" style="width: 25%"></Column>
    <Column field="company" header="Company" style="width: 25%"></Column>
    <Column field="representative.name" header="Representative" style="width: 25%"></Column>
</DataTable>


```

### Headless [#](https://primevue.org/datatable/#paginator_headless)

Headless mode on Pagination is enabled by adding using *paginatorcontainer*.

```

<DataTable :value="customers" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" style="width: 25%"></Column>
    <Column field="country.name" header="Country" style="width: 25%"></Column>
    <Column field="company" header="Company" style="width: 25%"></Column>
    <Column field="representative.name" header="Representative" style="width: 25%"></Column>
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
</DataTable>


```

## Sort [#](https://primevue.org/datatable/#sort)

### Single Column [#](https://primevue.org/datatable/#single_sort)

Sorting on a column is enabled by adding the *sortable* property.

```

<DataTable :value="products" tableStyle="min-width: 50rem">
    <Column field="code" header="Code" sortable style="width: 25%"></Column>
    <Column field="name" header="Name" sortable style="width: 25%"></Column>
    <Column field="category" header="Category" sortable style="width: 25%"></Column>
    <Column field="quantity" header="Quantity" sortable style="width: 25%"></Column>
</DataTable>


```

### Multiple Columns [#](https://primevue.org/datatable/#multiple_sort)

Multiple columns can be sorted by defining *sortMode* as *multiple*. This mode requires metaKey (e.g. *⌘*) to be pressed when clicking a header.

```

<DataTable :value="products" sortMode="multiple" tableStyle="min-width: 50rem">
    <Column field="code" header="Code" sortable style="width: 25%"></Column>
    <Column field="name" header="Name" sortable style="width: 25%"></Column>
    <Column field="category" header="Category" sortable style="width: 25%"></Column>
    <Column field="quantity" header="Quantity" sortable style="width: 25%"></Column>
</DataTable>


```

### Presort [#](https://primevue.org/datatable/#pre_sort)

Defining a default *sortField* and *sortOrder* displays data as sorted initially in single column sorting. In *multiple* sort mode, *multiSortMeta* should be used instead by providing an array of *DataTableSortMeta* objects.

```

<DataTable :value="products" sortField="price" :sortOrder="-1" tableStyle="min-width: 50rem">
    <Column field="code" header="Code" sortable style="width: 20%"></Column>
    <Column field="name" header="Name" sortable style="width: 20%"></Column>
    <Column field="price" header="Price" :sortable="true">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.price) }}
        </template>
    </Column>
    <Column field="category" header="Category" sortable style="width: 20%"></Column>
    <Column field="quantity" header="Quantity" sortable style="width: 20%"></Column>
</DataTable>


```

### Removable [#](https://primevue.org/datatable/#removable_sort)

When *removableSort* is present, the third click removes the sorting from the column.

```

<DataTable :value="products" removableSort tableStyle="min-width: 50rem">
    <Column field="code" header="Code" sortable style="width: 25%"></Column>
    <Column field="name" header="Name" sortable style="width: 25%"></Column>
    <Column field="category" header="Category" sortable style="width: 25%"></Column>
    <Column field="quantity" header="Quantity" sortable style="width: 25%"></Column>
</DataTable>


```

## Filter [#](https://primevue.org/datatable/#filter)

### Basic [#](https://primevue.org/datatable/#basic_filter)

Data filtering is enabled by defining the *filters* model referring to a *DataTableFilterMeta* instance and specifying a filter element for a column using the *filter* template. This template receives a *filterModel* and *filterCallback* to build your own UI.

The optional global filtering searches the data against a single value that is bound to the *global* key of the *filters* object. The fields to search against are defined with the *globalFilterFields*.

```

<DataTable v-model:filters="filters" :value="customers" paginator :rows="10" dataKey="id" filterDisplay="row" :loading="loading"
        :globalFilterFields="['name', 'country.name', 'representative.name', 'status']">
    <template #header>
        <div class="flex justify-end">
            <IconField>
                <InputIcon>
                    <i class="pi pi-search" />
                </InputIcon>
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
            </IconField>
        </div>
    </template>
    <template #empty> No customers found. </template>
    <template #loading> Loading customers data. Please wait. </template>
    <Column field="name" header="Name" style="min-width: 12rem">
        <template #body="{ data }">
            {{ data.name }}
        </template>
        <template #filter="{ filterModel, filterCallback }">
            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by name" />
        </template>
    </Column>
    <Column header="Country" filterField="country.name" style="min-width: 12rem">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${data.country.code}`" style="width: 24px" />
                <span>{{ data.country.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel, filterCallback }">
            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by country" />
        </template>
    </Column>
    <Column header="Agent" filterField="representative" :showFilterMenu="false" style="min-width: 14rem">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img :alt="data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${data.representative.image}`" style="width: 32px" />
                <span>{{ data.representative.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel, filterCallback }">
            <MultiSelect v-model="filterModel.value" @change="filterCallback()" :options="representatives" optionLabel="name" placeholder="Any" style="min-width: 14rem" :maxSelectedLabels="1">
                <template #option="slotProps">
                    <div class="flex items-center gap-2">
                        <img :alt="slotProps.option.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.option.image}`" style="width: 32px" />
                        <span>{{ slotProps.option.name }}</span>
                    </div>
                </template>
            </MultiSelect>
        </template>
    </Column>
    <Column field="status" header="Status" :showFilterMenu="false" style="min-width: 12rem">
        <template #body="{ data }">
            <Tag :value="data.status" :severity="getSeverity(data.status)" />
        </template>
        <template #filter="{ filterModel, filterCallback }">
            <Select v-model="filterModel.value" @change="filterCallback()" :options="statuses" placeholder="Select One" style="min-width: 12rem" :showClear="true">
                <template #option="slotProps">
                    <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
                </template>
            </Select>
        </template>
    </Column>
    <Column field="verified" header="Verified" dataType="boolean" style="min-width: 6rem">
        <template #body="{ data }">
            <i class="pi" :class="{ 'pi-check-circle text-green-500': data.verified, 'pi-times-circle text-red-400': !data.verified }"></i>
        </template>
        <template #filter="{ filterModel, filterCallback }">
            <Checkbox v-model="filterModel.value" :indeterminate="filterModel.value === null" binary @change="filterCallback()" />
        </template>
    </Column>
</DataTable>


```

### Advanced [#](https://primevue.org/datatable/#advanced_filter)

When *filterDisplay* is set as *menu*, filtering UI is placed inside a popover with support for multiple constraints and advanced templating.

```

<DataTable v-model:filters="filters" :value="customers" paginator showGridlines :rows="10" dataKey="id"
        filterDisplay="menu" :loading="loading" :globalFilterFields="['name', 'country.name', 'representative.name', 'balance', 'status']">
    <template #header>
        <div class="flex justify-between">
            <Button type="button" icon="pi pi-filter-slash" label="Clear" variant="outlined" @click="clearFilter()" />
            <IconField>
                <InputIcon>
                    <i class="pi pi-search" />
                </InputIcon>
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
            </IconField>
        </div>
    </template>
    <template #empty> No customers found. </template>
    <template #loading> Loading customers data. Please wait. </template>
    <Column field="name" header="Name" style="min-width: 12rem">
        <template #body="{ data }">
            {{ data.name }}
        </template>
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by name" />
        </template>
    </Column>
    <Column header="Country" filterField="country.name" style="min-width: 12rem">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${data.country.code}`" style="width: 24px" />
                <span>{{ data.country.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by country" />
        </template>
        <template #filterclear="{ filterCallback }">
            <Button type="button" icon="pi pi-times" @click="filterCallback()" severity="secondary"></Button>
        </template>
        <template #filterapply="{ filterCallback }">
            <Button type="button" icon="pi pi-check" @click="filterCallback()" severity="success"></Button>
        </template>
        <template #filterfooter>
            <div class="px-4 pt-0 pb-4 text-center">Customized Buttons</div>
        </template>
    </Column>
    <Column header="Agent" filterField="representative" :showFilterMatchModes="false" :filterMenuStyle="{ width: '14rem' }" style="min-width: 14rem">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img :alt="data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${data.representative.image}`" style="width: 32px" />
                <span>{{ data.representative.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <MultiSelect v-model="filterModel.value" :options="representatives" optionLabel="name" placeholder="Any">
                <template #option="slotProps">
                    <div class="flex items-center gap-2">
                        <img :alt="slotProps.option.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.option.image}`" style="width: 32px" />
                        <span>{{ slotProps.option.name }}</span>
                    </div>
                </template>
            </MultiSelect>
        </template>
    </Column>
    <Column header="Date" filterField="date" dataType="date" style="min-width: 10rem">
        <template #body="{ data }">
            {{ formatDate(data.date) }}
        </template>
        <template #filter="{ filterModel }">
            <DatePicker v-model="filterModel.value" dateFormat="mm/dd/yy" placeholder="mm/dd/yyyy" />
        </template>
    </Column>
    <Column header="Balance" filterField="balance" dataType="numeric" style="min-width: 10rem">
        <template #body="{ data }">
            {{ formatCurrency(data.balance) }}
        </template>
        <template #filter="{ filterModel }">
            <InputNumber v-model="filterModel.value" mode="currency" currency="USD" locale="en-US" />
        </template>
    </Column>
    <Column header="Status" field="status" :filterMenuStyle="{ width: '14rem' }" style="min-width: 12rem">
        <template #body="{ data }">
            <Tag :value="data.status" :severity="getSeverity(data.status)" />
        </template>
        <template #filter="{ filterModel }">
            <Select v-model="filterModel.value" :options="statuses" placeholder="Select One" showClear>
                <template #option="slotProps">
                    <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
                </template>
            </Select>
        </template>
    </Column>
    <Column field="activity" header="Activity" :showFilterMatchModes="false" style="min-width: 12rem">
        <template #body="{ data }">
            <ProgressBar :value="data.activity" :showValue="false" style="height: 6px"></ProgressBar>
        </template>
        <template #filter="{ filterModel }">
            <Slider v-model="filterModel.value" range class="m-4"></Slider>
            <div class="flex items-center justify-between px-2">
                <span>{{ filterModel.value ? filterModel.value[0] : 0 }}</span>
                <span>{{ filterModel.value ? filterModel.value[1] : 100 }}</span>
            </div>
        </template>
    </Column>
    <Column field="verified" header="Verified" dataType="boolean" bodyClass="text-center" style="min-width: 8rem">
        <template #body="{ data }">
            <i class="pi" :class="{ 'pi-check-circle text-green-500 ': data.verified, 'pi-times-circle text-red-500': !data.verified }"></i>
        </template>
        <template #filter="{ filterModel }">
            <label for="verified-filter" class="font-bold"> Verified </label>
            <Checkbox v-model="filterModel.value" :indeterminate="filterModel.value === null" binary inputId="verified-filter" />
        </template>
    </Column>
</DataTable>


```

## Row Selection [#](https://primevue.org/datatable/#row_selection)

### Single [#](https://primevue.org/datatable/#single_row_selection)

Single row selection is enabled by defining *selectionMode* as *single* along with a value binding using *selection* property. When available, it is suggested to provide a unique identifier of a row with *dataKey* to optimize performance.

By default, metaKey press (e.g. *⌘*) is necessary to unselect a row however this can be configured with disabling the *metaKeySelection* property. In touch enabled devices this option has no effect and behavior is same as setting it to false.

```

<ToggleSwitch v-model="metaKey" inputId="input-metakey" />

<DataTable v-model:selection="selectedProduct" :value="products" selectionMode="single" :metaKeySelection="metaKey" dataKey="id" tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

### Multiple [#](https://primevue.org/datatable/#multiple_rows_selection)

More than one row is selectable by setting *selectionMode* to *multiple*. By default in multiple selection mode, metaKey press (e.g. *⌘*) is not necessary to add to existing selections. When the optional *metaKeySelection* is present, behavior is changed in a way that selecting a new row requires meta key to be present. Note that in touch enabled devices, DataTable always ignores metaKey.

```

<ToggleSwitch v-model="metaKey" inputId="input-metakey" />

<DataTable v-model:selection="selectedProducts" :value="products" selectionMode="multiple" :metaKeySelection="metaKey" dataKey="id" tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

### RadioButton [#](https://primevue.org/datatable/#radiobutton_row_selection)

Specifying *selectionMode* as *single* on a Column, displays a radio button inside that column for selection. By default, row clicks also trigger selection, set *selectionMode* of DataTable to *radiobutton* to only trigger selection using the radio buttons.

```

<DataTable v-model:selection="selectedProduct" :value="products" dataKey="id" tableStyle="min-width: 50rem">
    <Column selectionMode="single" headerStyle="width: 3rem"></Column>
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

### Checkbox [#](https://primevue.org/datatable/#checkbox_row_selection)

Specifying *selectionMode* as *multiple* on a Column, displays a checkbox inside that column for selection.

The header checkbox toggles the selection state of the whole dataset by default, when paginator is enabled you may add *selectAll* property and *select-all-change* event to only control the selection of visible rows.

```

<DataTable v-model:selection="selectedProducts" :value="products" dataKey="id" tableStyle="min-width: 50rem">
    <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

### Column [#](https://primevue.org/datatable/#column_row_selection)

Row selection with an element inside a column is implemented with templating.

```

<DataTable :value="products" tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
    <Column class="w-24 !text-end">
        <template #body="{ data }">
            <Button icon="pi pi-search" @click="selectRow(data)" severity="secondary" rounded></Button>
        </template>
    </Column>
</DataTable>


```

### Events [#](https://primevue.org/datatable/#row_selection_events)

DataTable provides *row-select* and *row-unselect* events to listen selection events.

```

<DataTable v-model:selection="selectedProduct" :value="products" selectionMode="single" dataKey="id" :metaKeySelection="false"
        @rowSelect="onRowSelect" @rowUnselect="onRowUnselect" tableStyle="min-width: 50rem">
    <Column selectionMode="single" headerStyle="width: 3rem"></Column>
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

## Row Expansion [#](https://primevue.org/datatable/#row_expansion)

Row expansion is controlled with *expandedRows* property. The column that has the expander element requires *expander* property to be enabled. Optional *rowExpand* and *rowCollapse* events are available as callbacks.

Expanded rows can either be an array of row data or when *dataKey* is present, an object whose keys are strings referring to the identifier of the row data and values are booleans to represent the expansion state e.g. *{'1004': true}*. The *dataKey* alternative is more performant for large amounts of data.

```

<DataTable v-model:expandedRows="expandedRows" :value="products" dataKey="id"
        @rowExpand="onRowExpand" @rowCollapse="onRowCollapse" tableStyle="min-width: 60rem">
    <template #header>
        <div class="flex flex-wrap justify-end gap-2">
            <Button variant="text" icon="pi pi-plus" label="Expand All" @click="expandAll" />
            <Button variant="text" icon="pi pi-minus" label="Collapse All" @click="collapseAll" />
        </div>
    </template>
    <Column expander style="width: 5rem" />
    <Column field="name" header="Name"></Column>
    <Column header="Image">
        <template #body="slotProps">
            <img :src="`https://primefaces.org/cdn/primevue/images/product/${slotProps.data.image}`" :alt="slotProps.data.image" class="shadow-lg" width="64" />
        </template>
    </Column>
    <Column field="price" header="Price">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.price) }}
        </template>
    </Column>
    <Column field="category" header="Category"></Column>
    <Column field="rating" header="Reviews">
        <template #body="slotProps">
            <Rating :modelValue="slotProps.data.rating" readonly />
        </template>
    </Column>
    <Column header="Status">
        <template #body="slotProps">
            <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data)" />
        </template>
    </Column>
    <template #expansion="slotProps">
        <div class="p-4">
            <h5>Orders for {{ slotProps.data.name }}</h5>
            <DataTable :value="slotProps.data.orders">
                <Column field="id" header="Id" sortable></Column>
                <Column field="customer" header="Customer" sortable></Column>
                <Column field="date" header="Date" sortable></Column>
                <Column field="amount" header="Amount" sortable>
                    <template #body="slotProps">
                        {{ formatCurrency(slotProps.data.amount) }}
                    </template>
                </Column>
                <Column field="status" header="Status" sortable>
                    <template #body="slotProps">
                        <Tag :value="slotProps.data.status.toLowerCase()" :severity="getOrderSeverity(slotProps.data)" />
                    </template>
                </Column>
                <Column headerStyle="width:4rem">
                    <template #body>
                        <Button icon="pi pi-search" />
                    </template>
                </Column>
            </DataTable>
        </div>
    </template>
</DataTable>


```

## Edit [#](https://primevue.org/datatable/#edit)

### Cell [#](https://primevue.org/datatable/#cell_edit)

Cell editing is enabled by setting *editMode* as *cell*, defining input elements with *editor* templating of a Column and implementing *cell-edit-complete* to update the state.

```

<DataTable :value="products" editMode="cell" @cell-edit-complete="onCellEditComplete"
    :pt="{
        table: { style: 'min-width: 50rem' },
        column: {
            bodycell: ({ state }) => ({
                class: [{ '!py-0': state['d_editing'] }]
            })
        }
    }"
>
    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" style="width: 25%">
        <template #body="{ data, field }">
            {{ field === 'price' ? formatCurrency(data[field]) : data[field] }}
        </template>
        <template #editor="{ data, field }">
            <template v-if="field !== 'price'">
                <InputText v-model="data[field]" autofocus fluid />
            </template>
            <template v-else>
                <InputNumber v-model="data[field]" mode="currency" currency="USD" locale="en-US" autofocus fluid />
            </template>
        </template>
    </Column>
</DataTable>


```

### Row [#](https://primevue.org/datatable/#row_edit)

Row editing is configured with setting *editMode* as *row* and defining *editingRows* with the v-model directive to hold the reference of the editing rows. Similarly with cell edit mode, defining input elements with *editor* slot of a Column and implementing *row-edit-save* are necessary to update the state. The column to control the editing state should have *editor* templating applied.

```

<DataTable v-model:editingRows="editingRows" :value="products" editMode="row" dataKey="id" @row-edit-save="onRowEditSave"
    :pt="{
        table: { style: 'min-width: 50rem' },
        column: {
            bodycell: ({ state }) => ({
                style:  state['d_editing']&&'padding-top: 0.75rem; padding-bottom: 0.75rem'
            })
        }
    }"
>
    <Column field="code" header="Code" style="width: 20%">
        <template #editor="{ data, field }">
            <InputText v-model="data[field]" />
        </template>
    </Column>
    <Column field="name" header="Name" style="width: 20%">
        <template #editor="{ data, field }">
            <InputText v-model="data[field]" fluid />
        </template>
    </Column>
    <Column field="inventoryStatus" header="Status" style="width: 20%">
        <template #editor="{ data, field }">
            <Select v-model="data[field]" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status" fluid>
                <template #option="slotProps">
                    <Tag :value="slotProps.option.value" :severity="getStatusLabel(slotProps.option.value)" />
                </template>
            </Select>
        </template>
        <template #body="slotProps">
            <Tag :value="slotProps.data.inventoryStatus" :severity="getStatusLabel(slotProps.data.inventoryStatus)" />
        </template>
    </Column>
    <Column field="price" header="Price" style="width: 20%">
        <template #body="{ data, field }">
            {{ formatCurrency(data[field]) }}
        </template>
        <template #editor="{ data, field }">
            <InputNumber v-model="data[field]" mode="currency" currency="USD" locale="en-US" fluid />
        </template>
    </Column>
    <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center"></Column>
</DataTable>


```

## Scroll [#](https://primevue.org/datatable/#scroll)

### Vertical [#](https://primevue.org/datatable/#vertical_scroll)

Adding *scrollable* property along with a *scrollHeight* for the data viewport enables vertical scrolling with fixed headers.

```

<DataTable :value="customers" scrollable scrollHeight="400px" tableStyle="min-width: 50rem">
    <Column field="name" header="Name"></Column>
    <Column field="country.name" header="Country"></Column>
    <Column field="representative.name" header="Representative"></Column>
    <Column field="company" header="Company"></Column>
</DataTable>


```

### Flexible [#](https://primevue.org/datatable/#flex_scroll)

Flex scroll feature makes the scrollable viewport section dynamic instead of a fixed value so that it can grow or shrink relative to the parent size of the table. Click the button below to display a maximizable Dialog where data viewport adjusts itself according to the size changes.

Show

```

<Button label="Show" icon="pi pi-external-link" @click="dialogVisible = true" />
<Dialog v-model:visible="dialogVisible" header="Flex Scroll" :style="{ width: '75vw' }" maximizable modal :contentStyle="{ height: '300px' }">
    <DataTable :value="customers" scrollable scrollHeight="flex" tableStyle="min-width: 50rem">
        <Column field="name" header="Name"></Column>
        <Column field="country.name" header="Country"></Column>
        <Column field="representative.name" header="Representative"></Column>
        <Column field="company" header="Company"></Column>
    </DataTable>
    <template #footer>
        <Button label="Ok" icon="pi pi-check" @click="dialogVisible = false" />
    </template>
</Dialog>


```

### Horizontal [#](https://primevue.org/datatable/#horizontal_scroll)

Horizontal scrollbar is displayed when table width exceeds the parent width.

```

<DataTable :value="customers" scrollable scrollHeight="400px">
    <Column field="id" header="Id" footer="Id" style="min-width: 100px"></Column>
    <Column field="name" header="Name" footer="Name" style="min-width: 200px"></Column>
    <Column field="country.name" header="Country" footer="Country" style="min-width: 200px"></Column>
    <Column field="date" header="Date" footer="Date" style="min-width: 200px"></Column>
    <Column field="balance" header="Balance" footer="Balance" style="min-width: 200px">
        <template #body="{ data }">
            {{ formatCurrency(data.balance) }}
        </template>
    </Column>
    <Column field="company" header="Company" footer="Company" style="min-width: 200px"></Column>
    <Column field="status" header="Status" footer="Status" style="min-width: 200px"></Column>
    <Column field="activity" header="Activity" footer="Activity" style="min-width: 200px"></Column>
    <Column field="representative.name" header="Representative" footer="Representative" style="min-width: 200px"></Column>
</DataTable>


```

### Frozen Rows [#](https://primevue.org/datatable/#frozen_rows)

Rows can be fixed during scrolling by enabling the *frozenValue* property.

```

<DataTable
    :value="customers"
    :frozenValue="lockedCustomers"
    scrollable
    scrollHeight="400px"
    :pt="{
        table: { style: 'min-width: 50rem' },
        bodyrow: ({ props }) => ({
            class: [{ 'font-bold': props.frozenRow }]
        })
    }"
>
    <Column field="name" header="Name"></Column>
    <Column field="country.name" header="Country"></Column>
    <Column field="representative.name" header="Representative"></Column>
    <Column field="status" header="Status"></Column>
    <Column style="flex: 0 0 4rem">
        <template #body="{ data, frozenRow, index }">
            <Button type="button" :icon="frozenRow ? 'pi pi-lock-open' : 'pi pi-lock'" :disabled="frozenRow ? false : lockedCustomers.length >= 2" text size="small" @click="toggleLock(data, frozenRow, index)" />
        </template>
    </Column>
</DataTable>


```

### Frozen Columns [#](https://primevue.org/datatable/#frozen_columns)

A column can be fixed during horizontal scrolling by enabling the *frozen* property. The location is defined with the *alignFrozen* that can be *left* or *right*.

```

<ToggleButton v-model="balanceFrozen" onIcon="pi pi-lock" offIcon="pi pi-lock-open" onLabel="Balance" offLabel="Balance" />
<DataTable :value="customers" scrollable scrollHeight="400px" class="mt-6">
    <Column field="name" header="Name" style="min-width: 200px" frozen class="font-bold"></Column>
    <Column field="id" header="Id" style="min-width: 100px"></Column>
    <Column field="name" header="Name" style="min-width: 200px"></Column>
    <Column field="country.name" header="Country" style="min-width: 200px"></Column>
    <Column field="date" header="Date" style="min-width: 200px"></Column>
    <Column field="company" header="Company" style="min-width: 200px"></Column>
    <Column field="status" header="Status" style="min-width: 200px"></Column>
    <Column field="activity" header="Activity" style="min-width: 200px"></Column>
    <Column field="representative.name" header="Representative" style="min-width: 200px"></Column>
    <Column field="balance" header="Balance" style="min-width: 200px" alignFrozen="right" :frozen="balanceFrozen">
        <template #body="{ data }">
            <span class="font-bold">{{ formatCurrency(data.balance) }}</span>
        </template>
    </Column>
</DataTable>


```

## Virtual Scroll [#](https://primevue.org/datatable/#virtualscroll)

### Preload [#](https://primevue.org/datatable/#preload_virtualscroll)

Virtual Scrolling is an efficient way to render large amount data. Usage is similar to regular scrolling with the addition of *virtualScrollerOptions* property to define a fixed *itemSize*. Internally, [VirtualScroller](https://primevue.org/virtualscroller/) component is utilized so refer to the API of VirtualScroller for more information about the available options.

In this example, **100000** preloaded records are rendered by the Table.

```

<DataTable :value="cars" scrollable scrollHeight="400px" :virtualScrollerOptions="{ itemSize: 44 }" tableStyle="min-width: 50rem">
    <Column field="id" header="Id" style="width: 20%; height: 44px"></Column>
    <Column field="vin" header="Vin" style="width: 20%; height: 44px"></Column>
    <Column field="year" header="Year" style="width: 20%; height: 44px"></Column>
    <Column field="brand" header="Brand" style="width: 20%; height: 44px"></Column>
    <Column field="color" header="Color" style="width: 20%; height: 44px"></Column>
</DataTable>


```

### Lazy [#](https://primevue.org/datatable/#lazy_virtualscroll)

When lazy loading is enabled via the *virtualScrollerOptions*, data is fetched on demand during scrolling instead of preload.

In sample below, an in-memory list and timeout is used to mimic fetching from a remote datasource. The *virtualCars* is an empty array that is populated on scroll.

```

<DataTable :value="virtualCars" scrollable scrollHeight="400px" tableStyle="min-width: 50rem"
        :virtualScrollerOptions="{ lazy: true, onLazyLoad: loadCarsLazy, itemSize: 44, delay: 200, showLoader: true, loading: lazyLoading, numToleratedItems: 10 }">
    <Column field="id" header="Id" style="width: 20%; height: 44px">
        <template #loading>
            <div class="flex items-center" :style="{ height: '17px', 'flex-grow': '1', overflow: 'hidden' }">
                <Skeleton width="60%" height="1rem" />
            </div>
        </template>
    </Column>
    <Column field="vin" header="Vin" style="width: 20%; height: 44px">
        <template #loading>
            <div class="flex items-center" :style="{ height: '17px', 'flex-grow': '1', overflow: 'hidden' }">
                <Skeleton width="40%" height="1rem" />
            </div>
        </template>
    </Column>
    <Column field="year" header="Year" style="width: 20%; height: 44px">
        <template #loading>
            <div class="flex items-center" :style="{ height: '17px', 'flex-grow': '1', overflow: 'hidden' }">
                <Skeleton width="30%" height="1rem" />
            </div>
        </template>
    </Column>
    <Column field="brand" header="Brand" style="width: 20%; height: 44px">
        <template #loading>
            <div class="flex items-center" :style="{ height: '17px', 'flex-grow': '1', overflow: 'hidden' }">
                <Skeleton width="40%" height="1rem" />
            </div>
        </template>
    </Column>
    <Column field="color" header="Color" style="width: 20%; height: 44px">
        <template #loading>
            <div class="flex items-center" :style="{ height: '17px', 'flex-grow': '1', overflow: 'hidden' }">
                <Skeleton width="60%" height="1rem" />
            </div>
        </template>
    </Column>
</DataTable>


```

## Column Group [#](https://primevue.org/datatable/#column_group)

Columns can be grouped within a *Row* component and groups can be displayed within a ColumnGroup component. These groups can be displayed using *type* property that can be *header* or *footer*. Number of cells and rows to span are defined with the *colspan* and *rowspan* properties of a Column.

```

<DataTable :value="sales" tableStyle="min-width: 50rem">
    <ColumnGroup type="header">
        <Row>
            <Column header="Product" :rowspan="3" />
            <Column header="Sale Rate" :colspan="4" />
        </Row>
        <Row>
            <Column header="Sales" :colspan="2" />
            <Column header="Profits" :colspan="2" />
        </Row>
        <Row>
            <Column header="Last Year" sortable field="lastYearSale" />
            <Column header="This Year" sortable field="thisYearSale" />
            <Column header="Last Year" sortable field="lastYearProfit" />
            <Column header="This Year" sortable field="thisYearProfit" />
        </Row>
    </ColumnGroup>
    <Column field="product" />
    <Column field="lastYearSale">
        <template #body="slotProps"> {{ slotProps.data.lastYearSale }}% </template>
    </Column>
    <Column field="thisYearSale">
        <template #body="slotProps"> {{ slotProps.data.thisYearSale }}% </template>
    </Column>
    <Column field="lastYearProfit">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.lastYearProfit) }}
        </template>
    </Column>
    <Column field="thisYearProfit">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.thisYearProfit) }}
        </template>
    </Column>
    <ColumnGroup type="footer">
        <Row>
            <Column footer="Totals:" :colspan="3" footerStyle="text-align:right" />
            <Column :footer="lastYearTotal" />
            <Column :footer="thisYearTotal" />
        </Row>
    </ColumnGroup>
</DataTable>


```

## Row Group [#](https://primevue.org/datatable/#row_group)

### Subheader [#](https://primevue.org/datatable/#rowgroup_subheader)

Rows are grouped with the *groupRowsBy* property. When *rowGroupMode* is set as *subheader*, a header and footer can be displayed for each group. The content of a group header is provided with *groupheader* and footer with *groupfooter* slots.

```

<DataTable :value="customers" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single"
        sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px" tableStyle="min-width: 50rem">
    <Column field="representative.name" header="Representative"></Column>
    <Column field="name" header="Name" style="min-width: 200px"></Column>
    <Column field="country" header="Country" style="min-width: 200px">
        <template #body="slotProps">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.data.country.code}`" style="width: 24px" />
                <span>{{ slotProps.data.country.name }}</span>
            </div>
        </template>
    </Column>
    <Column field="company" header="Company" style="min-width: 200px"></Column>
    <Column field="status" header="Status" style="min-width: 200px">
        <template #body="slotProps">
            <Tag :value="slotProps.data.status" :severity="getSeverity(slotProps.data.status)" />
        </template>
    </Column>
    <Column field="date" header="Date" style="min-width: 200px"></Column>
    <template #groupheader="slotProps">
        <div class="flex items-center gap-2">
            <img :alt="slotProps.data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.data.representative.image}`" width="32" style="vertical-align: middle" />
            <span>{{ slotProps.data.representative.name }}</span>
        </div>
    </template>
    <template #groupfooter="slotProps">
        <div class="flex justify-end font-bold w-full">Total Customers: {{ calculateCustomerTotal(slotProps.data.representative.name) }}</div>
    </template>
</DataTable>


```

### Expandable [#](https://primevue.org/datatable/#rowgroup_expandable)

When *expandableRowGroups* is present in subheader based row grouping, groups can be expanded and collapsed. State of the expansions are controlled using the *expandedRows* property and *rowgroup-expand* and *rowgroup-collapse* events.

```

<DataTable v-model:expandedRowGroups="expandedRowGroups" :value="customers" tableStyle="min-width: 50rem"
        expandableRowGroups rowGroupMode="subheader" groupRowsBy="representative.name" @rowgroup-expand="onRowGroupExpand" @rowgroup-collapse="onRowGroupCollapse"
        sortMode="single" sortField="representative.name" :sortOrder="1">
    <template #groupheader="slotProps">
        <img :alt="slotProps.data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.data.representative.image}`" width="32" style="vertical-align: middle; display: inline-block" class="ml-2" />
        <span class="align-middle ml-2 font-bold leading-normal">{{ slotProps.data.representative.name }}</span>
    </template>
    <Column field="representative.name" header="Representative"></Column>
    <Column field="name" header="Name" style="width: 20%"></Column>
    <Column field="country" header="Country" style="width: 20%">
        <template #body="slotProps">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.data.country.code}`" style="width: 24px" />
                <span>{{ slotProps.data.country.name }}</span>
            </div>
        </template>
    </Column>
    <Column field="company" header="Company" style="width: 20%"></Column>
    <Column field="status" header="Status" style="width: 20%">
        <template #body="slotProps">
            <Tag :value="slotProps.data.status" :severity="getSeverity(slotProps.data.status)" />
        </template>
    </Column>
    <Column field="date" header="Date" style="width: 20%"></Column>
    <template #groupfooter="slotProps">
        <div class="flex justify-end font-bold w-full">Total Customers: {{ calculateCustomerTotal(slotProps.data.representative.name) }}</div>
    </template>
</DataTable>


```

### RowSpan [#](https://primevue.org/datatable/#rowgroup_rowspan)

When *rowGroupMode* is configured to be *rowspan*, the grouping column spans multiple rows.

```

<DataTable :value="customers" rowGroupMode="rowspan" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" tableStyle="min-width: 50rem">
    <Column header="#" headerStyle="width:3rem">
        <template #body="slotProps">
            {{ slotProps.index + 1 }}
        </template>
    </Column>
    <Column field="representative.name" header="Representative" style="min-width: 200px">
        <template #body="slotProps">
            <div class="flex items-center gap-2">
                <img :alt="slotProps.data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.data.representative.image}`" width="32" style="vertical-align: middle" />
                <span>{{ slotProps.data.representative.name }}</span>
            </div>
        </template>
    </Column>
    <Column field="name" header="Name" style="min-width: 200px"></Column>
    <Column field="country" header="Country" style="min-width: 150px">
        <template #body="slotProps">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.data.country.code}`" style="width: 24px" />
                <span>{{ slotProps.data.country.name }}</span>
            </div>
        </template>
    </Column>
    <Column field="company" header="Company" style="min-width: 200px"></Column>
    <Column field="status" header="Status" style="min-width: 100px">
        <template #body="slotProps">
            <Tag :value="slotProps.data.status" :severity="getSeverity(slotProps.data.status)" />
        </template>
    </Column>
</DataTable>


```

## Conditional Style [#](https://primevue.org/datatable/#conditional_style)

Particular rows and cells can be styled based on conditions. The *rowClass* receives a row data as a parameter to return a style class for a row whereas cells are customized using the *body* template.

```

<DataTable :value="products" :rowClass="rowClass" :rowStyle="rowStyle" tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity">
        <template #body="slotProps">
            <Badge :value="slotProps.data.quantity" :severity="stockSeverity(slotProps.data)" />
        </template>
    </Column>
</DataTable>


```

## Column Resize [#](https://primevue.org/datatable/#column_resize)

### Fit Mode [#](https://primevue.org/datatable/#resize_fitmode)

Columns can be resized with drag and drop when *resizableColumns* is enabled. Default resize mode is *fit* that does not change the overall table width.

```

<DataTable :value="products" resizableColumns columnResizeMode="fit" showGridlines tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

### Expand Mode [#](https://primevue.org/datatable/#resize_expandmode)

Setting *columnResizeMode* as *expand* changes the table width as well.

```

<DataTable :value="products" resizableColumns columnResizeMode="expand" showGridlines tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

## Reorder [#](https://primevue.org/datatable/#reorder)

Order of the columns and rows can be changed using drag and drop. Column reordering is configured by adding *reorderableColumns* property.

Similarly, adding *rowReorder* property to a column enables draggable rows. For the drag handle a column needs to have *rowReorder* property and table needs to have *row-reorder* event is required to control the state of the rows after reorder completes.

```

<DataTable :value="products" :reorderableColumns="true" @columnReorder="onColReorder" @rowReorder="onRowReorder" tableStyle="min-width: 50rem">
    <Column rowReorder headerStyle="width: 3rem" :reorderableColumn="false" />
    <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field"></Column>
</DataTable>


```

## Column Toggle [#](https://primevue.org/datatable/#column_toggle)

Column visibility based on a condition can be implemented with dynamic columns, in this sample a MultiSelect is used to manage the visible columns.

```

<DataTable :value="products" tableStyle="min-width: 50rem">
    <template #header>
        <div style="text-align:left">
            <MultiSelect :modelValue="selectedColumns" :options="columns" optionLabel="header" @update:modelValue="onToggle"
                display="chip" placeholder="Select Columns" />
        </div>
    </template>
    <Column field="code" header="Code" />
    <Column v-for="(col, index) of selectedColumns" :field="col.field" :header="col.header" :key="col.field + '_' + index"></Column>
</DataTable>


```

## Export [#](https://primevue.org/datatable/#export)

DataTable can export its data to CSV format.

```

<DataTable :value="products" ref="dt" tableStyle="min-width: 50rem">
    <template #header>
        <div class="text-end pb-4">
            <Button icon="pi pi-external-link" label="Export" @click="exportCSV($event)" />
        </div>
    </template>
    <Column field="code" header="Code" exportHeader="Product Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="quantity" header="Quantity"></Column>
</DataTable>


```

## Context Menu [#](https://primevue.org/datatable/#contextmenu)

DataTable has exclusive integration with ContextMenu using the *contextMenu* event to open a menu on right click along with *contextMenuSelection* property and *row-contextmenu* event to control the selection via the menu.

```

<ContextMenu ref="cm" :model="menuModel" @hide="selectedProduct = null" />
<DataTable v-model:contextMenuSelection="selectedProduct" :value="products" contextMenu
        @row-contextmenu="onRowContextMenu" tableStyle="min-width: 50rem">
    <Column field="code" header="Code"></Column>
    <Column field="name" header="Name"></Column>
    <Column field="category" header="Category"></Column>
    <Column field="price" header="Price">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.price) }}
        </template>
    </Column>
</DataTable>


```

## Stateful [#](https://primevue.org/datatable/#stateful)

Stateful table allows keeping the state such as page, sort and filtering either at local storage or session storage so that when the page is visited again, table would render the data using the last settings.

Change the state of the table e.g paginate, navigate away and then return to this table again to test this feature, the setting is set as *session* with the *stateStorage* property so that Table retains the state until the browser is closed. Other alternative is *local* referring to *localStorage* for an extended lifetime.

```

<DataTable v-model:filters="filters" v-model:selection="selectedCustomer" :value="customers"
    stateStorage="session" stateKey="dt-state-demo-session" paginator :rows="5" filterDisplay="menu"
    selectionMode="single" dataKey="id" :globalFilterFields="['name', 'country.name', 'representative.name', 'status']" tableStyle="min-width: 50rem">
    <template #header>
        <IconField>
            <InputIcon>
                <i class="pi pi-search" />
            </InputIcon>
            <InputText v-model="filters['global'].value" placeholder="Global Search" />
        </IconField>
    </template>
    <Column field="name" header="Name" sortable style="width: 25%">
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by name" />
        </template>
    </Column>
    <Column header="Country" sortable sortField="country.name" filterField="country.name" filterMatchMode="contains" style="width: 25%">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${data.country.code}`" style="width: 24px" />
                <span>{{ data.country.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by country" />
        </template>
    </Column>
    <Column header="Representative" sortable sortField="representative.name" filterField="representative" :showFilterMatchModes="false" :filterMenuStyle="{ width: '14rem' }" style="width: 25%">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img :alt="data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${data.representative.image}`" style="width: 32px" />
                <span>{{ data.representative.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <MultiSelect v-model="filterModel.value" :options="representatives" optionLabel="name" placeholder="Any">
                <template #option="slotProps">
                    <div class="flex items-center gap-2">
                        <img :alt="slotProps.option.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.option.image}`" style="width: 32px" />
                        <span>{{ slotProps.option.name }}</span>
                    </div>
                </template>
            </MultiSelect>
        </template>
    </Column>
    <Column field="status" header="Status" sortable filterMatchMode="equals" style="width: 25%">
        <template #body="{ data }">
            <Tag :value="data.status" :severity="getSeverity(data.status)" />
        </template>
        <template #filter="{ filterModel }">
            <Select v-model="filterModel.value" :options="statuses" placeholder="Select One" showClear>
                <template #option="slotProps">
                    <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
                </template>
            </Select>
        </template>
    </Column>
    <template #empty> No customers found. </template>
</DataTable>


```

## Samples [#](https://primevue.org/datatable/#samples)

### Customers [#](https://primevue.org/datatable/#customers)

DataTable with selection, pagination, filtering, sorting and templating.

```

<DataTable v-model:filters="filters" v-model:selection="selectedCustomers" :value="customers" paginator :rows="10" dataKey="id" filterDisplay="menu"
    :globalFilterFields="['name', 'country.name', 'representative.name', 'balance', 'status']">
    <template #header>
        <div class="flex justify-between">
            <Button type="button" icon="pi pi-filter-slash" label="Clear" variant="outlined" @click="clearFilter()" />
            <IconField>
                <InputIcon>
                    <i class="pi pi-search" />
                </InputIcon>
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
            </IconField>
        </div>
    </template>
    <template #empty> No customers found. </template>
    <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>
    <Column field="name" header="Name" sortable style="min-width: 14rem">
        <template #body="{ data }">
            {{ data.name }}
        </template>
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by name" />
        </template>
    </Column>
    <Column header="Country" sortable sortField="country.name" filterField="country.name" style="min-width: 14rem">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${data.country.code}`" style="width: 24px" />
                <span>{{ data.country.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by country" />
        </template>
    </Column>
    <Column header="Agent" sortable sortField="representative.name" filterField="representative" :showFilterMatchModes="false" :filterMenuStyle="{ width: '14rem' }" style="min-width: 14rem">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img :alt="data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${data.representative.image}`" style="width: 32px" />
                <span>{{ data.representative.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <MultiSelect v-model="filterModel.value" :options="representatives" optionLabel="name" placeholder="Any">
                <template #option="slotProps">
                    <div class="flex items-center gap-2">
                        <img :alt="slotProps.option.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.option.image}`" style="width: 32px" />
                        <span>{{ slotProps.option.name }}</span>
                    </div>
                </template>
            </MultiSelect>
        </template>
    </Column>
    <Column field="date" header="Date" sortable filterField="date" dataType="date" style="min-width: 10rem">
        <template #body="{ data }">
            {{ formatDate(data.date) }}
        </template>
        <template #filter="{ filterModel }">
            <DatePicker v-model="filterModel.value" dateFormat="mm/dd/yy" placeholder="mm/dd/yyyy" />
        </template>
    </Column>
    <Column field="balance" header="Balance" sortable filterField="balance" dataType="numeric" style="min-width: 10rem">
        <template #body="{ data }">
            {{ formatCurrency(data.balance) }}
        </template>
        <template #filter="{ filterModel }">
            <InputNumber v-model="filterModel.value" mode="currency" currency="USD" locale="en-US" />
        </template>
    </Column>
    <Column header="Status" field="status" sortable :filterMenuStyle="{ width: '14rem' }" style="min-width: 12rem">
        <template #body="{ data }">
            <Tag :value="data.status" :severity="getSeverity(data.status)" />
        </template>
        <template #filter="{ filterModel }">
            <Select v-model="filterModel.value" :options="statuses" placeholder="Select One" showClear>
                <template #option="slotProps">
                    <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
                </template>
            </Select>
        </template>
    </Column>
    <Column field="activity" header="Activity" sortable :showFilterMatchModes="false" style="min-width: 12rem">
        <template #body="{ data }">
            <ProgressBar :value="data.activity" :showValue="false" style="height: 6px"></ProgressBar>
        </template>
        <template #filter="{ filterModel }">
            <Slider v-model="filterModel.value" range class="m-4"></Slider>
            <div class="flex items-center justify-between px-2">
                <span>{{ filterModel.value ? filterModel.value[0] : 0 }}</span>
                <span>{{ filterModel.value ? filterModel.value[1] : 100 }}</span>
            </div>
        </template>
    </Column>
    <Column headerStyle="width: 5rem; text-align: center" bodyStyle="text-align: center; overflow: visible">
        <template #body>
            <Button type="button" icon="pi pi-cog" rounded />
        </template>
    </Column>
</DataTable>


```

### Products [#](https://primevue.org/datatable/#dtproducts)

CRUD implementation example with a Dialog.

```

<Toolbar class="mb-6">
    <template #start>
        <Button label="New" icon="pi pi-plus" class="mr-2" @click="openNew" />
        <Button label="Delete" icon="pi pi-trash" severity="danger" variant="outlined" @click="confirmDeleteSelected" :disabled="!selectedProducts || !selectedProducts.length" />
    </template>

    <template #end>
        <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" customUpload chooseLabel="Import" class="mr-2" auto :chooseButtonProps="{ severity: 'secondary' }" />
        <Button label="Export" icon="pi pi-upload" severity="secondary" @click="exportCSV($event)" />
    </template>
</Toolbar>

<DataTable
    ref="dt"
    v-model:selection="selectedProducts"
    :value="products"
    dataKey="id"
    :paginator="true"
    :rows="10"
    :filters="filters"
    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
    :rowsPerPageOptions="[5, 10, 25]"
    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
>
    <template #header>
        <div class="flex flex-wrap gap-2 items-center justify-between">
            <h4 class="m-0">Manage Products</h4>
            <IconField>
                <InputIcon>
                    <i class="pi pi-search" />
                </InputIcon>
                <InputText v-model="filters['global'].value" placeholder="Search..." />
            </IconField>
        </div>
    </template>

    <Column selectionMode="multiple" style="width: 3rem" :exportable="false"></Column>
    <Column field="code" header="Code" sortable style="min-width: 12rem"></Column>
    <Column field="name" header="Name" sortable style="min-width: 16rem"></Column>
    <Column header="Image">
        <template #body="slotProps">
            <img :src="`https://primefaces.org/cdn/primevue/images/product/${slotProps.data.image}`" :alt="slotProps.data.image" class="rounded" style="width: 64px" />
        </template>
    </Column>
    <Column field="price" header="Price" sortable style="min-width: 8rem">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.price) }}
        </template>
    </Column>
    <Column field="category" header="Category" sortable style="min-width: 10rem"></Column>
    <Column field="rating" header="Reviews" sortable style="min-width: 12rem">
        <template #body="slotProps">
            <Rating :modelValue="slotProps.data.rating" :readonly="true" />
        </template>
    </Column>
    <Column field="inventoryStatus" header="Status" sortable style="min-width: 12rem">
        <template #body="slotProps">
            <Tag :value="slotProps.data.inventoryStatus" :severity="getStatusLabel(slotProps.data.inventoryStatus)" />
        </template>
    </Column>
    <Column :exportable="false" style="min-width: 12rem">
        <template #body="slotProps">
            <Button icon="pi pi-pencil" variant="outlined" rounded class="mr-2" @click="editProduct(slotProps.data)" />
            <Button icon="pi pi-trash" variant="outlined" rounded severity="danger" @click="confirmDeleteProduct(slotProps.data)" />
        </template>
    </Column>
</DataTable>


```

## Accessibility [#](https://primevue.org/datatable/#accessibility)

### Screen Reader

DataTable uses a *table* element whose attributes can be extended with the *tableProps* option. This property allows passing aria roles and attributes like *aria-label* and *aria-describedby* to define the table for readers. Default role of the table is *table*. Header, body and footer elements use *rowgroup*, rows use *row* role, header cells have *columnheader* and body cells use *cell* roles. Sortable headers utilizer *aria-sort* attribute either set to "ascending" or "descending".

Built-in checkbox and radiobutton components for row selection use *checkbox* and *radiobutton*. The label to describe them is retrieved from the *aria.selectRow* and *aria.unselectRow* properties of the [locale](https://primevue.org/configuration/#locale) API. Similarly header checkbox uses *selectAll* and *unselectAll* keys. When a row is selected, *aria-selected* is set to true on a row.

The element to expand or collapse a row is a *button* with *aria-expanded* and *aria-controls* properties. Value to describe the buttons is derived from *aria.expandRow* and *aria.collapseRow* properties of the [locale](https://primevue.org/configuration/#locale) API.

The filter menu button use *aria.showFilterMenu* and *aria.hideFilterMenu* properties as *aria-label* in addition to the *aria-haspopup*, *aria-expanded* and *aria-controls* to define the relation between the button and the overlay. Popop menu has *dialog* role with *aria-modal* as focus is kept within the overlay. The operator dropdown use *aria.filterOperator* and filter constraints dropdown use *aria.filterConstraint* properties. Buttons to add rules on the other hand utilize *aria.addRule* and *aria.removeRule* properties. The footer buttons similarly use *aria.clear* and *aria.apply* properties. *filterInputProps* of the Column component can be used to define aria labels for the built-in filter components, if a custom component is used with templating you also may define your own aria labels as well.

Editable cells use custom templating so you need to manage aria roles and attributes manually if required. The row editor controls are button elements with *aria.editRow*, *aria.cancelEdit* and *aria.saveEdit* used for the *aria-label*.

Paginator is a standalone component used inside the DataTable, refer to the [paginator](https://primevue.org/paginator/) for more information about the accessibility features.

### Keyboard Support

Any button element inside the DataTable used for cases like filter, row expansion, edit are tabbable and can be used with *space* and *enter* keys.

### Sortable Headers Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves through the headers. |
| *enter* | Sorts the column. |
| *space* | Sorts the column. |

### Filter Menu Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves through the elements inside the popup. |
| *escape* | Hides the popup. |

### Selection Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the first selected row, if there is none then first row receives the focus. |
| *up arrow* | Moves focus to the previous row. |
| *down arrow* | Moves focus to the next row. |
| *enter* | Toggles the selected state of the focused row depending on the metaKeySelection setting. |
| *space* | Toggles the selected state of the focused row depending on the metaKeySelection setting. |
| *home* | Moves focus to the first row. |
| *end* | Moves focus to the last row. |
| *shift* + *down arrow* | Moves focus to the next row and toggles the selection state. |
| *shift* + *up arrow* | Moves focus to the previous row and toggles the selection state. |
| *shift* + *space* | Selects the rows between the most recently selected row and the focused row. |
| *control* + *shift* + *home* | Selects the focused rows and all the options up to the first one. |
| *control* + *shift* + *end* | Selects the focused rows and all the options down to the last one. |
| *control* + *a* | Selects all rows. |