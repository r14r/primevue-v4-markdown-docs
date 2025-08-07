<TreeTable :value="nodes" :size="size.value" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>