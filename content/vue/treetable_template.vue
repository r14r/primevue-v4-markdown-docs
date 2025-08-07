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