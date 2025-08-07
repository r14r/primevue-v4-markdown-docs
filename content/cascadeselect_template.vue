<CascadeSelect v-model="selectedCity" :options="countries" optionLabel="cname" optionGroupLabel="name"
    :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City">
    <template #option="slotProps">
        <div class="flex items-center">
            <img v-if="slotProps.option.states" :alt="slotProps.option.name" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px"  />
            <i v-if="slotProps.option.cities" class="pi pi-compass mr-2"></i>
            <i v-if="slotProps.option.cname" class="pi pi-map-marker mr-2"></i>
            <span>{{ slotProps.option.cname || slotProps.option.name }}</span>
        </div>
    </template>
    <template #dropdownicon>
        <i class="pi pi-map" />
    </template>
    <template #header>
        <div class="font-medium px-3 py-2">Available Countries</div>
    </template>
    <template #footer>
        <div class="px-3 py-1">
            <Button label="Add New" fluid severity="secondary" variant="text" size="small" icon="pi pi-plus" />
        </div>
    </template>
</CascadeSelect>