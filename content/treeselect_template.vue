<TreeSelect v-model="selectedValue" :options="nodes" placeholder="Select Item" class="md:w-80 w-full">
    <template #dropdownicon>
        <i class="pi pi-search" />
    </template>
    <template #header>
        <div class="font-medium px-3 py-2">Available Files</div>
    </template>
    <template #footer>
        <div class="px-3 pt-1 pb-2 flex justify-between">
            <Button label="Add New" severity="secondary" text size="small" icon="pi pi-plus" />
            <Button label="Remove All" severity="danger" text size="small" icon="pi pi-plus" />
        </div>
    </template>
</TreeSelect>