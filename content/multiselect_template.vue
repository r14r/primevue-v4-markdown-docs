<MultiSelect v-model="selectedCountries" :options="countries" optionLabel="name" filter placeholder="Select Countries" display="chip" class="w-full md:w-80">
    <template #option="slotProps">
        <div class="flex items-center">
            <img :alt="slotProps.option.name" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ slotProps.option.name }}</div>
        </div>
    </template>
    <template #dropdownicon>
        <i class="pi pi-map" />
    </template>
    <template #filtericon>
        <i class="pi pi-map-marker" />
    </template>
    <template #header>
        <div class="font-medium px-3 py-2">Available Countries</div>
    </template>
    <template #footer>
        <div class="p-3 flex justify-between">
            <Button label="Add New" severity="secondary" variant="text" size="small" icon="pi pi-plus" />
            <Button label="Remove All" severity="danger" variant="text" size="small" icon="pi pi-times" />
        </div>
    </template>
</MultiSelect>