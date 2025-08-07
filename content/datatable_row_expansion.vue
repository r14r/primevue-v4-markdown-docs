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