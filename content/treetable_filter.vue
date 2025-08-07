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