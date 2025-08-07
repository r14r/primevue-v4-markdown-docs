<ContextMenu ref="cm" :model="menuModel" @hide="selectedNode = null" />
<TreeTable v-model:contextMenuSelection="selectedNode" :value="nodes" contextMenu @row-contextmenu="onRowContextMenu" tableStyle="min-width: 50rem">
    <Column field="name" header="Name" expander style="width: 34%"></Column>
    <Column field="size" header="Size" style="width: 33%"></Column>
    <Column field="type" header="Type" style="width: 33%"></Column>
</TreeTable>