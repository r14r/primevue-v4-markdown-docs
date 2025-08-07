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