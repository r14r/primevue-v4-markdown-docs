<DataTable v-model:filters="filters" v-model:selection="selectedCustomer" :value="customers"
    stateStorage="session" stateKey="dt-state-demo-session" paginator :rows="5" filterDisplay="menu"
    selectionMode="single" dataKey="id" :globalFilterFields="['name', 'country.name', 'representative.name', 'status']" tableStyle="min-width: 50rem">
    <template #header>
        <IconField>
            <InputIcon>
                <i class="pi pi-search" />
            </InputIcon>
            <InputText v-model="filters['global'].value" placeholder="Global Search" />
        </IconField>
    </template>
    <Column field="name" header="Name" sortable style="width: 25%">
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by name" />
        </template>
    </Column>
    <Column header="Country" sortable sortField="country.name" filterField="country.name" filterMatchMode="contains" style="width: 25%">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img alt="flag" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`flag flag-${data.country.code}`" style="width: 24px" />
                <span>{{ data.country.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <InputText v-model="filterModel.value" type="text" placeholder="Search by country" />
        </template>
    </Column>
    <Column header="Representative" sortable sortField="representative.name" filterField="representative" :showFilterMatchModes="false" :filterMenuStyle="{ width: '14rem' }" style="width: 25%">
        <template #body="{ data }">
            <div class="flex items-center gap-2">
                <img :alt="data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${data.representative.image}`" style="width: 32px" />
                <span>{{ data.representative.name }}</span>
            </div>
        </template>
        <template #filter="{ filterModel }">
            <MultiSelect v-model="filterModel.value" :options="representatives" optionLabel="name" placeholder="Any">
                <template #option="slotProps">
                    <div class="flex items-center gap-2">
                        <img :alt="slotProps.option.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.option.image}`" style="width: 32px" />
                        <span>{{ slotProps.option.name }}</span>
                    </div>
                </template>
            </MultiSelect>
        </template>
    </Column>
    <Column field="status" header="Status" sortable filterMatchMode="equals" style="width: 25%">
        <template #body="{ data }">
            <Tag :value="data.status" :severity="getSeverity(data.status)" />
        </template>
        <template #filter="{ filterModel }">
            <Select v-model="filterModel.value" :options="statuses" placeholder="Select One" showClear>
                <template #option="slotProps">
                    <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
                </template>
            </Select>
        </template>
    </Column>
    <template #empty> No customers found. </template>
</DataTable>