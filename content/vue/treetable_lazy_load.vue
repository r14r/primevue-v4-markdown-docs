<TreeTable :value="nodes" :lazy="true" :paginator="true" :rows="rows" :loading="loading"
    @nodeExpand="onExpand" @page="onPage" :totalRecords="totalRecords" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander></Column>
    <Column field="size" header="Size"></Column>
    <Column field="type" header="Type"></Column>
</TreeTable>