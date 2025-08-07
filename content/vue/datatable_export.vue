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